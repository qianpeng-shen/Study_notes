import signal
from time import sleep

signal.alarm(5)
#采用默认的方法处理
# signal.signal(signal.SIGALRM,signal.SIG_DFL)
#忽略方法
signal.signal(signal.SIGALRM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)
while True:
    sleep(2)
    print("让你按ctrl+c")
    print("等待时钟")

# import signal
# from time import sleep
# signal.alarm(5)
# signal.signal(signal.SIGALRM,signal.SIG_IGN)
# while True:
#     sleep(1)
#     print("事件阻塞")