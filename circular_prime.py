'''

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

'''

import math

l=[]
circ=[]
st=''

def check_prime(n):
	n=float(n)
	sqr=math.sqrt(n)
	#print(sqr)
	sqr=int(sqr)
	sqr=sqr+1
	count=0

	for i in range(2,sqr):
		if(n%i==0):
			count+=1
			break;

	if(count==0):
		return 1;
	else:
		return 0


for inp in range(1,101):
	if(check_prime(inp)):
		l.append(inp)
		

for inp in l:
	
	
	temp=inp
	temp=list(str(temp))
	first_digit=list(temp.pop(0))
	temp=temp+first_digit

	for i in temp:
		st=st+str(i)

			
	temp=int(st)
	st=''
	
	while(inp!=temp):
		if(temp in l):
					
			temp=list(str(temp))	
			first_digit=list(temp.pop(0))
			temp=temp+first_digit
			for i in temp:
				st=st+str(i)	
			temp=int(st)
			st=''
			
			
		else:
			break

	if(temp==inp):
		circ.append(inp)			
			

print (circ)		



