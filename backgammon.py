import numpy as np
import sys
import matplotlib.pyplot as plt
def master_list(arg, condi):	
  ary = []
  length = len(arg)
  if condi == True:
	  for i in range(0,length,3):
	    ary.append([int(arg[i]),int(arg[i+1])])
	    clean(ary,condi)
  else:
    for i in range(0,length,3):
      ary.append([int(arg[i])])
      ary.append([int(arg[i+1])])
      clean(ary,condi)
  return ary 
	    
def clean(arg,condi):
  if condi == False:
    for i in arg:
      if i==0:
        arg.remove(i)
  elif condi == True:
    for i in arg:
      if i[0]==0 and i[1]==0:
        arg.remove(i)
    return arg
    
def histogram(arg):
  plt.hist(arg, bins = 'auto')
  plt.title("Backgammon")
  plt.savefig('myfig')


if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    content = f.readlines()
  content = [str(x) for x in content]
  histogram(master_list(content[0],False))
  
    
    
  
