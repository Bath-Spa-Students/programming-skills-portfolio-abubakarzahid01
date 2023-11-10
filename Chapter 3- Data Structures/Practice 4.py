#Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that
#copies the values in numbers to numbers2.
numbers1=[]
for i in range (1,100):
    numbers1.append(i)
numbers2=[]
print ("before copying in numbers:",numbers2)
numbers2=numbers1
print ("after copying in numbers2:",numbers2)