from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
from accuracy_measure_n import accuracy_measure_n
import pylab

def main():
	x=[]
	y={}
	for category in categories:
		y[category]=[]
	for n in range(10,100,10):
		print('n=',n)
		x.append(n)
		yn=accuracy_measure_n(n)
		print(yn)
		for category in categories:
			y[category].append(yn[category])
	print(y)
	total=[]
	for n in range(len(x)):
		total.append(0)
		for category in categories:
			total[n]+=y[category][n]
		total[n]=total[n]/float(len(categories))
		
	print(y) 
		
		
		
		
						
	#Plot graph
	for item in y:
		t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Overal performance",linewidth=4,linestyle='--')
	t=pylab.xlabel('Number of trainig documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='upper right')
	t=pylab.title('Accuracy vs Number of training documents')
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())