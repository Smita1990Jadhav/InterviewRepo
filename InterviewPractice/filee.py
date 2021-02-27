import os
file= open("myfile.txt", "x")
file=open('test2.txt','a')
file.write("here is new data")

file = open("test2.txt", "r")
print(file.read())


#os.remove("test2.txt")
#file = open("test2.txt", "r")
#print(file.read())


