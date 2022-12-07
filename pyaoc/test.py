#! /usr/bin/env python

def test(input_data: str, expected_result: any) -> any:
  """Wrapper function to test AoC solver function

  Args:
      input_data (str): test input
      expected_result (any): expected result

  Returns:
      function: solver function
  """
  def decorator(function):
    answer = function(input_data)
    assert answer == expected_result, f"\n\n❌ Expected result: {expected_result} ❌\n❌ Produced result: {answer} ❌"
    return function

  return decorator
