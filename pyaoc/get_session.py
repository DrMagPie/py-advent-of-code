#! /usr/bin/env python
import os
from pathlib import Path

import appdirs


def get_session(name: str, reset: bool = False) -> str:
  """Return session name value from config file"""
  config_dir = appdirs.user_config_dir(appname='AdventOfCode')
  if not os.path.exists(config_dir):
    os.mkdir(config_dir)
  if not name:
    session_list = os.listdir(config_dir)
    name = session_list[0] if session_list != [] else 'default'
  config_file = Path(os.path.join(config_dir, name, 'token'))
  if not config_file.exists() or reset:
    # os.makedirs(os.path.dirname(config_file), exist_ok=True)
    Path(os.path.dirname(config_file)).mkdir(parents=True, exist_ok=True)
    token = input("Enter Session Token: ")
    with open(config_file, "a+") as opened_file:
      opened_file.write(token)
  with open(config_file) as opened_file:
    return {'name': name, 'value': opened_file.read()}