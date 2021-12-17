# Import Statements
import asyncio
from asyncio import QueueEmpty


class Worker(object):
    """
    Generic worker class designed to be instantiated for any programmer-defined task involving async queues.
    In your main function when calling the worker's async methods use task to assign task for worker to complete.

    """

    def __init__(self, name, queue):
        self.name = name
        self.queue = queue
        self.status = "Inactive"
        self.current_task = None

    # Synchronous class method
    @property
    def current_task(self):
        if self.current_task is not None:
            return self.current_task

    @current_task.setter
    def current_task(self, task):
        self.task = task

    @property
    def state(self):
        if self.status is None:
            return self.status
        else:
            return self.status

    @state.setter
    def state(self, status):
        self.status = status

    # async class methods

    # Run-once - Do task assigned to the worker.
    async def do_work(self, queue, task):
        try:
            print(queue)
            if not queue.empty():
                self.status = "Working..."
                self.current_task = asyncio.current_task()
                print(f"Worker : {self.name} is {self.status}.\n"
                      f"Current Task is: {self.current_task}")
                await task
                queue.task_done()
                print(f"Worker : {self.name} has completed {self.current_task}.")
            else:
                self.status = "Inactive"
                print(f"Worker {self.name} is {self.status}")
        except Exception as error:
            return error
