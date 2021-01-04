
import time
def countdown(n):
  if(n==0):
     print("Time has Ended")
  else:
    print(n)
    time.sleep(1) 
    countdown(n-1)



countdown(int(input("Enter the number ")))
