try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pykowski',
    version='0.1.0',
    author='Lukas Mosser',
    packages=['pykowski'],
    description='Computation of Minkowski Tensors in Python'
)
