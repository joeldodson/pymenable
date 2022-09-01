"""  pymenable/config.py
configuration of the jinja environment 
"""

import logging 
logger = logging.getLogger(__name__)

import os
import inspect 
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import List 

import pymenable 

env = None 

#######
def getEnv():
    return env

#######
def initEnv(templateDirs: List[str] = None) -> Environment:
    """
    to override any of the templates in pymenable, 
    create a template with the same name as the one to override,
    put it in some local directory,
    pass the local directory as an argument to initEnv 
    you can pass in multiple directories and jinja will search them in order for the given template 
    The passed in template directories will be listed before the pymenable template directory
    thus jinja will find your template first and use that one.
    """
    templates = [f'{os.path.dirname(inspect.getfile(pymenable))}\\templates']
    templates = templateDirs + templates if templateDirs else templates 
    global env 
    env = Environment(
        line_statement_prefix = '#',
        line_comment_prefix = '##',
        loader=FileSystemLoader(templates),
        autoescape=select_autoescape()
    )
    return env 

## end of file