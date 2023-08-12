import threading
import time

class Ctroltest:
    def __init__(self):
        self.stop_thread = 0

    def control_time(self, t):
        time.sleep(t)
        print("time is up")
        self.stop_thread = 1

class TestClass():
    def test_case(self, Ctroltest):
        while True:
            time.sleep(1)
            print(time.time())
            if Ctroltest.stop_thread:
                break
        #print("case pass")

if __name__ == '__main__':
        print("hi")
        ct = Ctroltest()
        a = threading.Thread(target=ct.control_time, args=(5,))
        b = threading.Thread(target=TestClass().test_case, args=(ct,))
        print("startinga...")
        a.start()
        print("startingb...")
        b.start()

        a.join()
        b.join()


