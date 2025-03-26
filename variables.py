a = "Kevin"
b = 19
print(a)
print(b)

c = 4
d = "Sally"
print(c)
print(d)

e = str(5)
f = int(5)
g = float(5)
print(e) # e will be string '5'
print(f) # f will be integer 5
print(g) # g will be float 5.0

h = "That's Integer"
i = 37
j = 7.5
print(type(h)) #String
print(type(i)) #Integer
print(type(j)) #Float

k = "Two quote"
# "" same as ''
k = 'One quote'

#################################### Variable Names ####################################

random_var = 1 # Words can be seperated with underscore
randomvar = 2 # No need to seperate
_random_var = 3 # Can be started with underscore
randomVar = 4 # Second word can start with uppercase
RANDOMVAR = 5  # By convention, uppercase means constant, but it can still be changed.
randomvar1 =6 # Can be ended with number

# 1randomvar = 7 Incorrect because variable name cannot be started with number
# random-var = 8 Incorrect because variable name cannot be seperated with Hyphen(Minus)
# random var = 9 Incorrect beacuse variable name cannot be seperated with Space( )

myRandomVariableName = 10 # This is Camel Case variable name
MyRandomVariableName = 11 # This is Pascal Case variable name
my_random_variable_name = 12 # This is Snake Case variable name
print(random_var, randomvar, _random_var, randomVar, RANDOMVAR, randomvar1)

for _ in range(5): # This is actually variable name and we can use it as a Temporary variable
    print("Look it's working") # Developers also calls it Throwaway variable  iwhen they don't need a value

# >>> 5 + 5
# 10
# _ Can hold the last result in shell and retrieves it to terminal
# 10

имя = "Abdulaziz" # Python ALLOWS variable names in other languages for example this is Russian means "Name"
年齢 = 19 # All this called Unicode Varibale names and this one is Japanese means "Age"
print(имя, 年齢) # But sometimes it's best to stick with English vaiable names for good readability

# Python does not have strict rules on creating variable name that allows very long variable names
this_very_very_long_variable_name_which_is_very_annoying_to_type = 13
print(this_very_very_long_variable_name_which_is_very_annoying_to_type)
# But this kind of methods are bad at practice. Best practice is creating short and descriptive variable names


#################################### Assigning Multiple Values ####################################

l, m, n = "First", "Second", "Third" # Python allows assigning values to multiple variables in one line
print(l, m, n) # Printing them

o = p = q = "Orange" # We can assign one value into multiple variable names in one line
print(o)
print(p)
print(q)

s, t = 14, 15 # Swapping values without temporary values (Without Temp Values)
s, t = t, s # It makes swapping cleaner and avoids extra memory usage
print(s, t)

values = (16, 17, 18) # In here values were inside of tuple
u, v, w = values # By doing this we are assigning tuple values into free variable names
print(u, v, w)

a1, *b1, c1 = [19, 20, 21, 22, 23, 24] # Assigning remaining values into a list
print(a1, b1, c1) # Using * (Asterisk) to capturing remain values into a list 

names = ["Abdulaziz", "Sardor", "Jahongir"]
ages = [19, 20, 21]

for name, age in zip(names, ages): # By zip() pairs elements from two lists/tuples
    print(f"{name} is {age} years old") # zip() pairs name with age


#################################### Global Variables ####################################

d1 = "After seven" # We are using variable which is outside of function

def random_function():
    print(d1 + " here comes eight") # As we can see we are calling d1 inside of random_function()
random_function() # This is for call and run the created function



x = "awesome" # Creating global variable named x

def myfunc(): # Creating function named myFunc
  x = "fantastic" # Creating same named variable inside of this function
  print("Python is " + x) # In here we using local variable which is same named as global variable

myfunc() # Calling function

print("Python is " + x) # But in here we are using global variable which has same name as local one



e1 = "Python is " # Creating global variable

def random_function1(): # Creating function with using def
    f1 = "C++ is " # This is local variable which works only inside of function
    print(e1, "very easy") # Using global variable e1
random_function1() # Calling the function 
print(e1 + "very hard") # If we call f1 variable in outside of function, It will cause Name Error



sum1 = 45 # Global variable

def calculate_sum(): # Creating function
    sum2 = 45 # Local variable
    result = sum1 + sum2 # Adding two variables and equaling them into new variable named result
    print(result) # Printing previous created variable to see sum of two variables
calculate_sum() # Calling the function



ball = 10 # Creating global variable named ball

def updating_ball(): # Creating function
    global ball # We want to modify the existing global variable ball inside this function.
    ball = ball + 10 # This is where we are editing global variable inside of function
    print(ball) # Printing edited global variable to see it's value
updating_ball() # Calling function



