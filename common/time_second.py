import time

def TimeSecond():
    second = time.strftime('%S ',time.localtime(time.time()))
    return int(second)
