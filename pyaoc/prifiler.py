import cProfile, pstats, io


def profile(fnc):
  """A decorator that uses cProfile to profile a function

  Args:
    fnc (any): function to profile.
  """
  def inner(*args, **kwargs):
    pr = cProfile.Profile()
    pr.enable()
    retval = fnc(*args, **kwargs)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())
    return retval

  return inner
