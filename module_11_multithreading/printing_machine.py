import logging
import random
import threading
import time

TOTAL_TICKETS = 10
SEATS_CAPACITY = 20
TICKETS_THRESHOLD = 4

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')

        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))

class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        while TOTAL_TICKETS < SEATS_CAPACITY:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS + TICKETS_THRESHOLD > SEATS_CAPACITY:
                    tickets_to_add = SEATS_CAPACITY - TOTAL_TICKETS
                else:
                    tickets_to_add = TICKETS_THRESHOLD

                TOTAL_TICKETS += tickets_to_add
                logger.info(f'Director added {tickets_to_add} tickets; total tickets {TOTAL_TICKETS}')

        logger.info('Director finished adding tickets')

    def random_sleep(self):
        time.sleep(random.randint(1, 3))

def main():
    semaphore = threading.Semaphore()
    sellers = []

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    director = Director(semaphore)
    director.start()

    for seller in sellers:
        seller.join()

    director.join()

if __name__ == '__main__':
    main()
