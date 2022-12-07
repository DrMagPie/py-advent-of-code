#! /usr/bin/env python
import os

from .config import config_dir


def get_session(name: str, reset: bool = False) -> str:
  """Return session name value from config file"""

  if config_dir.exists() and not name:
    session_list = os.listdir(config_dir)
    name = session_list[0] if session_list != [] else 'default'
  elif not name:
    name = 'default'

  config_file = config_dir.joinpath(name, 'token')
  if not config_file.exists() or reset:
    token = input("Enter Session Token: ")
    config_file.parent.mkdir(parents=True, exist_ok=True)
    with open(config_file, "a+") as opened_file:
      opened_file.write(token)

  with open(config_file) as opened_file:
    return {'name': name, 'value': opened_file.read()}
