import searcher
import data_load
import indexer
from datetime import datetime

print("Please the enter the words that are to be searched")
query=input()
indexer.preprocess(data_load.data_list)


#Search_Engine with dictionary

s=searcher.search_dict(query)
print("**************************************")
print("Execution time for dictionary is ",s[1])
for i in s[0]:
    print("Found_at: ",i,"  ",data_load.data_list[i])

#Search Engine with list
    
s=searcher.search_list(query)
execTime=s[1]
print("**************************************")
print("Execution time for list is ",execTime)
for i in s[0]:
    print("Found_at: ",i,"  ",data_load.data_list[i])

#Search Engine with Dictionary

s=searcher.search_tuple(query)
execTime=s[1]
print("**************************************")
print("Execution time for tuple is ",execTime)
for i in s[0]:
    print("Found_at: ",i,"  ",data_load.data_list[i])



#Output

    #Please the enter the words that are to be searched
    #sheep sheep and flowers or flowers
    #['sheep', 'sheep', 'flowers', 'flowers']
    #**************************************
    #Execution time for dictionary is  15002
    #Found_at:  31    For millions of years flowers have been producing thorns. For millions of years sheep have been eating them all the same. And it's not serious, trying to understand why flowers go to such trouble to produce thorns that are good for nothing? It's not important, the war between the sheep and the flowers? It's no more serious and more important than the numbers that fat red gentleman is adding up? Suppose I happen to know a unique flower, one that exists nowhere in the world except on my planet, one that a little sheep can wipe out in a single bite one morning, just like that, without even realizing what he'd doing - that isn't important? If someone loves a flower of which just one example exists among all the millions and millions of stars, that's enough to make him happy when he looks at the stars. He tells himself 'My flower's up there somewhere...' But if the sheep eats the flower, then for him it's as if, suddenly, all the stars went out. And that isn't important?
    #**************************************
    #Execution time for list is  9997
    #Found_at:  31    For millions of years flowers have been producing thorns. For millions of years sheep have been eating them all the same. And it's not serious, trying to understand why flowers go to such trouble to produce thorns that are good for nothing? It's not important, the war between the sheep and the flowers? It's no more serious and more important than the numbers that fat red gentleman is adding up? Suppose I happen to know a unique flower, one that exists nowhere in the world except on my planet, one that a little sheep can wipe out in a single bite one morning, just like that, without even realizing what he'd doing - that isn't important? If someone loves a flower of which just one example exists among all the millions and millions of stars, that's enough to make him happy when he looks at the stars. He tells himself 'My flower's up there somewhere...' But if the sheep eats the flower, then for him it's as if, suddenly, all the stars went out. And that isn't important?
    #**************************************
    #Execution time for tuple is  10031
    #Found_at:  31    For millions of years flowers have been producing thorns. For millions of years sheep have been eating them all the same. And it's not serious, trying to understand why flowers go to such trouble to produce thorns that are good for nothing? It's not important, the war between the sheep and the flowers? It's no more serious and more important than the numbers that fat red gentleman is adding up? Suppose I happen to know a unique flower, one that exists nowhere in the world except on my planet, one that a little sheep can wipe out in a single bite one morning, just like that, without even realizing what he'd doing - that isn't important? If someone loves a flower of which just one example exists among all the millions and millions of stars, that's enough to make him happy when he looks at the stars. He tells himself 'My flower's up there somewhere...' But if the sheep eats the flower, then for him it's as if, suddenly, all the stars went out. And that isn't important?

#My Observation:
#Lists are taking less time when compared to other data structures.
