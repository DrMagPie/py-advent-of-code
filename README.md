# Python Advent of Code Wrapper (pyaoc)

Small wrapper to decorate python functions.
Retrives Advent of Code Challenge Input, and submits results.

innstall via `pip install https://github.com/DrMagPie/py-advent-of-code/archive/refs/heads/main.zip`

provides `aoc` function wrapper that gets input executes wrapped function and submits result, unless specified notu submit.
uppon furst execution will request sesion token from cookies. you can get it using dev tools of your browser.

```python
aoc(year: int, day: int, part: int, session_name: str = None, submit: bool = True, reset_session: bool = False) -> any:...
```

```python
from pyaoc import aoc
@aoc(2020, 1, 1)
def Solve(data=None):
  data = set(map(int, data.strip().split('\n')))
  complement = {2020 - number for number in data}
  return prod(complement.intersection(data))

```

function `get_puzzle_input` that returns string version of the input data

```python
get_puzzle_input(year: int, day: int, session_name: str = None, reset_session: bool = False) -> str
```

Then finally it provides `profile` and `timer` function wrapers for performance mesurment 🙂
