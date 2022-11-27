''' the triSelection is a function to sort
    a random unsorted list of 11 elements
    '''
import random
def triSelection(l:list):
    min_value=0
    temp=0
    for i in range(len(l)-1):
        list2=l[i+1:]
        if min(list2)<l[i]:
            temp=l[i]
            l[i]=min(list2) 
            indice=l.index(min(list2),i+1)
            l[indice]=temp
    print("la liste trié est:",l)


l=list(range(0,11))
random.shuffle(l)
print("la liste non-tri est:",l)
triSelection(l)


