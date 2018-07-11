from distutils.core import setup
from Cython.Build import cythonize
import numpy 

setup(name='Fast R-CNN',
      ext_modules=cythonize("nms.pyx", include_path = [numpy.get_include()]))