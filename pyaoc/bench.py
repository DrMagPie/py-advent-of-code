#! /usr/bin/env python

from time import perf_counter_ns

from .get_input import get_input
from .get_session import get_session
from .utils import format_time


def bench(year: int, day: int, session_name: str = None) -> any:
  """Wrapper function to get input and benchmark solver function

  Args:
      year (int): year of event
      day (int): day of year
      session_name (str, optional): Name of session token to use, if not provided will prompt to input. Defaults to None.

  Returns:
      any: anything returned by solver function
  """

  session = get_session(session_name, False)

  def decorator(function):
    input_data, _ = get_input(year, day, session)
    if not input_data: return function
    results = []
    for i in range(10):
      start = perf_counter_ns()
      function(input_data)
      end = perf_counter_ns()
      results.append(end - start)

    average = sum(results) / len(results)
    minimum = min(results)
    maximum = max(results)

    print(f'Average: {format_time(average)}\nMinimum: {format_time(minimum)}\nMaximum: {format_time(maximum)}\nResults: {results}')
    return function

  return decorator
