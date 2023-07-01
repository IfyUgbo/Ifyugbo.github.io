# Question 1: Evaluating and printing the data type of each of the following
import math
pi = math.pi
print(type(5))
print(type(5.0))
print(type(5 > 1))
print(type('5'))
print(type('5' + '2'))
print(type(5 / 2))
print(type(5 % 2))
print(type({5, 2, 1}))
print(type(5==3))
print (pi) # it will print the value of (pi)

#Question 2: Write and Evalute the python experession that answer these questions:
#Question 2a: Number of characters in 'Supercalifragilisticexpialidocious'?
magicword = 'Supercalifragilisticexpialidocious'
print(len(magicword))

#Question 2b: Does the word 'Supercalifragilisticexpialidocious' contains 'ice' as substring?
if 'ice' in magicword:
    print("Yes, it is a substring!")
else:
    print("Not a substring!")

#Question 2c: #To check the longest string in a list of string
string_list = ['Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus', 'Bababadalgharaghtakamminarronnkonn']
print("The longest word is:" + max(string_list, key=len)) #this will print the longest word.

#Question 2d:#Printing the first and the last word in dictionary order:
#Store the composer in a list
myComposerList = ['Berlioz', 'Borodin', 'Brian','Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
myKey = list(range(1, len(myComposerList))) #Generate the key list

#convert it to dictionary to be in key:value format
Composer = dict(zip(myKey,myComposerList))

# Get first composer from dictionary
myComposerList.sort() # To sort the composer
print('First Composer is : ', myComposerList[0])

# Get last composer from dictionary
last_composer = list(Composer.values())[-1]
print('Last Composer is : ', last_composer)


#Question 3: Calculating Area of a Triangle using Heron's Formula
import math
def triangleArea(a, b, c):
    Perimeter = a + b + c
    s = (a + b + c) / 2
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print("Perimeter of the 3 side Triangle = %.2f" %Perimeter);
    print("Semi Perimeter of the 3 side Triangle = %.2f" %s);
    print("The Area of the Triangle is %0.2f" %Area)
triangleArea(2,2,2)


#Question 4: Seperating Odd & Even Intergers in seperate arrays
"""
This function receives input from a user, the user feeds it the amount of number it should receive
and it awaits to receive them, then groups them by even or odd.
This is going to treat 0 as an even number
"""
even = []
odd = []

nums = input("Input the number of elements to be stored in the array : ")

try:
    nums = int(nums)
except:
    print("\n This function takes only integers")

for num in range(nums):
    new = input(f"element - {num}: ")

    try:
        new = int(new)
    except:
        print("Sorry we do not do that here, you can try again and feed only integers")

    if new == 0:
        even.append(new)
    elif new % 2:
        odd.append(new)
    else:
        even.append(new)

    print(f"The Even numbers are: \n{str(even)} \nThe Odd numbers are: \n{str(odd)}")

#Question 5: Write a function inside (x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).
def inside(x1, y1, x2, y2, x, y) :
    if (x > x1 and x < x2 and y > y1 and y < y2) :
        return True
    else :
        return False
     
print("for instance, (1,1,0,0,2,3) : ")

x1 , y1 , x2 , y2 = 0, 0, 2, 3

x, y = 1,1

if inside(x1, y1, x2, y2, x, y) :
    print("True")
else :
    print("False")
 
print("for instance, (-1,-1,0,0,2,3) : ")
x1 , y1, x2 , y2 = 0, 0 , 2, 3 
x , y = -1, -1
print(inside(x1,y1,x2,y2,x,y))

#Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2)." )

print("Is the point (1,1) lies inside the rectangle with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7)? : ")
a1,b1,a2,b2=0.3,0.5,1.1,0.7
a,b=1,1
print(inside(a1,b1,a2,b2,a,b))

print("Is the point (1,1) lies inside the rectangle with lower left corner (0.5, 0.2) and upper right corner (1.1, 2) ? : ")
x1,y1,x2,y2=0.5,0.2,1.1,2
x,y=1,1
print(inside(x1,y1,x2,y2,x,y))

#Question 6:Turning a word into a pig-Latin using the given rules in the Problem set 1
def pig(word):
    #Transforms normal english to pig language, if is consonant it moves the letter to the end and append "ay"
    z = word.lower()
    words = z.split()
    vowels = ("a","e","i","o","u")
    if z[0] in vowels:
        for word in words:
            print(word + "way", end = " ")
    else:
        for word in words:
            print(word[1:] + word[0] + "ay", end = " ")
    print()
    
print("pig('happy') - ")
pig('happy')
print("pig('enter') - ")
pig('enter')


#Question 7: Write a function bldcount() that reads the file with name name and reports (i.e.,prints) how many patients there are in each bloodtype.

def bldcount(txt):
    with open(txt) as f:
        lines = f.read()
    bg = lines.split()
    
    global a,b,ab,o,oo
    a = b=ab=o=oo=0
    for blood in bg:
        if blood == 'A' :
            a = a+1            
        elif blood == 'B':
            b = b+1
        elif blood == 'AB':
            ab = ab+1
        elif blood == 'O':
            o = o+1
        elif blood == 'OO':
            oo = oo+1
    print("There " + ('is ' if (a==1) else 'are ') + ('no' if (a==0) else str(a)) + (' patient' if (b==1) else ' patients') +" patients of blood type A")
    print("There " + ('is ' if (b==1) else 'are ' )+ ('no' if (b==0) else str(b)) + (' patient' if (b==1) else ' patients') +" of blood type B")
    print("There " + ('is ' if (ab==1) else 'are ' )+ ('no' if (ab==0) else str(ab)) + (' patient' if (b==1) else ' patients') +" patients of blood type AB")
    print("There " + ('is ' if (o==1) else 'are ' )+ ('no' if (o==0) else str(o)) + (' patient' if (b==1) else ' patients') +" patients of blood type O")
    print("There " + ('is ' if (oo==1) else 'are ' )+ ('no' if (oo==0) else str(oo)) + (' patient' if (b==1) else ' patients') +" patients of blood type OO")

print("bldcount('bloodtype1.txt'): ")    
bldcount('bloodtype1.txt')

#Question 8:Write a function curconv() that takes as input:
#a: a currency represented using a string (e.g., 'JPY' for the Japanese Yen or'EUR' for the Euro)
#b: an amount and then converts and returns the amount in US dollars
currency = ""
res = int
def curconv(cur,amt):
    if cur == "AUD":
        res = 1.0345157*amt
        currency = "Australian Dollar"
    elif cur == "CHF":
        res =  1.0237414*amt
        currency = "Swiss Franc"
    elif cur == "CNY":
        res =  0.1550176*amt
        currency = "Chinese Yuan"
    elif cur == "DKK":
        res =  0.1651442*amt
        currency = "Danish Krone"
    elif cur == "EUR":
        res =  1.2296544*amt
        currency = "Euro"
    elif cur == "GBP":
        res =  1.5550989*amt
        currency = "British Pound"
    elif cur == "HKD":
        res =  0.1270207*amt
        currency = "Hong Kong Dollar"
    elif cur == "INR":
        res =  0.0177643*amt
        currency = "Indian Rupee"
    elif cur == "JPY":
        res =  0.01241401*amt
        currency = "Japanese Yen"
    elif cur == "MXN":
        res =  0.0751848*amt
        currency = "Mexican Peso"
    elif cur == "MYR":
        res =  0.3145411*amt
        currency = "Malaysian Ringgit"
    elif cur == "NOK":
        res =  0.1677063*amt
        currency = "Norwegian Krone"
    elif cur == "NZD":
        res =  0.8003591*amt
        currency = "New Zealand Dollar"
    elif cur == "PHP":
        res =  0.0233234*amt
        currency = "Philippine Peso"
    elif cur == "SEK":
        res =  0.148269*amt
        currency = "Swedish Krona"
    elif cur == "SGD":
        res =  0.788871*amt
        currency = "Singapore Dollar"
    elif cur == "THB":
        res =  0.0313789*amt
        currency = "Thai Baht"
        
    print (str(res))

print("curconv('EUR' , 100): ")
curconv("EUR" , 100)
print("curconv('JPY' , 100): ")
curconv("JPY" , 100)

#Question 9: Identifying what type of exception (error) each of the following below will cause.
import math

#Adding an incompactible variable
try:
    print(6 + 'a')
except Exception as e:
    print(e)

#Referring to the 12th item of a list that has only 10 items
try:
    list = [20, 70, 75, 51, 8, 44, 10, 3, 39, 64]
    print(list[12])
except Exception as e:
    print(e)

#Using a value that is out of range for a function's input, such as calling math.sqrt(-1.0)
try:
    print(math.sqrt(-1.0))
except Exception as e:
    print(e)

#Using an undeclared variable such as print (x), when x has not been defined
try:
    print(x)
except Exception as e:
    print(e)

#Trying to open a file that doesnt exist, such as mistyping the file name or looking in the wrong directory
try:
    f = open("class.txt")
    f.close()
except Exception as e:
    print(e) 

#Question 10: Write a function called frequencies()
#that takes a string as its only parameter, and returns a list of integers, showing the
#number of times each character appears in the text. 
def frequencies(word):
  alphabets = "abcdefghijklmnopqrstuvwqyz"
  counts = []
  for letter in alphabets:
    count = word.count(letter)
    counts.append(count)
  print(counts)   

print("Input = The quick red fox got bored and went home.")
print("Output:")
frequencies("The quick red fox got bored and went home.")
print("Input = apple")
print("Output:")
frequencies("apple")
