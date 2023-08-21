import threading
import requests
import logging
import time
from queue import Queue

class GetDate(threading.Thread):
    def __init__(self, timestamp_queue):
        super().__init__()
        self.timestamp_queue = timestamp_queue

    def write_log(self, timestamp):
        response = requests.get(f"http://127.0.0.1:8080/timestamp/{timestamp}")
        date = response.text.strip()
        logger.info(f"{timestamp} {date}")

    def run(self):
        while True:
            try:
                timestamp = self.timestamp_queue.get(timeout=1)
                if timestamp is None:
                    break
                self.write_log(timestamp)
                self.timestamp_queue.task_done()
            except queue.Empty:
                break

def main():
    timestamp_queue = Queue()

    current_timestamp = int(time.time())
    for _ in range(10):
        timestamp_queue.put(current_timestamp)
        current_timestamp += 1

    threads = []
    for _ in range(10):
        th = GetDate(timestamp_queue)
        threads.append(th)
        th.start()

    for thr in threads:
        thr.join()

    for _ in range(10):
        timestamp_queue.put(None)

    for thr in threads:
        thr.join()

    timestamp_queue.join()

if __name__ == "__main__":
    main()
