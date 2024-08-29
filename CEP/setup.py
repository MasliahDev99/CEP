from setuptools import setup, find_packages


def read_requirements(filename):
    """Lee un archivo de requerimientos y devuelve una lista de dependencias."""
    with open(filename,'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='create_structure_projects',
    version='0.1',
    packages=find_packages(),
    install_requires = read_requirements('requirements.txt'),
    description='Cep es una herramienta útil para crear la estructura inicial de tus proyectos de manera rápida y sencilla. Con Cep, puedes configurar fácilmente la estructura de directorios y archivos necesarios para distintos tipos de proyectos, ahorrándote tiempo en la organización de tu trabajo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='MasliahDev99',
    author_email='felipe_dev99@outlook.es',
    url='https://github.com/MasliahDev99/CEP',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
)
