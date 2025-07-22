arr=[10,20,30,40,50]
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1]) #last element
print(arr[-2]) #second last element

#append an element in array
brands=["Coke","Apple","Microsoft","Google"]
print(brands)
num_brands=len(brands)
print(num_brands)
brands.append("Infosys")
print(brands)

#remove an element from array
colors=["red","blue","green","pink","yellow","indigp"]
print(colors)
del colors[4] #delete the color at index four i.e 4(0 based indexing)
print(colors)
colors.remove("blue")
print(colors)
colors.pop(3)
print(colors)

#Modifying elements of array using indexing
fruits=["Apple","Banana","Mango","Grapes","Orange"]
fruits[1]="pineapple" # add pineapple at first index
print(fruits)
fruits[-1]="gauva" #add gauva at last index.It gets replaced by orange
print(fruits)

#concatenating two arrays using + operator
concat=[1,2,3]
concat=concat+[4,5,6]
print(concat)

#Repting an array 
repeat=["a"]
print(repeat)
repeat=repeat*5
print(repeat)

#Slicing an array
fruits=["Apple","Banana","Mango","Grapes","Orange"]
print(fruits[1:4])
print(fruits[:3]) #starting index not mentioned to by default it is 0
print(fruits[-4:]) #orange=-1,grapes=-2,mango=-3,banana=-4.Sice last index is not mentioned go till -1
print(fruits[-3:-1]) #from -3 to -2 since -1 is excluded

#declaring and defining multidimensional array
multd=[[1,2],[3,4],[5,6],[7,8]]
print(multd[0])
print(multd[3])
print(multd[2][1]) #2 indexed ele is [5,6] out of which 5 has 0 index  & 6 has 1 index
print(multd[3][0]) #3 indexed ele is [7,8] out of which 7 has 0 index  & 8 has 1 index





    