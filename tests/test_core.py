import sys
import os
import unittest

current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, "..")

src_dir = os.path.normpath(src_dir)
sys.path.append(os.path.normpath(src_dir))

from src.modules.utils.connection import checkConnection
from src.modules.utils.validation import validateIP

targetIP = "8.8.8.8"

class TestConnection(unittest.TestCase):

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