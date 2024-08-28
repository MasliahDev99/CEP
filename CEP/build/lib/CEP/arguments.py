import argparse
import os,sys
from dotenv import load_dotenv,set_key
from generatorstructure import GeneratorStructure
from IAagent import IAagent,GPTgeneratorStructure,OpenAIgeneratorStructure

def get_arguments():
    parser = argparse.ArgumentParser(description="Esta herramienta sirve para crear la estructura de un proyecto")
    subparsers = parser.add_subparsers(dest="command")

    parser_config = subparsers.add_parser('configure', help="Inicia el proceso para configurar  o actualizar el fichero de configuracion .\nEj: configure start  / or configure reset")
    parser_config.add_argument('action', choices=['start','reset'], help="Acción para comenzar la configuración")

    # Comando para estructura de API
    parser_api = subparsers.add_parser("init_proyect_api", help="Crea una estructura básica para un proyecto de API")
    parser_api.add_argument("project_name", type=str, help="Nombre del proyecto")

    # Comando para estructura de React
    parser_rx = subparsers.add_parser("init_proyect_tsx", help="Crea una estructura básica para un proyecto web (React)")
    parser_rx.add_argument("project_name", type=str, help="Nombre del proyecto")

    # Comando para estructura de datos
    parser_data = subparsers.add_parser("init_proyect_data", help="Crea una estructura básica para un proyecto de ciencia de datos")
    parser_data.add_argument("project_name", type=str, help="Nombre del proyecto")

    # Comando para estructura de machine learning
    parser_ml = subparsers.add_parser("init_proyect_ml", help="Crea una estructura básica para un proyecto de machine learning")
    parser_ml.add_argument("project_name", type=str, help="Nombre del proyecto")


    # Comando para utilizar IA
    parser_gpt = subparsers.add_parser("init", help="Genera una estructura basada en una descripción utilizando IA.\nEj: init -gpt 'descripcion de la estructura' ")
    parser_gpt.add_argument("-gpt", type=str, help="Descripción de la estructura del proyecto")


    return parser.parse_args()




def openai_config():
    """Solicita al usuare la clave API KEY de openai"""
    OPENAI_API_KEY = input("Introduce la clave API key de OpenAI: ")
    set_key(".env","OPENAI_API_KEY",OPENAI_API_KEY)
    
def reset_config():
    set_key(".env","OPENAI_API_KEY","")



def handle_command(args):
    

    if args.command in ["init_proyect_api","init_proyect_tsx","init_proyect_data","init_proyect_ml"]:
        project_type_dict = {
        "init_proyect_api": "api",
        "init_proyect_tsx": "react",
        "init_proyect_data": "data_science",  
        "init_proyect_ml": "ml"
         }

        print(f"Este comando crea la estructura de un proyecto api.\nNombre del proyecto: {args.project_name}")
        project_type = project_type_dict.get(args.command)
        structure = GeneratorStructure(args.project_name)
        structure.create_structure(project_type)
        

    elif args.command == "configure":
        if args.action == "start":
            print(f"Comenzando el proceso de configuracion del fichero .env")
            choice = input("Desea actualizar el fichero de configuracion ? (s/n): ")
            if choice.lower() == 's':
                openai_config()
                print(f"\n[+] El fichero .env se ha actualizado correctamente!.")

        elif args.action == 'reset':
            print(f"Resetea el fichero .env")
            choice = input("Desea resetear el fichero de configuracion ? (s/n): ")
            if choice.lower() == 's':
                reset_config()
                print(f"\n[+] El fichero .env se ha reseteado correctamente!.")

    elif args.command == "init":
        description = args.gpt
        choice = input("Desea utilizar un modelo de inteligencia artificial local?(s/n): ")
        if choice.lower() == "s":
            print("Utilizar un modelo de ia local puede demorarar varios minutos....\n")
            gpt4all_generator = GPTgeneratorStructure()
            ia_agent = IAagent(gpt4all_generator)
            print(f"Descripcion del la estructura del proyecto:\n{description}")
            ia_agent.generate_structure_project(description=description)
        else:
            if os.path.exists(".env"):
                load_dotenv()  # Cargamos las variables del entorno
                OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
                if OPENAI_API_KEY is None:
                    print("Error: La clave API de OpenAI no está configurada en .env.")
                    sys.exit(1)
                openai_generator = OpenAIgeneratorStructure()
                ia_agent = IAagent(openai_generator)
                print(f"Este comando genera una estructura basada en una descripción utilizando un modelo de inteligencia artificial.\nDescripción: {description}")
                ia_agent.ia_structure(description)
                sys.exit(1)
            else:
                print("[!] Error: El fichero de configuración .env no existe.\nPara utilizar GPT-3.5 debe configurar el fichero '.env' con el comando 'configure start'")
                sys.exit(1)

        

        
        #tendria que emitir un mensaje avisando al usuario del costo de la consulta y si desea generarlo
        print(f"Este comando genera una estructura basada en una descripcion utilizando un modelo de inteligencia artificial.\nDescripcion: {description}")
        ia_agent.ia_structure(description)
        sys.exit(1)

    else:
        print(f"Comando ingresado incorrecto. Ingrese: cep -h para obtener informacion de los comandos.")




    