# Overview

Personal project on understanding mulit threading and multi processing based on Python. \
The idea for this is based on the following [Medium Post](https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29).

The tests for the scripts have been made on the MacBook Pro (14", 2021) using the Apple M1 Pro with 8 CPU Kernels. 

## Multi Threading in Python

As described in the article, multi threading can make sense in the case of simple [I/O (Input/Output) tasks](https://en.wikipedia.org/wiki/I/O_bound).

We are going to compare a simple downloading tasks without any multi-threading (see notebook [simple_io_task.py](https://github.com/johanneseder711/mul/blob/main/simple_io_task.py)) to the same task using mulit threading (see notebook [multithreaded_io_task.py](https://github.com/johanneseder711/mul/blob/main/multithreaded_io_task.py)).

### Results

To measure the time needed to execute the notebooks I used the commands `time python simple_io_task.py` and the same for the multithreaded notebook `time python multithreaded_io_task.py`.

__simple_io_task.py__: 1,95s user 0,28s system 18% cpu 12,333 total

__multithreaded_io_task.py__: 1,00s user 0,14s system 46% cpu 2,485 total

We can already see a clear time gain in using the multi threaded version of our notebook.

You may also want to investigate on why multi-threading in Pyhton may not always be a good idea (or faster than a normal implementation) as described in this [article](https://hackernoon.com/concurrent-programming-in-python-is-not-what-you-think-it-is-b6439c3f3e6a). _Spoiler Alert_: As explained in the Medium article, the reason for this is the __Python GIL__ (Global Interpreter Lock).
## Multiprocessing in Python

In this part we want to have a look at parallelism in Python, e.g. using the multiple CPU's available on my Mac to achieve performance gains by executing multiple tasks literally at the same time.
To make use of multiprocessing we need a [CPU-bound](https://en.wikipedia.org/wiki/CPU-bound) task. We will use the same function as proposed in the Mediun article above, which is a function appending random integers to a list. 

### Results

__simple_cpu_task.py__: 11,42s user 0,23s system 99% cpu 11,651 total 

__multiprocessed_cpu_task.py__: 12,65s user 0,31s system 197% cpu 6,572 total

We notice almost only half the time needed when performing the task with multiprocessing. The CPU usage also confirms the correct execution utilizing 2 CPU's when performing multiprocessing. 

Interestingly the CPU user time in the multiprocessing example is higher than the total time needed for executing the task. This is because CPU user time is the accumulated time for all CPU's. Since we are using 2 CPU's the time for each is added, therefore resulting in a higher CPU user time than total time.
For more on the meaning of user, sys and total check out this [Stackoverflow post](https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1)


