# __ IMPORTED MODULES : ____________________________________________________
import keyboard
import random
import time
import os
#==============================================================================

# __ GLOBALS : _____________________________________________________________
test_file_path = 'resources/test-file.txt'
file_path = 'resources/data-day-two.txt'
#==============================================================================

def read_file(path):
  file = open(path, 'r')
  f = file.readlines()
  file.close()
  return f


def main():
  f = read_file(test_file_path) 
  print(f)


#____CALL_MAIN_PROGRAM_________________
if __name__ == '__main__':            # 
  main()                              #
  quit
#________________________________  