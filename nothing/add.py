import json
import os
import time


second = time.time()
print(second)
while(1):
    if (time.time()-second )> 5:
        print(time.time())
        break