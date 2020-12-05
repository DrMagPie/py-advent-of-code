#! /usr/bin/env python

from .get_sesion import get_session
from .check_status import check_status
from .get_input import get_input
from .submit_answer import submit_answer

def AdventOfCode(year: int, day: int, part: int, session_name: str = None, submit: bool = True):
  session = get_session(session_name)
  def decorator(function):
    answer = check_status(year, day, part, session.get('name'))
    status = '✅'
    message = ''
    if not answer:
      status = '❔'
      input_data, message = get_input(year, day, session)
      if not input_data:
        print(message)
        return
      answer = function(input_data)
      if submit:
        message, err = submit_answer(year, day, part, session, answer, message)
        if err:
          status = '❌'
        else:
          status = '✅'
    print(f'{status}| {session.get("name")}/{year}-{day}-{part}/{answer}\t{message}')
  return decorator