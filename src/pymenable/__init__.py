""" src/pymenable//__init__.py 
"""

# read version from installed package
from importlib.metadata import version
__version__ = version("pymenable")


from .config import initEnv, getEnv  
from .openpage import openPage 


## end of file 