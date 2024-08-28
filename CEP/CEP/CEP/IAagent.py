import os
import json
from transformers import GPT2Tokenizer
from gpt4all import GPT4All
from openai import OpenAI
from dotenv import load_dotenv

class IAGeneratorInterface:
    """Define la interfaz común para los generadores de IA.
    
    Esta interfaz establece el método que todas las clases generadoras de IA deben implementar.
    """
    
    def generate(self, prompt):
        """Genera una salida basada en un mensaje de entrada.
        
        Args:
            prompt (str): Mensaje de entrada para el generador.
        
        Returns:
            str: La salida generada por el modelo de IA.
        
        Raises:
            NotImplementedError: Si el método no ha sido implementado por la subclase.
        """
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class GPTgeneratorStructure(IAGeneratorInterface):
    def __init__(self, model_name='orca-mini-3b-gguf2-q4_0.gguf'):
        try:
            self.model = GPT4All(model_name)
        except ValueError as e:
            print(f"Error al inicializar el modelo GPT4All: {e}")
            self.model = None  # O podrías establecer un modelo alternativo aquí

    def generate(self, prompt):
        if not self.model:
            print("El modelo no se ha inicializado correctamente.")
            return ""
        try:
            return self.model.generate(prompt)
        except Exception as e:
            print(f"Error al generar con GPT4All: {e}")
            return ""


class OpenAIgeneratorStructure(IAGeneratorInterface):
    def __init__(self,model_name='gpt-3.5-turbo-0125'):
        self.model_name = model_name
        self.client = OpenAI()

    def generate(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=
                [
                    {
                    "role": "user", 
                    "content": prompt
                    }
                ],
                max_tokens=100
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error en la generación con OpenAI: {e}")
            return ""


class IAagent:
    def __init__(self, generator_model):
        self.generator = generator_model

    def generate_structure_project(self, description):
        prompt = self._build_prompt(description)

        try:
            structure_json = self.generator.generate(prompt)
            structure = json.loads(structure_json)
            self.generate_structure(structure)
        except Exception as e:
            print(f"Error al generar la estructura solicitada: {e}")

    def _build_prompt(self, description):
        return f"""
        Tienes la tarea de generar una estructura de proyecto basada en la siguiente descripción. La estructura debe incluir directorios y archivos organizados de manera lógica y debe devolverse en formato JSON. 

        Descripción del proyecto:
        {description}

        La estructura JSON debe incluir:
        - Directorios principales como claves.
        - Archivos dentro de cada directorio como listas de valores.
        - Asegúrate de incluir archivos de configuración específicos del lenguaje, si son necesarios.
        - Incluye archivos de documentación si son necesarios.

        Ejemplo de estructura JSON para un proyecto de API en Python:
        {{
            "api_project": {{
                "src": ["main.py", "utils.py", "config.py", "__init__.py"],
                "tests": ["test_main.py", "test_utils.py"],
                "docs": ["README.md"],
                "config": ["config.yaml", "logging.conf"]
            }}
        }}

        Ejemplo de estructura JSON para un proyecto React:
        {{
            "react_project": {{
                "src": ["App.js", "index.js"],
                "public": ["index.html"],
                "docs": ["README.md"]
            }}
        }}

        Por favor, ajusta la estructura JSON a la descripción del proyecto proporcionado. Si la descripción incluye algún lenguaje específico o tipo de proyecto no cubierto en los ejemplos, asegúrate de incluir los archivos y directorios relevantes para ese contexto.
        """

    def generate_structure(self, structure):
        base_path = os.path.join(os.getcwd(), "my_project")
        os.makedirs(base_path, exist_ok=True)
        
        for folder, files in structure.items():
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            for file in files:
                file_path = os.path.join(folder_path, file)
                open(file_path, 'w').close()
        print(f"Estructura del proyecto 'my_project' creada exitosamente!")

    def calculate_costs(self, description, prompt, model_name, max_tokens=100):
        precios = {
            "gpt-4-0125-preview": {"input_cost": 0.01, "output_cost": 0.03},
            "gpt-4-1106-preview": {"input_cost": 0.01, "output_cost": 0.03},
            "gpt-4-1106-vision-preview": {"input_cost": 0.01, "output_cost": 0.03},
            "gpt-4": {"input_cost": 0.03, "output_cost": 0.06},
            "gpt-4-32k": {"input_cost": 0.06, "output_cost": 0.12},
            "gpt-3.5-turbo-0125": {"input_cost": 0.0005, "output_cost": 0.0015},
            "gpt-3.5-turbo-instruct": {"input_cost": 0.0015, "output_cost": 0.002}
        }
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        len_token_prompt = len(tokenizer.tokenize(prompt))
        len_token_description = len(tokenizer.tokenize(description))
        input_cost = (len_token_prompt + len_token_description / 1000) * precios[model_name]["input_cost"]
        output_cost = (max_tokens / 1000) * precios[model_name]["output_cost"]

        return (len_token_prompt + len_token_description, input_cost + output_cost)

    def ia_structure(self, description, model_name='gpt-3.5-turbo-0125', max_tokens=100):
        """Realiza la generación de la estructura utilizando el modelo especificado."""
        prompt = self._build_prompt(description)
        tokens, cost = self.calculate_costs(description, prompt, model_name, max_tokens)
        response = input(f"El resultado tiene una longitud de: {tokens} tokens (aprox. {cost} dólares), ¿desea procesarlo? (s/n): ")
        if response.lower() in ('y', 'yes'):
            load_dotenv()  # Cargamos las variables de entorno
            self.generate_structure_project(description)
