#! /usr/bin/env python
import os
from pathlib import Path

import appdirs
import requests


def submit_answer(year: int, day: int, part: int, session: object, answer: str) -> (str, bool):
  """Save submitted answer to file of problem"""
  payload = {'level': part, 'answer': answer}
  cookies = {'session': session.get('value')}
  response = requests.post(f'https://adventofcode.com/{year}/day/{day}/answer', payload, cookies=cookies)
  if response.status_code != 200:
    return "Error Submitting a Solution Online doesn't got response code 200", True
  text_data = response.text
  if "too high" in text_data:
    return "Your answer is too high", True
  elif "too low" in text_data:
    return "Your answer is too low", True
  elif "That's not" in text_data:
    return "That's not the right answer", True
  elif "You don't seem" in text_data:
    return "You don't seem to be solving right level", True
  elif "You gave an answer" in text_data:
    return "You have to wait for 1 min before submitting next solution", True
  elif "That's the right answer" in text_data:
    submitted_file = Path(os.path.join(appdirs.user_cache_dir(appname="AdventOfCode"), session.get('name'), str(year), str(day), str(part)))
    Path(os.path.dirname(submitted_file)).mkdir(parents=True, exist_ok=True)
    with open(submitted_file, "a") as opened_file:
      opened_file.write(str(answer))
    return "Congratulation, you have solved question successfully", False
