#! /usr/bin/env python
import os
import appdirs
from pathlib import Path

def get_session(session_name: str) -> str:
  """Return session name value from config file"""
  config_dir = appdirs.user_config_dir(appname='AdventOfCode')
  if not session_name:
    session_list = os.listdir(config_dir)
    if session_list != []:
      session_name = session_list[0]
    else:
      session_name = 'default'
  config_file = Path(os.path.join(config_dir, session_name, 'token'))
  if not config_file.exists():
    # os.makedirs(os.path.dirname(config_file), exist_ok=True)
    Path(os.path.dirname(config_file)).mkdir(parents=True, exist_ok=True)
    token = input("Enter Session Token: ")
    with open(config_file, "a+") as opened_file:
      opened_file.write(token)
  with open(config_file) as opened_file:
    return {'name': session_name, 'value': opened_file.read()}