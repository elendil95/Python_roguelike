Python data structures
======================

- List == Arraylist
- Tuple == Array
- Set == Unsorted list (?)
- Dict == HashMap

Strings also count as lists in python, so you can access strings by Index as if they were lists or tuples! (eg if x="dog", x[1] will return "o" XD)

**You can 'slice' out substrings from all three (lists, strings, tuples)**  

    Syntax is x[startRange:endRange-1:step] // "step" is the increment  


for example if x="computer":  
    x[1:4] (element 1 through 3, 4)  

    x[1:6:2] (elements 1, 3, 5) //takes every 2nd element within range

    x[3:] (lelments from 3 to the end)

    x[:5] (elements from 0 to 4)

    x[-1] (last element)

    x[-3:] (last 3 elements) //from -3 to the end of the string

    x[:-2] (from the beginning to last two elements)

**You can do math operations on all three**

x = 'dog'+'cat' returns 'dogcat' //for strings  
For lists it appends one list to another  

    x = 'dog'*3 returns 'dogdogdog' // for strings  
    x = [8, 5]*3 returns [8, 5, 8, 5, 8, 5] // for lists. notice that it does not multiply the numbers inside

**You can check wheter something is present in an array/string with "in" & "not in" keywords**

    x='cat'
    print('c' in x) returns True

    y='dog'
    print ('g' not in y) returns False

**You can also iterate through items in sequence**

    list=[1, 2, 3, 4, 5]
    for item in list:
        print(item*2) //returns [2, 4, 6, 8, 10]
you can use the *enumerate()* function to get the value *and* its position in the array:  

    list=["cow", "cat", "bird", "dog", "lion"]
    for index, item in enumerate(list):
        print (index, item)  //returns (0, 'cow') (1, 'cat') (2, 'bird') (3, 'dog') (4, 'lion')

**You can calculate the length of an array/string**

    x="dog"
    print(len(x)) returns '3' //for strings
    
    y=[1, 2, 6, 20]
    print (len(y)) returns "4" //for lists
    
