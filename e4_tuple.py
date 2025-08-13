#TUPLE
scores=()
print(scores,type(scores))
a=(1)
print(a,type(a))
b=(2,)
print(b,type(b))
c =1,
print(c,type(c))
#PACKING IN TUPLE
students=("Dorcas","dorcas","Bethel","Yusuf")
print(students,type(students),len(students))
students= list(students)
students[0]="Tk"
print(students,type(students[0]))

students= tuple(students)
print(students,type(students))


#UNPACKING IN TUPLE
cars="Lambo","Rolroyce","BMW"
a,b,*c= cars
print(a)
print(b)
print(c)
kingpin,*others=cars
print(kingpin)
print(others)
