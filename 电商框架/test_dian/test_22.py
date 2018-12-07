from 电商框架.config.peizhi import beizhi
from 电商框架.data.读取 import ssl
import unittest
class duan(unittest.TestCase,):
    tes_1 = beizhi().jine
    wen = ssl()
    def test_1(self):
        html=self.tes_1(int(self.wen[4][0]))
        self.assertNotEqual(html['code'],int(self.wen[5][1]))
    def test_2(self):
        html=self.tes_1(int(self.wen[5][0]))
        self.assertNotEqual(html['code'],int(self.wen[5][1]))
    def test_3(self):
        html=self.tes_1(int(self.wen[6][0]))
        self.assertNotEqual(html['code'],int(self.wen[6][1]))
if __name__=='__main__':
    unittest.main()