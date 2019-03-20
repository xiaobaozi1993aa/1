import os
from datetime import *
import time
#a = os.popen('adb devices').readlines()
#b = os.popen('adb shell dumpsys meminfo com.sz.gcyh.KSHongBao').read()
#c = os.popen('adb shell top -n -1 | find "com.sz.gcyh.KSHongBao"').read()
#result = os.popen("adb shell dumpsys cpuinfo | findstr "+"com.sz.gcyh.KSHongBao").readlines()
#print(result)


  #  com.sz.gcyh.KSHongBao

def testRunTime():
    result = os.popen("adb shell dumpsys cpuinfo | findstr "+"com.sz.gcyh.KSHongBao").readlines()
    print(result)
    cputotle = 0
    for line in result:
        if len(line) > 0:
            cpu = line.split("%")[0].strip()
            #print(cpu)
            if len(cpu) > 0:
                cputotle = cputotle + float(cpu)
                a = str(cputotle)+"\n"
                print(a,datetime.now())

if __name__ == '__main__':
    for i in range(3):
        testRunTime()
