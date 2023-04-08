from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requriment(file_path:str)->List[str]:
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
    req=[r.replace('\n',' ') for r in req]
    if HYPEN_E_DOT in req:
        req.remove(HYPEN_E_DOT)
    return req

setup(name='house_price_regression',install_requires=get_requriment('requriement.txt'),
    packages=find_packages())