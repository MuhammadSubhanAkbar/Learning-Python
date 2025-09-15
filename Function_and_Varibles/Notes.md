#Intro

Python is not only a programming language; it's also a program, commonly known as an interpreter, that runs on your computer.
You can download it from python.org and use it to run Python scripts.
For example, you can pass a file like hello.py to the interpreter, and it will read the file top-to-bottom and left-to-right, converting it into machine instructions that your computer can execute.

To run your Python program from the terminal (which you can open with Ctrl + `, or Ctrl + Shift + ` for a new terminal), type:
         python your_program_name.py
Note: Avoid spaces in file names. Use underscores instead, e.g., my_program.py.


#Function

A function is like an action or a verb in programming — it performs a task.
Most languages include built-in functions such as:

1.print() – to display output
2.input() – to take user input
3.type()- Returns the type of an object.

You can also define your own functions using the def keyword.


#Arugument

An argument is a value you pass into a function to customize its behavior.
Example:
    print("Hello")  # "Hello" is the argument passed to the print() function
Functions can take one or more arguments, and some can even return values.


#Bug

A bug is an error or mistake in your code that causes it to behave incorrectly or crash.
Computers are very literal — even a missing colon or bracket can create a bug.
Example:
    print("Hello"  # Missing closing parenthesis → SyntaxError


#Varible

A varible is a container for some value in computer or program, it save the value in computer memory. For example
    name = input("What is your name?")

In python and may more languages, varibles are assingned with equal sign, it doesn't mean equality, it mean that the varible what every you call it is assingned to a function from left to right. On left there is a varibles name and on the right it is varibles function. value etc
You can reuse varible value, and change it if you want.
NOTE: While printing a varible don't put varible in qoutes(""), it mean literally print wwhat ever you write it. For examples

    name = input("What is you name?")

    print(name)


#Print 

The offical documentation for the print functoin is :
    print(*objects, sep=' ', end='\n', file=None, flush=False)

In the start there is the name of the function print the the bracket, then there is parameter " *object ", it mean that any number of object can be put in the bracket up to infinity.
Then the next parameter is " sep =' ', sep is short for seperation in English. The defult value of the parameter sep is a space, it means when you add multiple argument to a print function there will be a defult space value between them.
Then next parameter is " end ='/n', the defult of value of this parameter is '/n', this mean new line, it mean after the print function is excuted the cursor will move to the next line in the output in the terminal.
NOTE: You can over ride these parameter if you define these in a print function for example

-- print("Hello," end="")
   print("Subhan)
   --Defult the print funtion will end by ending a line and printing Subhan on the next line, but we over write the parameter to "/n" to nothing the line is not going to end with the funciton. Thus the out put will not on two lines but only on one


#Str

Str is short for String, it is a form of data that represent text, series of text e.g., a paragraph, world, alphbates etc
 
Example: 
-x = "My name is Subhan"
-y = " I am 16 years old"

x and y both are strings


#int

int is a short form for intergers, like in math these are just numbers, all the way from positive infinity to negative infinity. But it doesn't contain any decimal points values like 2.54654 etc

example:
-x =5
-y=6

x and y both are int values


#float

A float is a number with a decimal point, for example 2.654, 5.651, 25.654. It is also called floating point value, you can think of decimal point as the deciaml point 

example:

-x =35.6546
-y=354.5874

both x and y are floating values


#Round

Round is bulid in function in python which is used to return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

It documentation is 

--round(number, ndigits=None)
The name of the function if ofcourse round and its parameter are number there is no object, * like in the print so just number, that there is ndigit, it means how many number of digit you want you round function to round.