print ("hello world")
print ("hello world !")
print ('good boy')

score = "A"
print (score)


b = "first"
c = 'day'
a = 823
'''str and num test'''
print (a,b,c)
d = 811
e = a-d
print (e)

names = ["Amy", "Betty", "Cathy" , "Dog" , "Ella", "Frank" , "Gary"]
print (names)
Name = input ("what's your name: ")
Age = int (input ("how old are you: "))
question = input ("you are boy or girl?")
print (Name)
print (Age)
print (question)
if question == "boy" or question == "b":
    print ("please go to room 2")
elif question == "g" and Age == 25:
    print ("please go to the stage and perform")
elif (Age<12 or Age >35) and question == "g":
    print ("sorry,you are out, please leave")
else:
    print ("please go to room 1")
    
msg = '''
-----------personal infor-----------
Name : %s
Age  : %s
Room : %s
----------------end-----------------
''' %(Name, Age, question)
print (msg)


