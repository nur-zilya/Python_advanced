import threading
import queue
import logging
import random


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Producer(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore, description, priority):
        super().__init__()
        self.sem = semaphore
        self.description = description
        self.priority = priority

    def run(self):
        task = (self.priority, self.description)
        task_manager.add_task(task)
        logger.info(f'Produced Task {self.description} with priority {self.priority}')
        self.sem.release()

class TaskManager:
    def __init__(self):
        self.task_queue = queue.PriorityQueue()
    def add_task(self, task):
        self.task_queue.put(task)


class Consumer(threading.Thread):
    def __init__(self,semaphore):
        super().__init__()
        self.sem = semaphore

    def run(self):
        while True:
            self.sem.acquire()
            task = task_manager.task_queue.get()
            task_manager.task_queue.task_done()
            logger.info(f'Consumed Task {task[1]} with priority {task[0]}')

if __name__ == "__main__":
    task_manager = TaskManager()
    semaphore = threading.Semaphore(0)

    producers = []
    for _ in range(5):
        producer = Producer(semaphore, f"Task {random.randint(0, 10)}", random.randint(0,10))
        producers.append(producer)
    consumer = Consumer(semaphore)

    for producer in producers:
        producer.start()

    consumer.start()

    for producer in producers:
        producer.join()




