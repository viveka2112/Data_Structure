
# coding: utf-8

# In[ ]:


"-----SELECTION SORT-----"
"Sorting is the process of arranging or ordering a collection of items"
"Python provides a sort() method for sorting a list, it cannot be used with an array or other data structures."
"Selection Sort-scan the minimum value from given items and it placed on first places next scan the minimum value from the"
"remaining item and placed on next to firstone.selection sort Reduces the number of swaps compare with bubble sort.o(n**2)"

def selection_sort(items):
    for i in range(len(items)):
        min_val=i
        for j in range(i+1,len(items)):
            if(items[min_val]>items[j]):
                min_val=j
               # print(min_val)
        items[i],items[min_val]=items[min_val],items[i]
    print(items)
            
        
        
    

selection_sort([99,78,87,82,78,100,45,67,40])
"this method sorting a list ascending order"
"To sort as descending order"
"if(items[min_val]<items[j])"


# In[ ]:


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


# In[ ]:


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


# In[ ]:


"------Linear Search----------"

def linear_search(list1,target):
    success=False
    for i in range(len(list1)):
        if(list1[i]==target):            
            success=True
            print(list1.index(i))
        elif(list1[i]>target):
            return success
    
    

linear_search([2,8,10,12,122,134,154],12)

