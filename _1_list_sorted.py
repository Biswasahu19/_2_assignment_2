#Fun with Lists and Tuples

lst1 =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print ("List of Tuple before sorting in ascending order", lst1)

lst2 = len(lst1)

for i in range (0, lst2):
    
    for j in range(0, lst2 -i -1):
        if (lst1 [j] [-1] > lst1 [j + 1][-1]):
            temp = lst1[j]
            lst1 [j] = lst1 [j+1]
            lst1 [j+1] = temp

print("New Tuple list after sorting :", lst1)