

age = 25

# int convert into string with str method
print("hello man i am " + str(age) +  " old")

# another way short method

print("i am {} years old".format(age))

# multipal value short way

month = 11
print("i am {} years and {} months old".format(age, month))

# another way multipal short way

print("i am {age} years old {month} months old".format(age=age, month=month))

#  this with variable exmple
student_grade =17.0/29
s = "i scored {grade} on the test."
print(s.format(grade = student_grade))


# this with variable trick and tip exmple
student_grade =17.0/29
s = "i scored {grade: .2%} on the test."
print(s.format(grade = student_grade))


m = "19"

print("i am " + m + " old ")

# m is string not int so we can convert into int

print(int(m))

# define a function in python
def helloworld():
        print("this is greate method ")
        print("I love this method")

helloworld()

def getname(name):
    return "Hello, {}, how are you?".format(name)

print(getname("rohan"))


# if method
checkage = 25
if checkage < 30:
    print("you can drink ")
elif checkage == 35:
    print("you can drink to much")

else:
    print("sorry you can't drink")





#  input method use for get user details by default string
p = input("inter your age ")
my_age_count = int(p) * 365 * 24* 60 * 60
print(my_age_count)


