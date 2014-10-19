import pickle
from datetime import datetime
def search_dict(query):
    t1=datetime.now()
    f=open("pickles.txt","br")
    dict1=pickle.load(f)
    f.close()
    x=set()
    cond=0
    s=set()
    x=query.split()
    if ("or" in x) and (cond!=1):
        cond=0
        x.remove("or")
    if("and" in x):
        cond=1
        x.remove("and")
    print(x)
    for w in x:
        if(cond==1) and (w in dict1):
            if(len(s)!=0):
                s=s & set(dict1[w])
            else:
                s=set(dict1[w])
        
        elif(cond==0) and (cond!=1) and (w in dict1):
            s=s|set(dict1[w])
            
    t2=datetime.now()
    execTime=t2.microsecond-t1.microsecond
    return [s,execTime]


def dict_list_conversion(dict1):
    dictList=[]
    for key,value in dict1.items():
        temp=[key,value]
        dictList.append(temp)
    return dictList
def search_list(query):
    t1=datetime.now()
    f=open("pickles.txt","br")
    dict1=pickle.load(f)
    f.close()
    cond=0
    dictList=dict_list_conversion(dict1)
    s=set()
    y=set()
    s=query.split()
    if("or" in query) and (cond!=1):
        cond=0
        s.remove("or")
    if("and" in query):
        cond=1
        s.remove("and")
    for word in s:
        for x in dictList:
            if(cond==1):
                if(word==x[0]):
                    if(len(y)==0):
                        y=x[1]
                    else:
                        y=y&x[1]
            elif(cond==0):
                 if(word==x[0]):
                     y=y|x[1]
    t2=datetime.now()
    execTime=t2.microsecond-t1.microsecond
    return [y,execTime]
     
#SearchEngine with set
def dict_tuple_conversion(dict1):
   # s=set()
    #for key,value in dict1.items():
        #temp=(key,value)
       # s.add(temp)
        s=tuple(dict_list_conversion(dict1))
        return s
def search_tuple(query):
    t1=datetime.now()
    f=open("pickles.txt","br")
    dict1=pickle.load(f)
    f.close()
    cond=2
    dictSet=dict_tuple_conversion(dict1)
   
    s=set()
    y=set()
    s=query.split()
    if("or" in query) and (cond!=1):
        cond=0
        s.remove("or")
    if("and" in query):
        cond=1
        s.remove("and")
    for word in s:
        for x in dictSet:
            if(cond==1):
                if(word==x[0]):
                    if(len(y)==0):
                        y=x[1]
                    else:
                        y=y&x[1]
            elif(cond==0):
                 if(word==x[0]):
                     y=y|x[1]
    t2=datetime.now()
    execTime=t2.microsecond-t1.microsecond
    return [y,execTime]
