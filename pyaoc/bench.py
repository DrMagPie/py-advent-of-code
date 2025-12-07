#! /usr/bin/env python
from tqdm import trange

from time import perf_counter_ns

from .get_input import get_input
from .get_session import get_session
from .utils import format_time


def bench(year: int, day: int, times: int = 100, progress: bool = False, print_all_runs: bool = False, session_name: str = None) -> any:
  """Wrapper function to get input and benchmark solver function

  Args:
      year (int): year of event
      day (int): day of year
      times (int): number of times function will be measured
      progress (bool): print a progress bar
      print_all_runs (bool): prints results array with all run times
      session_name (str, optional): Name of session token to use, if not provided will prompt to input. Defaults to None.

  Returns:
      any: anything returned by solver function
  """

  session = get_session(session_name, False)

  def decorator(function):
    input_data, _ = get_input(year, day, session)
    if not input_data:
      return function
    results = []
    runs = trange(times) if progress else range(times)
    for _ in runs:
      start = perf_counter_ns()
      function(input_data)
      end = perf_counter_ns()
      results.append(end - start)

    average = sum(results) / len(results)
    minimum = min(results)
    maximum = max(results)

    message = f"Average: {format_time(average)}\nMinimum: {format_time(minimum)}\nMaximum: {format_time(maximum)}"

    print(message)
    if print_all_runs:
      print(f"Results: {results}")
    return function

  return decorator
