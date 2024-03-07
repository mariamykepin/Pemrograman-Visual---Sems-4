print("\033c")
#To close all
#Part1
#Constructing a Set (there are two methods)
Set_1 = {"Toyota", "Daihatsu", "Honda"}
Set_2 = set(("Toyota", "Daihatsu", "Honda"))
print("Tipe data Set 1 adalah ", type(Set_1))
print("Tipe data Set 2 adalah", type(Set_2))
print("Data Set 1: ", Set_1)
print("Data Set 2: ", Set_2)
print("------")
#Print every item of Set 1
for x in Set_1:
    print(x)
print("----------------------------")
#Check the length of the set print(len(Set_1))
print(len(Set_1))
#Check if a key exist
if "Daihatsu" in Set_1:
    print("Yes, Daihatsu is an item in Set_1.")

#Add an item
Set_1.add("Mitsubishi")
print(Set_1)
#Add multiple itens
Set_1.update(["Suzuki", "Mazda", "Nissan"])
print(Set_1)

#Part2
#Remove an item (method 1)
Set_1.remove("Honda")
print(Set_1)
#Remove an item (method 2)
Set_1.discard("Mazda")
print(Set_1)
#Delete (pop) the last inserted key
Set_1.pop()
print(Set_1)
#Clear the set
Set_1.clear()
print(Set_1)
#Delete the set
del Set_1
print("------------------------------------")
#Union of two sets
Set_1 = {"a", "b" "c"}
Set_2 = {1, 2, 3}
Set_3 = Set_1.union(Set_2)
print(Set_3)
print(" ----")
#Set 1 takes copies of all items of set 2
Set_1 = {"a", "b", "c"}
Set_2 =  {1, 2, 3}
Set_1.update(Set_2)
print(set1)
