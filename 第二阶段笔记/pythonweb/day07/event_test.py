from multiprocessing import Event
#创建事件对象
e=Event()
print(e.is_set())
e.set()
print(e.is_set())
#将设置清除　wait又阻塞
e.clear()
e.wait()