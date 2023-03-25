!pip install re
#importing nessecary libraries
import unittest
import re

def ohms(s):
    res = 1/sum(1/i for i in eval(s)) if s[0] == '[' else sum(eval(s))
    return str(res)

def resist(net):
    while '(' in net or '[' in net:
        net = re.sub(r'[\[\(][\d,. ]+[\)\]]', lambda x: ohms(x.group()), net)
    return round(float(net), 1)

class TestResist(unittest.TestCase):
    def test_resist(self):
        self.assertAlmostEqual(resist('(2,[3,6],2)'), 2.2)
        self.assertAlmostEqual(resist('[10, [20, (30, 40)], 50]'), 16.7)
        self.assertAlmostEqual(resist('[1, [2, [3, [4, [5, [6, 7]]]]]]'), 1.2)
        self.assertAlmostEqual(resist('(2.5, [3.7, 4.5], 1.2, [5.3, (3.5, 2.2)])'), 1.4)

if __name__ == '__main__':
    unittest.main()
