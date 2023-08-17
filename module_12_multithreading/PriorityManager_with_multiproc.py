import multiprocessing
import logging
import random
import time
import queue

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Producer(multiprocessing.Process):
    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue

    def run(self):
        for _ in range(5):
            priority = random.randint(0, 10)
            task = (priority, f"Task {priority}")
            self.task_queue.put(task)
            logger.info(f'Produced Task {task[1]} with priority {task[0]}')

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue

    def run(self):
        while True:
            try:
                task = self.task_queue.get(timeout=1)  # Use a timeout to periodically check the queue
            except queue.Empty:
                break

            logger.info(f'Consumed Task {task[1]} with priority {task[0]}')
            time.sleep(random.random())  # Simulate task processing time

def main():
    task_queue = multiprocessing.Queue()

    producer = Producer(task_queue)
    consumer = Consumer(task_queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()
