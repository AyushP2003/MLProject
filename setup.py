from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_req(file_path:str) ->List[str]:
    '''
    Function will return list of requirment
    '''
    req = []
    with open(file_path) as file:
        req = file.readlines()
        req = [re.replace("\n","") for re in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req

setup(
name='mlproject',
version= '0.0.1',
author= 'Ayush',
author_email='patelayush2512@gmail.com',
packages=find_packages(),
requires=get_req('requirements.txt')
)