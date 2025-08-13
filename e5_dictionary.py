#DICTIONARY

contacts={"godiya":"0915422828",
          "dorcas":"0926574857",
          "john":"08035457658",
          "peter":"0708985767",
          "james":"0906454577",
          "charles":"081364667",
          "jessica":"091764576",
          "frey":"0706768456",
          "bjorn":"0905368687",
          "godwin":"091276545",
          "godiya":"09808976565",
          "":"08098678656",
          "indigo":""

          }

print(contacts)
print(len(contacts),type(contacts))
print(contacts["godiya"])
#print(contacts["indigo"])


trail= {True:True,False:False,4:"one",4.8:"one.zro",(1,2):"one comma zero"}
print(trail)
print(trail[True])
print(trail[False])
print(trail[4])
print(trail[4.8])
print(trail[(1,2)])
contacts["godiya"]= "000000000000" #update the value of godiya
contacts.update({"shalom":"0999680088"}) #update helps add more to contacts dic

print(contacts)
contacts.popitem()
print(contacts.keys())
print(contacts.values())
print(contacts)



laptop={"dorcas":[],"dan":[],"ben":[]}
dorcas=input("Enter: ")
laptop["dorcas"].append(dorcas)
dan=input("Enter: ")
laptop["dan"].append(dan)
ben=input("Enter :")
laptop["ben"].append(ben)
print(laptop)

cars={"emma":[],"jacob":[]}
cars["emma"].append("BMW")
cars["jacob"].append("Lambo")
print(cars)


