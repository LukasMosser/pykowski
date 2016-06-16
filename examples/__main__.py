# RUNME as 'python -m pykowski.tests.__main__'
import unittest
import pykowski.tests


def main():
    "Run all of the tests when run as a module with -m."
    suite = pykowski.tests.get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
