from threading import Lock
from typing import Callable
import time

class FooBar_Lock:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()

class FooBar_time_sleep:
    def __init__(self, n):
        self.n = n
        self.lock = 1


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while not self.lock:
                time.sleep(0)
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock = 0


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while self.lock:
                time.sleep(0)
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock = 1