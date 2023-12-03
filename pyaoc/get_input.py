#! /usr/bin/env python
from typing import Tuple

import requests

from .config import cache_dir


def get_input(year: int, day: int, session: object) -> Tuple[str, str]:
  """Return cache file input data from cache folder for certain problem"""
  cache_file = cache_dir.joinpath(session.get('name'), str(year), str(day), 'input')
  input_data = None
  if not cache_file.exists():
    input_data = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session.get('value')}).text
    if "before it unlocks!" in input_data:
      return None, "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available."
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_file, "w+") as opened_file:
      opened_file.write(input_data)
  else:
    with open(cache_file) as opened_file:
      input_data = opened_file.read()
  return input_data.rstrip(), ''
