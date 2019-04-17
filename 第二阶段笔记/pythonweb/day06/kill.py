import os
import signal
#向43903进程发送SIGKILL信号
os.kill(43903,signal.SIGKILL)
