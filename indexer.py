import pickle
import data_load
def add(self, key, value):
    self[key] = value

def preprocess(data_list):
    s=set()
    dict1={}
    
    for quote in data_list:s=s|set(quote.split())
    
    for word in s:
        s1=set()
        
        for i,quote in enumerate(data_list):
            found_at=quote.find(word)
            if(found_at>=0):
                s1=s1|{i}
        add(dict1,word,s1)
        
    #print(dict1)
    f=open("pickles.txt","bw")
    pickle.dump(dict1,f)
    f.close()
#preprocess(data_load.data_list)

    

