import inspect
#import unittest

def in_unit_test():
  current_stack = inspect.stack()
  for stack_frame in current_stack:
    for program_line in stack_frame[4]:    # This element of the stack frame contains 
      if "unittest" in program_line:       # some contextual program lines
        return True
  return False

if __name__ == '__main__' :

    print(f"Is unittest running {in_unit_test()}")
