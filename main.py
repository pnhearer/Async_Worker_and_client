import asyncio

from worker import Worker


async def main():
    my_queue = asyncio.Queue()
    broker = Worker("String_Printer", my_queue)
    # Initialize variable to insert obtuse data into queue
    integer = 0
    # Obtuse amount of iterations to append data into the queue; ideally you would push useful data or tasks into...
    #  the que.
    for _ in range(10):
        # Just adding 1 to interger(syntax sugar, nothing interesting here)
        integer += 1
        # Insert obtuse data into queue
        my_queue.put_nowait(integer)
    # Initialize a list to append tasks to for future ensuring of all tasks being cancelled. no runaway threads.
    tasks = []
    # for each entry in the queue (qsize checks the queue's size), create and schedule a Task
    for i in range(my_queue.qsize()):
        task = asyncio.create_task(broker.do_work(my_queue, task=my_queue.get()), name=f"Job_id: {i}")
        # Append newly created task object reference into the tasks list. Note that this is an actual reference to
        # the task.
        tasks.append(task)
    await my_queue.join()
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions= True)

if __name__ == '__main__':
    asyncio.run(main())
