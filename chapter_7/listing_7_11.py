from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:
        print('Acquired lock a from method a!')
        time.sleep(1)
        with lock_b:
            print('Acquired both locks from method a!')


def b():
    with lock_b:
        print('Acquired lock b from method b!')
        with lock_a:
            print('Acquired both locks from method b!')


t1 = Thread(target=a)
t2 = Thread(target=b)
t1.start()
t2.start()
t1.join()
t2.join()
