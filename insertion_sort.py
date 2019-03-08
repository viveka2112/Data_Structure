"-----INSERTION SORT-----"
def insertion_sort(items):
    for i in range(1,len(items)):
        pos=i
        value=items[i]
        while(pos > 0 and value < items[pos-1]):
            items[pos]=items[pos-1]
            pos-=1
            print(pos)
            
        items[pos]=value
        
    print(items)
    
    

insertion_sort([21,99,88,12,1,2,5,4,4,88])
