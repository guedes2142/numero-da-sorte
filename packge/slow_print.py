import sys
import time

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./20)

if __name__ == "__main__":
  slowprint("This is a test of slowprint")