import os
import fnmatch
import pickle
path_list=[]
start_dir="fortune1"




for dirpath,dirs,files in os.walk(start_dir):
    
    for single_file in files:
        
        if fnmatch.fnmatch(single_file,"*txt"):
            x=open(os.path.normpath(os.path.join(dirpath, single_file)))
            path_list.append((os.path.normpath(os.path.join(dirpath, single_file)),x.read()))
            
            
                    
print(path_list)
f=open("raw_data.pickle","bw")
pickle.dump(path_list,f)
f.close()

