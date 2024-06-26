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

    def test_network_address(self):
        s = Subnet('10.1.1.150', 25)
        self.assertEqual(s.network_address(), '10.1.1.128')

        s = Subnet('10.1.199.50', 18)
        self.assertEqual(s.network_address(), '10.1.192.0')
        
        s = Subnet('10.1.1.1', 16)
        self.assertEqual(s.network_address(), '10.1.0.0')
        
        s = Subnet('10.1.1.1', 6)
        self.assertEqual(s.network_address(), '8.0.0.0')

    def test_broadcast_address(self):
        s = Subnet('10.1.1.25', 25)
        self.assertEqual(s.broadcast_address(), '10.1.1.127')

        s = Subnet('10.1.199.50', 18)
        self.assertEqual(s.broadcast_address(), '10.1.255.255')
        
        s = Subnet('10.1.1.1', 16)
        self.assertEqual(s.broadcast_address(), '10.1.255.255')
        
        s = Subnet('10.1.1.1', 6)
        self.assertEqual(s.broadcast_address(), '11.255.255.255')

if __name__ == '__main__':
    unittest.main()
