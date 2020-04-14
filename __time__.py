import time

def timeStamp():
    timeArray = time.localtime()
    t = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return t

if __name__=='__main__':
    print(timeStamp())