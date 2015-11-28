'''

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular are there below one million?

'''

import math #to find square root of a number

l=[]
circ=[]
st=''
temp1=[]

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


for inp in range(2,1000001): #stores all prime till range(2,n) in a list l
	if(check_prime(inp)):
		l.append(inp)
		

for inp in l: # iterate each prime of list l to check if it is circular prime
	
	temp=inp
	temp=list(str(temp))
	first_digit=list(temp.pop(0))
	temp=temp+first_digit
	temp1=temp

	for i in temp:
		st=st+str(i)

			
	temp=int(st)
	st=''

	
	while (inp!=temp):	
		if(temp in l):
			if(temp1[0]=='0'):
				break;	
			temp=list(str(temp))	
			first_digit=list(temp.pop(0))
			temp=temp+first_digit
			temp1=temp
			for i in temp:
				st=st+str(i)	
			temp=int(st)
			st=''
			
			
		else:
			break

	if(temp==inp):
		circ.append(inp)			
			

print (circ)		
print(len(circ))

