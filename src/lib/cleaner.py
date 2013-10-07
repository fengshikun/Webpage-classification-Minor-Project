
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

class DataClean:
    def removeFreqone(self,list):
        new_list=[]
        for a in list :
            count = 0
            for b in list:
                if a == b :
                    count=count+1
            if count > 1 :
                new_list.append(a)
        return new_list
    def __init__(self,text):
        lmtzr = WordNetLemmatizer()
        data = text.translate('!@#$)(*&^%$#@!{}][;":/.,?><').lower()
        word_list = lmtzr.lemmatize(data).split(" ")
        filtered_words = [w for w in word_list if not w in stopwords.words('english')]

        #Now removal of terms with frequency =1  [ paper mentions about this ]
        self.filtered_words = self.removeFreqone(filtered_words)

    def GetData(self):
        return self.filtered_words
