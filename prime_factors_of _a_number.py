import datetime
def primeFactors (n):
      x=datetime.datetime.now()
      for i in range(2,int(n/2)+1):
            if i>int(n/i) :
                  break
            if isPrime(i) and n%i==0 and isPrime(int(n/i)):
                  print(i,int(n/i))
      y=datetime.datetime.now()
      print('start time : ',x.timestamp())
      print('end time : ',y.timestamp())
def isPrime(n) :
       for i in range (2,n):
              if n%i==0:
                  return False
       return True
