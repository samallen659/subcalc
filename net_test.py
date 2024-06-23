import unittest

from net import Subnet

class TestSubnet(unittest.TestCase):
    def test_setup(self):
        s = Subnet('172.22.220.1', 24)
        self.assertEqual(s.ip, '172.22.220.1')
        self.assertEqual(s.mask, 24)

    def test_calc_ip_bin(self):
        s = Subnet('172.22.220.1', 24)
        
        self.assertListEqual(s.ip_bin, [bin(172), bin(22), bin(220), bin(1)])

    def test_calc_mask_bin(self):
        s = Subnet('172.22.220.1', 24)

        self.assertListEqual(s.mask_bin, [bin(255), bin(255), bin(255), bin(0)])
        self.assertEqual(s.mask_bin_str, '11111111.11111111.11111111.00000000')


if __name__ == '__main__':
    unittest.main()
