import math
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Callable, Tuple, Dict
from queue import PriorityQueue
@dataclass
class Task:
   func: Callable
   priority: int
   args: Tuple = field(default_factory=tuple)
   kwargs: Dict = field(default_factory=dict)

   def execute(self) -> None:
       self.func(*self.args, **self.kwargs)

   def __str__(self):
       task_str = self.func.__name__ + '('

       f_args = ', '.join(map(repr, self.args))
       task_str += f_args

       if self.kwargs:
           f_kwargs = ', '.join(
               f'{k}={v!r}' for k, v in self.kwargs.items()
           )
           task_str += ', ' + f_kwargs

       task_str += ')'
       return task_str

class TaskQueue:
   def __init__(self):
       self.queue = PriorityQueue()

   def add_task(self, task: Task) -> None:
       print('Добавлена задача:', task)
       self.queue.put((task.priority, task))

   def execute_tasks(self) -> None:
       while not self.queue.empty():
           _, task = self.queue.get()
           print('Исполняется задача:', task)
           task.execute()
       print('Все задачи были успешно выполнены')

if __name__ == '__main__':
    queue = TaskQueue()
    queue.add_task(Task(
        func=time.sleep,
        priority=2,
        args=(1,)
    ))
    queue.add_task(Task(
        func=print,
        priority=1,
        args=('Hello', 'World'),
        kwargs={'sep': '_'}
    ))
    queue.add_task(Task(
        func=math.factorial,
        priority=3,
        args=(50,)
    ))
    queue.execute_tasks()
