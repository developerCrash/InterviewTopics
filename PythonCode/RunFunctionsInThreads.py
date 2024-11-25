import threading

def print_num(n):
    for i in range(n):
        print(i)

def print_more_num(n):
    for i in range(n):
        print(i*i)


thread1 = threading.Thread(target=print_num(10))
thread2 = threading.Thread(target=print_more_num(20))

thread1.start()
thread2.start()

thread1.join()
thread2.join()


