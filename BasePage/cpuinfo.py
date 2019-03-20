#/usr/bin/python
#encoding:utf-8
import os
import time
from datetime import datetime

#控制类
class Manager(object):
    def __init__(self, count,pagename):
      self.counter = count
      self.file = open('cpumessage.txt', 'w')
      self.pagename=pagename
    #单次测试过程
    def testRunTime(self):
        result = os.popen("adb shell dumpsys cpuinfo | findstr "+self.pagename).readlines()
        print(result)
        cputotle = 0
        for line in result:
            if len(line) > 0:
                cpu = line.split("%")[0].strip()
                if len(cpu) > 0:
                    cputotle = cputotle + float(cpu)
                    self.file.write('{} : {}'.format(datetime.now(),str(cputotle)+"\n"))
#多次执行测试过程
    def run(self):
        while self.counter >0:
            self.testRunTime()
            self.counter = self.counter - 1
            time.sleep(2)
            #关闭资源
        self.file.close()
if __name__ == "__main__":
    controller = Manager(10,"com.sz.gcyh.KSHongBao")
    controller.run()
