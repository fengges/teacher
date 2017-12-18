
import re
import jieba.posseg as pseg

class FenCi(object):
    path_stop_word='stop_words.txt'
    path_defind_stop_word=''
    fill=['v','vd','vn','vf ','vx ','vi','vl','vg','n','nr','nr1','nr2','nrj','nrf','ns','nsf','nt','nz','nl','ng']
    stopwords=[]
    def __init__(self):
        self.stopwords = [line.strip() for line in open(self.path_stop_word, 'r').readlines()]

    def filter(self,text):
        p1 = re.compile('\s+')
        new_string = re.sub(p1, ' ', text)
        seg_list = pseg.cut(new_string)
        words=[]
        for  word,flag in seg_list:
            if flag in self.fill and word in self.stopwords:
                words.append(word)
        return words