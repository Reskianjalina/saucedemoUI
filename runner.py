import unittest
from unittest.suite import TestSuite
import cart, login 
if __name__ == '__main__':

    #initalize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #add test to the test suite
    #suite.addTests(loader.loadTestsFromModule(First_Test))
    suite.addTests(loader.loadTestsFromModule(cart))
    suite.addTests(loader.loadTestsFromModule(login))

    #initalize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

