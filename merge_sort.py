"-----MERGING A SORTED LIST-----"
def merge_sort(listA,listB):
    newlist=[]
    a=0
    b=0
    while(a<len(listA) and b<len(listB)):
        if(listA[a]<listB[b]):
            newlist.append(listA[a])
            a+=1
        else:
            newlist.append(listB[b])
            b+=1
    while(a<len(listA)):
        newlist.append(listA[a])
        a+=1
    while(b<len(listB)):
        newlist.append(listB[b])
        b+=1
    print(newlist)
    
    

merge_sort([1,4,7,9,11],[2,4,5,8,12,14])
