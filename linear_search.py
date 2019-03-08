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

