file = open("Hello.txt", "r")
content = file.read()
print(content)
file.close()

with open("Hello.txt", "w") as file :
    file.write("I am practicing python\n")
    file.write("Lets see where it gooes!!")
#print("Content added successfully")


with open("Hello.txt" , "a") as file:
    file.write("I am practicing python\n")
    file.write("Lets see where it gooes!!")
print("Content added successfully")