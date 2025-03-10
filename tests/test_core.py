import sys
import os
import unittest

currentDir = os.path.dirname(__file__)
srcDir = os.path.join(currentDir, "..")

srcDir = os.path.normpath(srcDir)
sys.path.append(os.path.normpath(srcDir))


from src.modules.utils.connection import checkConnection
from src.modules.utils.validation import validateIP


targetIP = "8.8.8.8"


class testConnection(unittest.TestCase):

    def test_check_connection(self):
        try:
            checkConnection(targetIP)
            result = True

        except SystemExit: 
            result = False
        self.assertTrue(result)

    def test_validate_IP(self):
        self.assertTrue(validateIP("8.8.8.8"))
        self.assertFalse(validateIP("256.256.256.256"))
        self.assertFalse(validateIP("abcd"))


if __name__ == "__main__":
    unittest.main()