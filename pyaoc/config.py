import os
from pathlib import Path

import appdirs

cache_dir = Path(os.getcwd(), '.cache')

if not cache_dir.exists():
  cache_dir = Path(appdirs.user_cache_dir(appname="AdventOfCode"))

config_dir = Path(appdirs.user_config_dir(appname='AdventOfCode'))
