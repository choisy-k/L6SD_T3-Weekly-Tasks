import array

#LINEAR SEARCH (LONG)
def linear_search(list1, find1):
    #start searching from index 0
    i = 0
    #len() counts the items inside an element.
    while i < len(list1):
        #var i decides the index of the number in list1
        #if that specific item is matched with find1, then return i
        if list1[i] == find1:
            #you can also return True...?
            return i
        i += 1
    #you can also return False...?
    return -1

list1 = [6, 7, 4, 3, 3, 2, 0, 8]
find1 = 2

# linear_search(list1, find1)
if linear_search(list1, find1):
    print (f"I found {find1}!")
else:
    print (f"I do not found {find1}.")



#LINEAR SEARCH (SHORTER) got it from Amelie
def linear1(list, n):
    for x in list:
        if x == n:
            print(f"Found {n} with shorter linear search code")
            break
    else:
        print(f"{n} not found.")

list = [5,8,4,6,3,2,9,2]
n = 3
linear1(list, n)



#BINARY SEARCH

array1 = [1,2,3,4,5,6,7,8,9]
find2 = 2

def binary(array1, find2):
    min = 0
    max = len(array1) - 1
    
    for avg in array1:
        avg = min + (max - min) // 2
        if array1[avg] == find2:
            print("I found it with binary search!")
            break
        elif array1[avg] < find2 :
            min = avg + 1
            continue
        else:
            max = avg - 1
            continue
    else:
        print("I cannot find it :(")

binary(array1, find2)
print("Aaaaaaah")
    
    
