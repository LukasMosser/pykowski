import unittest


class TestSomething(unittest.TestCase):
    def test_something_else(self):
        self.assertEqual(True, True)


def get_suite():
    "Return a unittest.TestSuite."
    import pykowski.tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(pykowski.tests)
    return suite
