#LIST
noise_makers=[]

print(noise_makers,len(noise_makers))

noise_makers.append("Dorcas")
noise_makers.append("Bethel")
print(noise_makers,"the len:", len(noise_makers))
colors=["black","Red","Yellow","Blue","black","white","green"]
#colors.pop() #removes the last item from the list(it uses stack overflow last in first out approach)
colors.append("orange")
colors.insert(1,"purple")  # add an element the specified index 
colors.remove("black") # removes the specified element(if the elelment are 2 it removes the first one)
#colors.remove("violet") # it will throw error coz there is color violet in the list
print(colors,len(colors))





fruits=["Orange","Mango","Apple","Pear"]
print(fruits[0])
print(fruits[-1])
fruits[1]="Grape"  #REASIGNING THE ITEM IN INDEX ONE TO GRAPE

print(fruits)
fruits[0], fruits[-1] = fruits[-1],fruits[0]   # swap orange [0] and pear[-1]
fruits[1],fruits[2]= "Apple","Mango"
print(fruits)
 


yusuf=["yusuf",False,"9"]
print(yusuf)
print(yusuf[2])
yusuf[2]
print(yusuf,type(yusuf[2]))

yusuf[2] = int(yusuf[2]) +5
print(yusuf)


a = [1, 2, 3, [4, 5, [6, 7, [8], 9]]]
print(a[3][2][2][0])
print(yusuf)
yusuf[2]= str(yusuf[2])
print(yusuf[2],type(yusuf[2]))
