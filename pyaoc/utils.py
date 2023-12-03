def format_time(time: int) -> str:
  if time > 1000000000: time = f'{time / 1000000000:.3f} s'
  elif time > 1000000: time = f'{time / 1000000:.3f} ms'
  elif time > 1000: time = f'{time / 1000:.3f} µs'
  else: time = f'{time} ns'
  return time
