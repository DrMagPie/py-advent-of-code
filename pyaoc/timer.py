from time import perf_counter_ns


def timer(fnc):
  """A decorator that uses time functions execution

  Args:
      fnc (any): function to profile
  """
  def inner(*args, **kwargs):
    start = perf_counter_ns()
    retval = fnc(*args, **kwargs)
    print(f'Time Taken:\t{(perf_counter_ns() - start)/1000} μs')
    return retval

  return inner
