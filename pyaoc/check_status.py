#! /usr/bin/env python
import os
from pathlib import Path

import appdirs


def check_status(year: int, day: int, part: int, session_name: str) -> str:
  """Checks problem status. Solved or not"""
  answer_file = Path(os.path.join(appdirs.user_cache_dir(appname="AdventOfCode"), session_name, str(year), str(day), str(part)))
  if answer_file.exists():
    with open(answer_file) as opened_file:
      return opened_file.read()
  return None
