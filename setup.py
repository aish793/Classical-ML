from setuptools import find_packages, setup
from typing import List

hyphen_e = "-e."
def get_requirements(file_path:str)->List:
    '''
    :param file_path:
    :return: Returns a list of requirements for the project
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [requirement.replace("\n", " ") for requirement in requirements]
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements

setup(
    name='MLProject',
    author='Aishwarya',
    author_email='aishwarya.jauhari@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)