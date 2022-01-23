# Overview

Personal project on understanding mulit threading and multi processing based on Python. \
The idea for this is based on the following [Medium Post](https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29).

The tests for the scripts have been made on the MacBook Pro (14", 2021) using the Apple M1 Pro with 8 CPU Kernels. 

## Multi Threading in Python

As described in the article, multi threading can make sense in the case of simple [I/O (Input/Output) tasks](https://en.wikipedia.org/wiki/I/O_bound).

We are going to compare a simple downloading tasks without any multi-threading (see notebook [simple_io_task.py](https://github.com/johanneseder711/mul/blob/main/simple_io_task.py)) to the same task using mulit threading (see notebook notebook_title_goes_here.py.

### Results

To measure the time needed to execute the notebooks I used the commands `time python simple_io_task.py` and the same for the multithreaded notebook `time python multithreaded_io_task.py`.

__simple_io_task.py__: 1,95s user 0,28s system 18% cpu 12,333 total
__multithreaded_io_task.py__: 1,00s user 0,14s system 46% cpu 2,485 total

We can already see a clear time gain in using the multi threaded version of our notebook. Further investigation of the notebook will be done.
