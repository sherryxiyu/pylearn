import threading
from time import sleep

class TestThreads:
    def send_msg(self, autobench):
        data = autobench.gd.gen_http_bin_data('ming', 's')
        sleep(2)
        autobench.hp.httpbin_post(data)
        print(data)

    def test_thread(self, autobench):
        threads = []
        for i in range(2):
            p = threading.Thread(target=self.send_msg, args=(autobench,))
            threads.append(p)
            p.start()
        for item in threads:
            item.join()

