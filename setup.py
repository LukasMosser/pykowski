try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pykowski',
    version='0.1.0',
    author='Lukas Mosser',
    author_email='lukas.mosser@gmail.com',
    packages=['pykowski', 'pykowski.tests'],
    description='Computation of Minkowski Tensors in Python',
    test_suite='pykowski.tests.get_suite',
    install_requires=requirements
)
