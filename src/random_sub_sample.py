from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
import pylab

x=[]
y={}
ym={}


def main():
	data={400: {'sci.med': 89.66666666666667, 'comp.graphics': 84.94444444444444, 'talk.politics.mideast': 98.8888888888889, 'rec.autos': 82.0, 'comp.sys.mac.hardware': 70.72222222222223, 'soc.religion.christian': 98.26912339475153, 'talk.politics.guns': 83.61111111111113, 'rec.sport.hockey': 96.66666666666667, 'sci.electronics': 64.33333333333333, 'talk.religion.misc': 47.333333333333336, 'comp.os.ms-windows.misc': 56.388888888888886, 'alt.atheism': 83.88888888888887, 'sci.crypt': 98.5, 'talk.politics.misc': 77.33333333333333, 'misc.forsale': 63.666666666666664, 'comp.sys.ibm.pc.hardware': 76.83333333333333, 'comp.windows.x': 88.5, 'rec.motorcycles': 79.27777777777777, 'rec.sport.baseball': 88.88888888888887, 'sci.space': 94.0}, 600: {'sci.med': 90.75, 'comp.graphics': 94.25, 'talk.politics.mideast': 98.0, 'rec.autos': 83.08333333333333, 'comp.sys.mac.hardware': 74.41666666666667, 'soc.religion.christian': 99.07640638119229, 'talk.politics.guns': 82.58333333333333, 'rec.sport.hockey': 97.5, 'sci.electronics': 66.33333333333333, 'talk.religion.misc': 60.333333333333336, 'comp.os.ms-windows.misc': 63.833333333333336, 'alt.atheism': 72.33333333333333, 'sci.crypt': 98.25, 'talk.politics.misc': 85.0, 'misc.forsale': 66.41666666666667, 'comp.sys.ibm.pc.hardware': 77.33333333333333, 'comp.windows.x': 85.83333333333333, 'rec.motorcycles': 86.33333333333333, 'rec.sport.baseball': 93.0, 'sci.space': 93.41666666666667}, 700: {'sci.med': 91.66666666666667, 'comp.graphics': 92.66666666666667, 'talk.politics.mideast': 99.33333333333333, 'rec.autos': 83.77777777777779, 'comp.sys.mac.hardware': 79.1111111111111, 'soc.religion.christian': 98.989898989899, 'talk.politics.guns': 82.33333333333333, 'rec.sport.hockey': 98.22222222222223, 'sci.electronics': 71.44444444444444, 'talk.religion.misc': 51.11111111111111, 'comp.os.ms-windows.misc': 60.77777777777777, 'alt.atheism': 80.0, 'sci.crypt': 98.0, 'talk.politics.misc': 83.11111111111113, 'misc.forsale': 63.555555555555564, 'comp.sys.ibm.pc.hardware': 78.22222222222223, 'comp.windows.x': 87.55555555555556, 'rec.motorcycles': 89.0, 'rec.sport.baseball': 91.33333333333333, 'sci.space': 92.66666666666667}, 100: {'sci.med': 68.29629629629629, 'comp.graphics': 59.370370370370374, 'talk.politics.mideast': 92.8888888888889, 'rec.autos': 56.03703703703704, 'comp.sys.mac.hardware': 67.11111111111111, 'soc.religion.christian': 94.42586399108137, 'talk.politics.guns': 55.77777777777777, 'rec.sport.hockey': 88.0, 'sci.electronics': 40.333333333333336, 'talk.religion.misc': 36.333333333333336, 'comp.os.ms-windows.misc': 30.962962962962962, 'alt.atheism': 78.14814814814815, 'sci.crypt': 87.18518518518518, 'talk.politics.misc': 81.48148148148148, 'misc.forsale': 59.96296296296296, 'comp.sys.ibm.pc.hardware': 53.96296296296296, 'comp.windows.x': 64.14814814814815, 'rec.motorcycles': 76.37037037037038, 'rec.sport.baseball': 84.55555555555556, 'sci.space': 76.03703703703702}, 200: {'sci.med': 83.0, 'comp.graphics': 90.70833333333333, 'talk.politics.mideast': 94.20833333333333, 'rec.autos': 68.54166666666667, 'comp.sys.mac.hardware': 51.583333333333336, 'soc.religion.christian': 99.24717691342535, 'talk.politics.guns': 70.75, 'rec.sport.hockey': 92.5, 'sci.electronics': 42.125, 'talk.religion.misc': 51.833333333333336, 'comp.os.ms-windows.misc': 34.625, 'alt.atheism': 66.29166666666667, 'sci.crypt': 98.0, 'talk.politics.misc': 85.125, 'misc.forsale': 55.083333333333336, 'comp.sys.ibm.pc.hardware': 67.20833333333333, 'comp.windows.x': 73.54166666666667, 'rec.motorcycles': 77.625, 'rec.sport.baseball': 87.5, 'sci.space': 88.58333333333333}, 500: {'sci.med': 92.33333333333333, 'comp.graphics': 91.86666666666667, 'talk.politics.mideast': 98.26666666666667, 'rec.autos': 83.33333333333333, 'comp.sys.mac.hardware': 67.2, 'soc.religion.christian': 99.19517102615696, 'talk.politics.guns': 78.46666666666667, 'rec.sport.hockey': 96.2, 'sci.electronics': 70.73333333333333, 'talk.religion.misc': 53.93333333333333, 'comp.os.ms-windows.misc': 61.53333333333333, 'alt.atheism': 76.33333333333334, 'sci.crypt': 96.53333333333335, 'talk.politics.misc': 84.60000000000001, 'misc.forsale': 67.2, 'comp.sys.ibm.pc.hardware': 77.0, 'comp.windows.x': 85.33333333333333, 'rec.motorcycles': 88.26666666666667, 'rec.sport.baseball': 91.66666666666667, 'sci.space': 92.39999999999999}, 900: {'sci.med': 94.33333333333333, 'comp.graphics': 90.0, 'talk.politics.mideast': 98.0, 'rec.autos': 87.66666666666667, 'comp.sys.mac.hardware': 82.33333333333333, 'soc.religion.christian': 100.0, 'talk.politics.guns': 82.66666666666667, 'rec.sport.hockey': 96.66666666666667, 'sci.electronics': 78.33333333333333, 'talk.religion.misc': 49.333333333333336, 'comp.os.ms-windows.misc': 59.333333333333336, 'alt.atheism': 75.66666666666667, 'sci.crypt': 98.0, 'talk.politics.misc': 85.0, 'misc.forsale': 71.0, 'comp.sys.ibm.pc.hardware': 81.66666666666667, 'comp.windows.x': 93.0, 'rec.motorcycles': 92.66666666666667, 'rec.sport.baseball': 92.0, 'sci.space': 95.33333333333333}, 300: {'sci.med': 90.66666666666667, 'comp.graphics': 81.33333333333333, 'talk.politics.mideast': 98.09523809523809, 'rec.autos': 76.90476190476191, 'comp.sys.mac.hardware': 68.76190476190476, 'soc.religion.christian': 98.99569583931134, 'talk.politics.guns': 75.95238095238095, 'rec.sport.hockey': 94.33333333333333, 'sci.electronics': 56.666666666666664, 'talk.religion.misc': 43.52380952380952, 'comp.os.ms-windows.misc': 47.28571428571428, 'alt.atheism': 77.90476190476191, 'sci.crypt': 98.28571428571428, 'talk.politics.misc': 82.33333333333333, 'misc.forsale': 61.47619047619048, 'comp.sys.ibm.pc.hardware': 77.09523809523809, 'comp.windows.x': 84.3809523809524, 'rec.motorcycles': 80.3809523809524, 'rec.sport.baseball': 84.80952380952381, 'sci.space': 88.85714285714285}, 800: {'sci.med': 93.33333333333333, 'comp.graphics': 92.0, 'talk.politics.mideast': 98.66666666666667, 'rec.autos': 85.66666666666667, 'comp.sys.mac.hardware': 80.5, 'soc.religion.christian': 98.8155668358714, 'talk.politics.guns': 79.5, 'rec.sport.hockey': 98.0, 'sci.electronics': 76.16666666666667, 'talk.religion.misc': 52.333333333333336, 'comp.os.ms-windows.misc': 63.833333333333336, 'alt.atheism': 78.16666666666667, 'sci.crypt': 97.16666666666667, 'talk.politics.misc': 87.5, 'misc.forsale': 70.5, 'comp.sys.ibm.pc.hardware': 76.83333333333333, 'comp.windows.x': 92.0, 'rec.motorcycles': 88.5, 'rec.sport.baseball': 91.83333333333333, 'sci.space': 93.83333333333333}}
	datam={400: {'rec.sport.hockey': 93.8888888888889, 'sci.crypt': 92.5, 'talk.religion.misc': 56.55555555555555, 'comp.graphics': 72.61111111111111, 'comp.os.ms-windows.misc': 63.555555555555564, 'comp.sys.ibm.pc.hardware': 59.11111111111111, 'sci.space': 92.3888888888889, 'talk.politics.mideast': 94.05555555555556, 'sci.med': 89.22222222222223, 'rec.motorcycles': 87.72222222222223, 'alt.atheism': 75.33333333333333, 'comp.windows.x': 73.77777777777777, 'misc.forsale': 64.66666666666667, 'rec.sport.baseball': 89.33333333333333, 'rec.autos': 80.6111111111111, 'sci.electronics': 75.94444444444444, 'comp.sys.mac.hardware': 69.77777777777777, 'talk.politics.misc': 72.6111111111111, 'talk.politics.guns': 82.83333333333333, 'soc.religion.christian': 95.53322166387493}, 600: {'rec.sport.hockey': 95.5, 'sci.crypt': 93.5, 'talk.religion.misc': 58.583333333333336, 'comp.graphics': 73.41666666666667, 'comp.os.ms-windows.misc': 71.41666666666667, 'comp.sys.ibm.pc.hardware': 68.58333333333333, 'sci.space': 92.5, 'talk.politics.mideast': 93.08333333333333, 'sci.med': 91.25, 'rec.motorcycles': 91.58333333333333, 'alt.atheism': 72.16666666666667, 'comp.windows.x': 78.91666666666667, 'misc.forsale': 68.91666666666667, 'rec.sport.baseball': 92.0, 'rec.autos': 84.75, 'sci.electronics': 79.33333333333333, 'comp.sys.mac.hardware': 73.75, 'talk.politics.misc': 73.33333333333333, 'talk.politics.guns': 82.83333333333333, 'soc.religion.christian': 96.80940386230058}, 700: {'rec.sport.hockey': 95.77777777777779, 'sci.crypt': 94.0, 'talk.religion.misc': 52.333333333333336, 'comp.graphics': 73.77777777777777, 'comp.os.ms-windows.misc': 71.1111111111111, 'comp.sys.ibm.pc.hardware': 68.66666666666667, 'sci.space': 92.44444444444446, 'talk.politics.mideast': 93.55555555555556, 'sci.med': 93.1111111111111, 'rec.motorcycles': 93.1111111111111, 'alt.atheism': 77.0, 'comp.windows.x': 82.22222222222223, 'misc.forsale': 71.0, 'rec.sport.baseball': 92.33333333333333, 'rec.autos': 86.11111111111113, 'sci.electronics': 79.22222222222221, 'comp.sys.mac.hardware': 74.66666666666667, 'talk.politics.misc': 72.8888888888889, 'talk.politics.guns': 85.33333333333333, 'soc.religion.christian': 96.52076318742985}, 100: {'rec.sport.hockey': 89.70370370370371, 'sci.crypt': 86.03703703703702, 'talk.religion.misc': 51.74074074074074, 'comp.graphics': 54.77777777777777, 'comp.os.ms-windows.misc': 43.59259259259259, 'comp.sys.ibm.pc.hardware': 46.03703703703704, 'sci.space': 83.14814814814814, 'talk.politics.mideast': 87.51851851851852, 'sci.med': 77.4074074074074, 'rec.motorcycles': 82.81481481481482, 'alt.atheism': 72.14814814814815, 'comp.windows.x': 59.40740740740741, 'misc.forsale': 46.18518518518518, 'rec.sport.baseball': 80.37037037037037, 'rec.autos': 65.48148148148148, 'sci.electronics': 57.44444444444445, 'comp.sys.mac.hardware': 52.59259259259259, 'talk.politics.misc': 74.37037037037037, 'talk.politics.guns': 70.8888888888889, 'soc.religion.christian': 91.00706057227796}, 200: {'rec.sport.hockey': 91.16666666666667, 'sci.crypt': 92.79166666666667, 'talk.religion.misc': 54.416666666666664, 'comp.graphics': 69.08333333333333, 'comp.os.ms-windows.misc': 52.916666666666664, 'comp.sys.ibm.pc.hardware': 53.291666666666664, 'sci.space': 87.54166666666667, 'talk.politics.mideast': 89.875, 'sci.med': 86.08333333333333, 'rec.motorcycles': 85.91666666666667, 'alt.atheism': 72.41666666666667, 'comp.windows.x': 68.45833333333333, 'misc.forsale': 52.875, 'rec.sport.baseball': 85.75, 'rec.autos': 75.875, 'sci.electronics': 63.958333333333336, 'comp.sys.mac.hardware': 56.875, 'talk.politics.misc': 76.75, 'talk.politics.guns': 77.375, 'soc.religion.christian': 97.11417816813048}, 500: {'rec.sport.hockey': 94.46666666666665, 'sci.crypt': 92.93333333333334, 'talk.religion.misc': 55.4, 'comp.graphics': 73.66666666666667, 'comp.os.ms-windows.misc': 68.2, 'comp.sys.ibm.pc.hardware': 63.0, 'sci.space': 91.0, 'talk.politics.mideast': 93.8, 'sci.med': 91.2, 'rec.motorcycles': 91.33333333333333, 'alt.atheism': 76.06666666666666, 'comp.windows.x': 74.73333333333333, 'misc.forsale': 68.93333333333332, 'rec.sport.baseball': 90.39999999999999, 'rec.autos': 83.46666666666667, 'sci.electronics': 76.26666666666667, 'comp.sys.mac.hardware': 67.53333333333333, 'talk.politics.misc': 72.73333333333333, 'talk.politics.guns': 82.2, 'soc.religion.christian': 97.38430583501007}, 900: {'rec.sport.hockey': 97.66666666666667, 'sci.crypt': 95.0, 'talk.religion.misc': 52.0, 'comp.graphics': 75.33333333333333, 'comp.os.ms-windows.misc': 70.33333333333333, 'comp.sys.ibm.pc.hardware': 74.0, 'sci.space': 92.66666666666667, 'talk.politics.mideast': 91.33333333333333, 'sci.med': 94.33333333333333, 'rec.motorcycles': 93.66666666666667, 'alt.atheism': 71.33333333333333, 'comp.windows.x': 79.33333333333333, 'misc.forsale': 75.0, 'rec.sport.baseball': 92.66666666666667, 'rec.autos': 85.66666666666667, 'sci.electronics': 86.33333333333333, 'comp.sys.mac.hardware': 78.33333333333333, 'talk.politics.misc': 74.33333333333333, 'talk.politics.guns': 82.33333333333333, 'soc.religion.christian': 96.56357388316151}, 300: {'rec.sport.hockey': 92.71428571428572, 'sci.crypt': 92.42857142857144, 'talk.religion.misc': 55.285714285714285, 'comp.graphics': 67.42857142857143, 'comp.os.ms-windows.misc': 58.904761904761905, 'comp.sys.ibm.pc.hardware': 58.857142857142854, 'sci.space': 88.90476190476191, 'talk.politics.mideast': 93.85714285714285, 'sci.med': 88.76190476190476, 'rec.motorcycles': 88.90476190476191, 'alt.atheism': 75.90476190476191, 'comp.windows.x': 74.33333333333333, 'misc.forsale': 59.57142857142858, 'rec.sport.baseball': 88.80952380952381, 'rec.autos': 80.04761904761905, 'sci.electronics': 72.76190476190476, 'comp.sys.mac.hardware': 66.57142857142857, 'talk.politics.misc': 72.71428571428572, 'talk.politics.guns': 81.90476190476191, 'soc.religion.christian': 96.98708751793401}, 800: {'rec.sport.hockey': 97.0, 'sci.crypt': 93.0, 'talk.religion.misc': 55.0, 'comp.graphics': 74.33333333333333, 'comp.os.ms-windows.misc': 72.83333333333333, 'comp.sys.ibm.pc.hardware': 67.83333333333333, 'sci.space': 93.5, 'talk.politics.mideast': 93.0, 'sci.med': 93.66666666666667, 'rec.motorcycles': 93.0, 'alt.atheism': 76.16666666666667, 'comp.windows.x': 86.66666666666667, 'misc.forsale': 73.83333333333333, 'rec.sport.baseball': 90.66666666666667, 'rec.autos': 87.66666666666667, 'sci.electronics': 80.83333333333333, 'comp.sys.mac.hardware': 75.66666666666667, 'talk.politics.misc': 77.33333333333333, 'talk.politics.guns': 82.66666666666667, 'soc.religion.christian': 96.61590524534687}}


	for category in categories:
		y[category]=[]
		ym[category]=[]
	for n in range(100,1000,100):
		print('n=',n)
		x.append(n)
		for category in categories:
			y[category].append(data[n][category])
			ym[category].append(datam[n][category])
		

	total=[]
	totalm=[]
	for n in range(len(x)):
		total.append(0)
		totalm.append(0)
		for category in categories:
			total[n]+=y[category][n]
			totalm[n]+=ym[category][n]
		total[n]=total[n]/float(len(categories))
		totalm[n]=totalm[n]/float(len(categories))
		print('old',total[n],'modified',totalm[n])
		
		
		
		
		
						
	#Plot graph
	#for item in y:
	#	t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Overal performance",linewidth=4,linestyle='-',color='red')
	t=pylab.plot(x,totalm,label="Imroved performance",linewidth=4,linestyle='-',color='blue')
	t=pylab.xlabel('Number of train documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='lower right')
	t=pylab.title('Number of training documents vs accuracy')
	t=pylab.grid()
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
