from time import perf_counter_ns


def timer(fnc):
  """A decorator that uses time functions execution

  Args:
      fnc (any): function to profile
  """
  def inner(*args, **kwargs):
    start = perf_counter_ns()
    retval = fnc(*args, **kwargs)
    end = perf_counter_ns() - start
    if end > 1000000000: end = f'{end / 1000000000:.3f} s'
    elif end > 1000000: end = f'{end / 1000000:.3f} ms'
    elif end > 1000: end = f'{end / 1000:.3f} µs'
    else: end = f'{end} ns'
    print(f'Time Taken:\t{end}')
    return retval

  return inner
