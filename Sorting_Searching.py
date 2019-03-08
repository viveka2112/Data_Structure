
# coding: utf-8
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
