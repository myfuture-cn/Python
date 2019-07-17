# This program says hello and asks for my name.
while True:
    print("Who are you ?")
    name=input()
    if name!="Joe":
       continue
    print("Hello ,Joe .What is the password?(It is a fish.)")
    password =input()
    if password == "1234":
       break
print("The end")