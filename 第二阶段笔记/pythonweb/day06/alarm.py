import signal
import time
#3秒后向自己发送个SIGALRM信号
#当设置多个时钟时最后一个会覆盖前面的时钟
signal.alarm(3)
signal.alarm(8)
#阻塞等待接收一个信号
signal.pause()
while True:
    time.sleep(1)
    print("等待时钟.....")


