from constants import categories
from math import sqrt
from math import e
from math import pi
import pickle
from collections import OrderedDict
from decimal import *

def g(xk,meanki,sdki):
	
	power=-(xk-meanki)**2
	power=power/(2*(sdki**2))
	
	value=e**power
	value=value/(sqrt(2*pi)*sdki)
	return value

def naive_bayes(freq_list):
	'''
		Find the category corresponding to given frequence list and return category
	'''
	database=pickle.load(open('database.db','rb'))
	pc=OrderedDict()
	for category in categories:
		attributes=OrderedDict()
		documents=[]
		documents=[w for w in database if w['_category']==category]
		for document in documents:
			
			for word in document:
				if word!='_category':
					if word not in attributes:
						attributes[word]=document[word]
					else:
						attributes[word]+=document[word]
		
		number_of_training_documents=len(documents)
		pc[category]=Decimal(2**2000)
		for attribute in attributes:
			meanki=attributes[attribute]/float(number_of_training_documents)
			varrianceki=0
			for document in documents:
				if attribute in document:
					varrianceki+=(meanki-document[attribute])**2
				else:
					varrianceki+=meanki**2
			varrianceki=varrianceki/float(number_of_training_documents)
			sdki=sqrt(varrianceki)
		
			if varrianceki!=0:
				if attribute in freq_list:
					pc[category]=Decimal(pc[category]*Decimal(g(freq_list[attribute],meanki,sdki)))
				else:
					pc[category]=Decimal(pc[category]*Decimal(g(0,meanki,sdki)))
			
	'''for category in categories:
		print("Probability of "+category+" = "+str(pc[category]))
	'''
	
		
	p=0
	Category='Unable to decide'
	for category in categories:
		if p<pc[category]:
			Category=category
			p=pc[category]
	
	return Category			
			
			
				
	
