import unittest

from net import Subnet

class TestSubnet(unittest.TestCase):
    def test_setup(self):
        s = Subnet('172.22.220.1', 24)
        self.assertEqual(s.ip, '172.22.220.1')
        self.assertEqual(s.mask, 24)

if __name__ == '__main__':
    unittest.main()
