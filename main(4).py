#+---------------------------------------------------------------+
#+------------------------Python Variables-----------------------+
#+---------------------------------------------------------------+

a = 13 # Int Cuz there is no ""
b = "is unlucky number!?" # Str cuz we have "" and strings
print(a)
print(b)

c = 12 # This one is Int(Integer)
d = "sum word" # This one is Str(String)
print(c)
print(d)

e = str(3) # This thing will change our Int into Str :(
f = int(3) # Just a Int being Int
g = float(3) # Changing it into floating-point number
print(e)
print(f)
print(g)

h = 47
i = "Woopsie!"
j = 12.7
k = "47"
print(type(h)) # We'll get the type of parameter
print(type(i)) # Logically we just asking
print(type(j)) # "type j?"
print(type(k)) # from computer

l = "Quotation" # "" Is the same as ''
m = 'Quotation' # We'll get two Quotation in one line
print(l)
print(m)

n = 99 # Lowercase is seperated var
N = "Simon" # Uppercase is also seperated var
print(n)
print(N)

#+---------------------------------------------------------------+
#+------------------------Variables Names------------------------+
#+---------------------------------------------------------------+

our_var = "It was awkward"
your_var = "Hi, I'm here"
_my_var = "Wanna learn something?"
AnotherVar = "Six kind of"
ONEMOREVAR = "Looks like const. SCARY!!!"
urvar2 = "Yes, It's yours"
# 2myvar = "Is incorrect" Variables cannot start with numbers
# my-var = "Is incorrect" There shouldn't be - symbol
# my var = "Is incorrect af" There shouldn't be 'space' between y, v
print(our_var)
print(your_var)
print(_my_var)
print(AnotherVar)
print(ONEMOREVAR)
print(urvar2)

camelCaseVariable = "It works :D"
PascalCaseVariable = "It works :)"
snake_case_variable = "It also works :]"
print(camelCaseVariable)
print(PascalCaseVariable)
print(snake_case_variable)

#+---------------------------------------------------------------+
#+---------------------Assign Multiple Values--------------------+
#+---------------------------------------------------------------+

o, p, q = "Hexagon", "Cube", "Triangle"
print(o)
print(p)
print(q)

o = p = q = "Cube"
print(o)
print(p)
print(q)

mevalar = ["Ananas", "Kiwi", "Granade"]
r, s, t = mevalar
print(r)
print(s)
print(t)

#+---------------------------------------------------------------+
#+-------------------------Output Variables----------------------+
#+---------------------------------------------------------------+

u = "Something seems off"
print(u) # Just a calling variable

v = "Something"
w = "seems"
x = "off"
print(v, w, x) # We can call multiple variables by calling them one by one
# In here inside of print we are seperating them by using ","

y = "We"
z = "using"
ch = "adding"
sh = "symbol"
print(y + z + ch + sh) # We can call multiple variables by calling them one by one
# But in here inside of print we are seperating them by using ","

a1 = 5
b1 = 10
print(a1 + b1) # In mathematical way + works as a adding operator

c1 = "5"
d1 = "10"
print(c1 + d1) # This works same as str adding to each other

# e1 = 5
# f1 = "String"
# print(e1 + f1) Uhm... Adding str to int is impossible in Python. It won't works

g1 = 5
h1 = "Text"
print(g1, h1) # We can use "," it won't add two vars because "," means "and"
