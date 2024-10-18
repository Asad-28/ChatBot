from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.

    Args:
        file_path (str): The path to the requirements.txt file.

    Returns:
        List[str]: A list of requirements, each representing a package or dependency.
        
    Details:
        - This function reads the content of the given file, line by line.
        - It removes any newline characters from each requirement.
        - If the constant 'HYPEN_E_DOT' (commonly used for '-e .' in requirements) is present,
          it will be removed from the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='chatbot',
version='0.0.1',
author='Asad',
author_email='asadchoudhary321@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)