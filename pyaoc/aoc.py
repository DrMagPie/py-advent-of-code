#! /usr/bin/env python

from time import perf_counter_ns

from .check_status import check_status
from .get_input import get_input
from .get_session import get_session
from .submit_answer import submit_answer
from .utils import format_time


def aoc(year: int, day: int, part: int, session_name: str = None, submit: bool = True, reset_session: bool = False) -> any:
  """Wrapper function to get input, call solver function and submit answer

  Args:
      year (int): year of event
      day (int): day of year
      part (int): part of day
      session_name (str, optional): Name of session token to use, if not provided will prompt to input. Defaults to None.
      submit (bool, optional): Enable/Disable automatic submissions. Defaults to True.

  Returns:
      any: anything returned by solver function
  """
  session = get_session(session_name, reset_session)

  def decorator(function):
    answer = previous = check_status(year, day, part, session.get('name'))
    message, status, end = '', '✅' if previous else '❔', None
    input_data, message = get_input(year, day, session)
    if input_data:
      start = perf_counter_ns()
      answer = str(function(input_data))
      end = perf_counter_ns() - start
      if previous: status = '✅' if previous == answer else '❌'
      elif submit:
        message, err = submit_answer(year, day, part, session, answer)
        status = '❌' if err else '✅'
    print(f'{status}| {year}-{day}-{part} => {answer} 🕛 {format_time(end)}\t{message}')
    return function

  return decorator


def get_puzzle_input(year: int, day: int, session_name: str = None, reset_session: bool = False) -> str:
  """Gets challenges input

  Args:
      year (int): year of event
      day (int): day of year
      session_name (str, optional): Name of session token to use, if not provided will prompt to input. Defaults to None.

  Returns:
      str: input data
  """
  return get_input(year, day, get_session(session_name, reset_session))[0]
