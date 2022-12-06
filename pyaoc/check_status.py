#! /usr/bin/env python
from .config import cache_dir


def check_status(year: int, day: int, part: int, session_name: str) -> str:
  """Checks problem status. Solved or not"""
  answer_file = cache_dir.joinpath(session_name, str(year), str(day), str(part))
  if answer_file.exists():
    with open(answer_file) as opened_file:
      return opened_file.read()
  return None
