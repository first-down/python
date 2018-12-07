import  unittest
import HTMLTestRunnertest
import time
class ba():
    def run(self, aa):
        suit = unittest.TestSuite()
        for a in aa:
            disvover = unittest.defaultTestLoader.discover(r'..\test_dian', pattern='{}.py'.format(a.strip()))
            suit.addTest(disvover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open('adc.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='幸存者',
                                                       description='测试结果如下：',
                                                       title='好分数测试报告',
                                                       stream=f)
        runner.run(suit)
        f.close()
