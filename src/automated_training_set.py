from sys import path
from sys import exit
path.insert(0, './lib') #set library location
from construct_train_set import construct_train_set

def main():
	n=input("Enter number of documents to construct training set ")
	construct_train_set(n)




if __name__ == "__main__":
	exit(main())