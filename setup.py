from setuptools import setup,find_packages
from typing import List

def get_requirements(filepath:str)->List[str]:
   requirement=[]
   list1=[]
   with open(filepath) as f:
       requirement=f.readlines()
    
   for req in requirement:
        x=req.replace('\n','')
        list1.append(x)
        
   if "-e ." in list1:
       list1.remove("-e .")
   
   return list1
           

setup(
    name="Covid Prediction Machine learning project",
    version='0.0.1',
    author='Karthik',
    author_email='rajnairkarthik9325@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)