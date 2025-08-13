#   class task

cart={}
dre=dan=jibrin=cart
dan.update({"milk":24})
dre.update({"mango":34})
jibrin.update({"bread":56})
#cart.pop("milk")
print(cart)
cart.clear()
print(cart)

password=input("Enter pw: ")
print(password[0:2]+"*"*len(password[2:-2])+password[-2:])
