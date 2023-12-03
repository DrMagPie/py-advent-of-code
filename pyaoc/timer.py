from time import perf_counter_ns

from .utils import format_time


def time(fnc):
  """A decorator that uses time functions execution

  Args:
      fnc (any): function to profile
  """
  def inner(*args, **kwargs):
    start = perf_counter_ns()
    retval = fnc(*args, **kwargs)
    end = perf_counter_ns() - start
    print(f'Time Taken:\t{format_time(end)}')
    return retval

  return inner
