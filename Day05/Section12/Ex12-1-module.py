'''
파일명 : Ex12-1-module.py

모듈 (module)



import 모듈명

'''
from setuptools._distutils.command.config import config
import converter

miles = converter.kilometer_to_miles(150)
print('150km={}miles'.format(miles))

pounds = converter.gram_to_pounds(1000)
print('1000g=[]pounds'.format(pounds))
