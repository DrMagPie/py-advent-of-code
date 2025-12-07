#! /usr/bin/env python
import os

from dotenv import load_dotenv

from .config import config_dir


def get_name():
  if name := os.environ.get("AOC_NAME"):
    return name

  if config_dir.exists():
    session_list = os.listdir(config_dir)
    return session_list[0] if session_list != [] else "default"

  return "default"


def get_token(name: str, reset: bool = False):
  if token := os.environ.get("AOC_TOKEN"):
    return token
  config_file = config_dir.joinpath(name, "token")
  if not config_file.exists() or reset:
    token = input("Enter Session Token: ")
    config_file.parent.mkdir(parents=True, exist_ok=True)
    with open(config_file, "w+") as f:
      f.write(token)
      return token
  with open(config_file) as f:
    return f.read()


def get_session(name: str, reset: bool = False) -> str:
  """Return session name value from config file"""
  load_dotenv()
  name = name if name else get_name()
  token = get_token(name, reset)
  return {"name": name, "value": token}
