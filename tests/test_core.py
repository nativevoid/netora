import sys
import os
import unittest

current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, "..")

src_dir = os.path.normpath(src_dir)
sys.path.append(os.path.normpath(src_dir))

from src.modules.utils.connection import check_connection
from src.modules.utils.validation import validate_ip

targetIP = "8.8.8.8"

class TestConnection(unittest.TestCase):

    def test_check_connection(self):
        try:
            check_connection(targetIP)
            result = True

        except SystemExit: 
            result = False
        self.assertTrue(result)

    def test_validate_IP(self):
        self.assertTrue(validate_ip("8.8.8.8"))
        self.assertFalse(validate_ip("256.256.256.256"))
        self.assertFalse(validate_ip("abcd"))

if __name__ == "__main__":
    unittest.main()