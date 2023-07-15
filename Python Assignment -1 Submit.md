```python
# Assignment Part-1
```


```python
Q1. Why do we call Python as a general-purpose and high-level programming language?
Ans: 
- Because it can be used to design and develop a wide variety of applications, across multiple domains. 
- High-level programming language means it's more user-friendly. 
```


```python
Q2. Why is Python called a dynamically typed language?
Ans: 
- It means that variables are checked against types only when the program is executing. 
- We don't need to declare the variable type, the interpreter automatically interprets it.
```


```python
Q3. List some pros and cons of Python programming language?
Ans:
Pros:
- Easy to use
- High library support
- Easy to integrate
- Multi-paradigm approach
Cons:
- Slow speed of execution compared to C,C++
- Absence from mobile computing and browsers
```


```python
Q4. In what all domains can we use Python?
Ans:
- Web frameworks and applications
- Database Access
- Language Development
- Graphic design, image processing applications, Games, and Scientific/ computational Applications
- Prototyping
- Data Science and Machine Learning
- Scripting
- Software Development
```


```python
Q5. What are variable and how can we declare them?
Ans: 
- A variable is a symbolic name that is a reference or pointer to an object. 
- Once an object is assigned to a variable, you can refer to the object by that name.
```


```python
Q6. How can we take an input from the user in Python?
Ans:
- We can take it by using input() function.
```


```python
Q7. What is the default datatype of the value that has been taken as an input using input() function?
Ans:
- String!
```


```python
Q8. What is type casting?
Ans:
- It means changing the datatype of a variable.
- We can only type casting the datatype having higher bit value to lower bit value.
```


```python
Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
Ans:
- Yes!
```


```python
A,B,C = input('Entre three values: ').split(',')
print('Total number of candidate: ',A)
print('Number of males is: ',B)
print('Number of females is: ',C)
print()
```


```python
A =[int(A) for A in input('Enter multiple value:').split(',')]
print('Number of list is: ',A)
```


```python
Q10. What are keywords?
Ans:
- In python keywords are reserved words that can not be used as variable name, function name, or any other identifier.
```


```python
Q11. Can we use keywords as a variable? Support your answer with reason.
Ans:
- Yes, we can but we shoudn't as it will override the properties of keyword.
```


```python
Q12. What is indentation? What's the use of indentaion in Python?
Ans:
- Indentation is whitespace used in python.
- It is used to create block of statement
```


```python
Q13. How can we throw some output in Python?
Ans:
- Using print() function 
```


```python
Q14. What are operators in Python?
Ans:
    - Symbols or keywords used to perform certain operations on values of variable are know as operators
    
    There are different types of operators like:
    - Arithmetic operators
    - Comparison operators 
    - Logical operators 
    - Bitwise operators
    - Assignment operators  
```


```python
Q15. What is difference between / and // operators?
Ans:
    - / is used for float division and // is used for floor (integer) division.
```


```python
Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
Ans:
```


```python
"iNeuron"*4
```


```python
Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
Ans:
```


```python
num = float(input('Enter a number:'))
if num%2 == 0:
    print(f'{num} is even')
    else:
        print(f'{num} is odd')
```


```python
Q18. What are boolean operator?
Ans:
    - True
    - False
    - not
    - and
    - or
    above are the only built-in python boolean operators.
    
```


```python
Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```
Ans:
```


```python
    1 or 0 -> 1
    0 and 0 -> 0
    True and False and True -> False
    1 or 0 or 0 -> 1
```


```python
Q20. What are conditional statements in Python?
Ans:
    - In large projects we have to control the flow of execution of our program and we want to execute some set of statements only if the given condition is satisfied, and a different set of statements when it's not satisfied.
```


```python
Q21. What is use of 'if', 'elif' and 'else' keywords?
Ans:
    - 'if' is the first condition check for the condition.
    - if 'if' is false then 'elif'condition is checked.
    - else is checked when all the upper conditions fails.
```


```python
Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
Ans:
```


```python
age = int(input("Enter your age: "))
if age >= 18:
    print("I can vote")
else:
    print("I can't vote")
```


```python
Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Ans:
```


```python
numbers = [12, 75, 150, 180, 145, 525, 50]
add = 0
for num in numbers:
    if num%2 == 0:
        add = add+num
    else:
        continue
    print(add)
```


```python
Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
Ans:
```


```python
a,b,c = input("Enter 3 numbers seperated by comma: ").split(",")
if int(a) > int(b) and int(a) > int(c):
    print(f"{a} is greatest")
elif int(b)> int(c):
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")

```


```python
Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Ans:
```


```python
numbers = [12, 75, 150, 180, 145, 525, 50]
lst = []
for num in numbers:
    if num > 150:
    if num > 500:
        break
    elif num%5 ==0:
        1st.append(num)
        
print(lst)

```
