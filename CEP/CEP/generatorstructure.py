import os,sys
from structures import project_structures


class GeneratorStructure:
    def __init__(self, project_name):
        self.project_name = project_name

    def create_structure(self, project_type):
        print(f"Creating project structure for {self.project_name}")
        structure = project_structures.get(project_type)
        if not structure:
            raise ValueError(f"Unknown project type: {project_type}")

       
        self._create_directories_and_files(structure)

    def _create_directories_and_files(self, structure):
        base_path = os.path.join(os.getcwd(), self.project_name)
        os.makedirs(base_path, exist_ok=True)

       #creamos los directorios primero y luego todos los archivos 
        self._create_directories(base_path, structure)
        self._create_files(base_path, structure)

        print(f"Project structure for {self.project_name} created successfully.")

    #intentar refactorizar
    def _create_directories(self, base_path, structure):
        for folder, items in structure.items():
            folder_path = os.path.join(base_path, folder)
            if isinstance(items, list):  # si la instancia es una lista puede ser archivos o directorios
                for item in items:
                    item_path = os.path.join(folder_path, item)
                    if item.endswith('/'):
                        os.makedirs(item_path, exist_ok=True)
                    else:
                        os.makedirs(os.path.dirname(item_path), exist_ok=True)  # con exist_ok verificamos que el directorio exista
            elif isinstance(items, dict):  # si la instancia es un diccionario verificamos si hay directorios anidados
                os.makedirs(folder_path, exist_ok=True)
                self._create_directories(folder_path, items)

    def _create_files(self, base_path, structure):
        for folder, items in structure.items():
            folder_path = os.path.join(base_path, folder)
            if isinstance(items, list):  # verificamos los archivos
                for item in items:
                    file_path = os.path.join(folder_path, item)
                    if not os.path.exists(file_path):
                        with open(file_path, 'wb') as f:
                            pass  # Crea archivo vacío
            elif isinstance(items, dict):  
                self._create_files(folder_path, items)
