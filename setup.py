from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    this function will return list of requirements
    """
    req = []
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req = [r.replace("\n","") for r in req]

        if "-e ." in req:
            req.remove("-e .")

        return req

setup(
name = 'mlproject',
version='0.0.1',
author='SunRaku',
author_email='rajputsomesh78@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)