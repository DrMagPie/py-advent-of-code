#! /usr/bin/env python
from pathlib import Path
from typing import Tuple
import json

import requests

from .config import cache_dir


def get_known_wrong_answers(file: Path):
  if not file.exists():
    return {}
  with open(file, "r") as f:
    return json.load(f)


def known_wrong(file: Path, answer: str):
  data = get_known_wrong_answers(file)
  if answer in data:
    return data[answer]


def cache_wrong(file: Path, answer: str, message: str):
  file.parent.mkdir(parents=True, exist_ok=True)
  data = get_known_wrong_answers(file)
  data[answer] = message
  with open(file, "w") as f:
    json.dump(data, f)


def submit_answer(year: int, day: int, part: int, session: object, answer: str) -> Tuple[str, bool]:
  """Save submitted answer to file of problem"""
  invalid_answers_file = cache_dir.joinpath(session.get("name"), "invalid-answers", str(year), str(day), str(part))
  if known := known_wrong(invalid_answers_file, answer):
    return (known, True)

  payload = {"level": part, "answer": answer}
  cookies = {"session": session.get("value")}
  response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", payload, cookies=cookies)
  if response.status_code != 200:
    return "Error Submitting a Solution Online doesn't got response code 200", True
  text_data = response.text
  if "too high" in text_data:
    cache_wrong(invalid_answers_file, answer, "Your answer is too high")
    return "Your answer is too high", True
  elif "too low" in text_data:
    cache_wrong(invalid_answers_file, answer, "Your answer is too low")
    return "Your answer is too low", True
  elif "That's not" in text_data:
    cache_wrong(invalid_answers_file, answer, "That's not the right answer")
    return "That's not the right answer", True
  elif "You don't seem" in text_data:
    return "You don't seem to be solving right level", True
  elif "You gave an answer" in text_data:
    return "You have to wait for 1 min before submitting next solution", True
  elif "That's the right answer" in text_data:
    submitted_file = cache_dir.joinpath(session.get("name"), str(year), str(day), str(part))
    submitted_file.parent.mkdir(parents=True, exist_ok=True)
    with open(submitted_file, "a") as opened_file:
      opened_file.write(str(answer))
    return "Congratulation, you have solved question successfully", False
