import json
import os
import time


second = time.strftime('%S ',time.localtime(time.time()))
print(second)

while(1):
    second = time.strftime('%S ', time.localtime(time.time()))
    if int(second) % 2 != 0:
        print(second)
