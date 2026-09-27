def is_even(n: int) -> bool:
    """
    Return True if n is even, False otherwise.
    """
    if n % 2 == 0:
      return True
    else:
      return False


def greet_formal(name: str, title: str) -> str:
  return f"Good day, {title} {name}."
    
   


def apply_twice(func, value):
    """
    Call `func` on `value`, then call `func` again on the result
    of that first call. Return the final result.
    Example: apply_twice(lambda x: x + 1, 5) -> 7
    """
    return func(func(value))
