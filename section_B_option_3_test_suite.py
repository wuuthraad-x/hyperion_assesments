import unittest
from resist import resist

class TestResist(unittest.TestCase):
    def test_resist(self):
        # Test single resistor
        self.assertEqual(resist('10'), 10.0)
        
        # Test series resistors
        self.assertEqual(resist('2 + 3 + 4'), 9.0)
        
        # Test parallel resistors
        self.assertEqual(resist('1/2 + 1/3 + 1/4'), 1.31)
        
        # Test series and parallel resistors
        self.assertEqual(resist('2 + [3, 6, [8, 2]] + 4'), 6.7)
        
        # Test resistors with decimals and scientific notation
        self.assertEqual(resist('1.2 + 3e6 + 4.5e-3'), 3000004.7)
        
        # Test resistors with different units
        self.assertEqual(resist('100k + 1M + 2.2k'), 1222.2)
        
if __name__ == '__main__':
    unittest.main()
