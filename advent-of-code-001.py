# __ IMPORTED MODULES : ____________________________________________________
import os
import time
#==============================================================================

# __ GLOBALS : _____________________________________________________________
file_path = 'resources/day1.txt'
#==============================================================================

def read_file():
  file = open(file_path, 'r')
  f = file.readlines()
  file.close()
  return f


def main(): 
  first_column = []
  second_column = []

  f = read_file();

  for line in f:
      splitLine = line.split('   ')
      first_column.append(splitLine[0].strip())
      second_column.append(splitLine[1].strip())
  
  first_column.sort()
  second_column.sort()
  
  print('first 8 elements first column: ', first_column[:8])
  print('first 8 elements second column: ', second_column[:8])
  
  # distance = sum([abs(int(a), int(b)) for a,b in zip(first_column, second_column)])

  first_column = list(map(int, first_column))
  second_column = list(map(int, second_column))
  total_sum = 0
   
  for i in range(len(first_column)):
      currentCount = second_column.count(first_column[i])
      total_sum += first_column[i] * currentCount
      
  #print(distance)
  print(total_sum)


#____CALL_MAIN_PROGRAM_________________
if __name__ == '__main__':            # 
  main()                              #
  quit
#________________________________  
