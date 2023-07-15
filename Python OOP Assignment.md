# Python OOP Assignment


```python
Q1. What is the purpose of Python's OOP?

Ans:
    It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. 
    The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.
```


```python
Q2. Where does an inheritance search look for an attribute?

Ans:
    An inheritance search looks for an attribute first in the instance object, then in the class the instance was created from, then in all higher superclasses, progressing from left to right (by default). 
    The search stops at the first place the attribute is found.
```


```python
Q3. How do you distinguish between a class object and an instance object?

Ans:
    The basic concept of OOP is this: Class >> Object >> Instance. 
    The class = the blue print. 
    The Object is an actual thing that is built based on the 'blue print' (like the house). 
    An instance is a virtual copy (but not a real copy) of the object.
```


```python
Q4. What makes the first argument in a class’s method function special?

Ans:
    The calling process is automatic while the receiving process is not (its explicit). 
    This is the reason the first parameter of a function in class must be the object itself. 
    Writing this parameter as self is merely a convention. 
    It is not a keyword and has no special meaning in Python.
```


```python
Q5. What is the purpose of the init method?

Ans:
    The __init__ method lets the class initialize the object's attributes and serves no other purpose. 
    It is only used within classes.
```


```python
Q6. What is the process for creating a class instance?

Ans:
    To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts

```


```python
Q7. What is the process for creating a class?

Ans:
    Classes are created by keyword class. Attributes are the variables that belong to a class. 
    Attributes are always public and can be accessed using the dot (.) operator.
```


```python
Q8. How would you define the superclasses of a class?

Ans:
    The class from which a class inherits is called the parent or superclass. 
    A class which inherits from a superclass is called a subclass, also called heir class or child class. 
    Superclasses are sometimes called ancestors as well. 
    There exists a hierarchical relationship between classes.
```


```python
Q9. What is the relationship between classes and modules?

Ans:
    Classes in python are templates for creating objects. 
    They contain variables and functions which define the class objects. 
    At the same time, modules are python programs that can be imported into another python program.
```


```python
Q10. How do you make instances and classes?

And:
    To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.
```


```python
Q11. Where and how should be class attributes created?

Ans:
    In Python, class attributes are defined directly within the class definition and are shared among all instances of the class. 
    They can be accessed using the class name and through an instance of the class.
```


```python
Q12. Where and how are instance attributes created?

Ans:
    An instance attribute is a Python variable belonging to one, and only one, object. 
    This variable is only accessible in the scope of this object, and it's defined inside the constructor function, __init__(self,..) of the class.
```


```python
Q13. What does the term "self" in a Python class mean?

Ans:
    SELF represents the instance of class. 
    This handy keyword allows you to access variables, attributes, and methods of a defined class in Python. 
    The self parameter doesn't have to be named “self,” as you can call it by any other name.
```


```python
Q14. How does a Python class handle operator overloading?

Ans:
    To perform operator overloading, Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator. 
    For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.

```


```python
Q15. When do you consider allowing operator overloading of your classes?

Ans:
    Consider that we have two objects which are a physical representation of a class (user-defined data type) and we have to add two objects with binary '+' operator it throws an error, because compiler don't know how to add two objects. 
    So we define a method for an operator and that process is called operator overloading.
```


```python
Q16. What is the most popular form of operator overloading?

Ans:
    A very popular and convenient example is the Addition (+) operator. 
    Just think how the '+' operator operates on two numbers and the same operator operates on two strings. 
    It performs “Addition” on numbers whereas it performs “Concatenation” on strings.
```


```python
Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

Ans:
    Both inheritance and polymorphism are fundamental concepts of object oriented programming. 
    These concepts help us to create code that can be extended and easily maintainable.
```


```python
Q18. Describe three applications for exception processing.

Ans:
    IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error. 
    ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero. 
    ImportError: This exception is raised when an import statement fails to find or load a module.
```


```python
Q19. What happens if you don't do something extra to treat an exception?

Ans:
    You need to know how to properly handle exceptions, especially in production environments, because if they are not handled your program won't know what to do and will crash. 
```


```python
Q20. What are your options for recovering from an exception in your script?

Ans:
    A single try statement can have multiple except statements.
    You can also provide a generic except clause, which handles any exception.
    After the except clause(s), you can include an else-clause.
    The else-block is a good place for code that does not need the try: block's protection.
```


```python
Q21. Describe two methods for triggering exceptions in your script.

Ans:
    To avoid such a scenario, there are two methods to handle Python exceptions: Try – This method catches the exceptions raised by the program. 
    Raise – Triggers an exception manually using custom exceptions.
```


```python
Q22. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.

Ans:
    try/except – Catches and recovers from exceptions raised by Python, or by your code. 
    try/finally – Allows to specify termination or cleanup actions, irrespective of exceptions occur or not. 
    raise – You can use it to trigger an exception manually in your code.
```


```python
Q23. What is the purpose of the try statement?

Ans:
    A Try-Except statement is a code block that allows your program to take alternative actions in case an error occurs. 
    Python will first attempt to execute the code in the try statement (code block 1). 
    If no exception occurs, the except statement is skipped and the execution of the try statement is finished.
```


```python
Q24. What are the two most popular try statement variations?

Ans:
    There are two other optional segments to a try block: else and finally. 
    Both of these optional blocks will come after the try and the except.
```


```python
Q25. What is the purpose of the raise statement?

Ans:
    Python raise Keyword is used to raise exceptions or errors. 
    The raise keyword raises an error and stops the control flow of the program. 
    It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack.
```


```python
Q26. What does the assert statement do, and what other statement is it like?

Ans:
    Python's assert statement allows you to write sanity checks in your code. 
    These checks are known as assertions, and you can use them to test if certain assumptions remain true while you're developing your code. 
    If any of your assertions turn false, then you have a bug in your code.
```


```python
Q27. What is the purpose of the with/as argument, and what other statement is it like?

Ans:
    In Python, the with statement replaces a try-catch block with a concise shorthand. 
    More importantly, it ensures closing resources right after processing them. 
    A common example of using the with statement is reading or writing to a file. 
    A function or class that supports the with statement is known as a context manager.
```


```python
Q28. What are *args, **kwargs?

Ans:
    In such cases, we take the help of special symbols pre-defined by Python which are known as *args and **kwargs. 
    The args stands for arguments that are passed to the function whereas kwargs stands for keyword arguments which are passed along with the values into the function.
```


```python
Q29. How can I pass optional or keyword parameters from one function to another?

Ans:
    Users can either pass their values or can pretend the function to use theirs default values which are specified. 
    In this way, the user can call the function by either passing those optional parameters or just passing the required parameters. 
    Without using keyword arguments. By using keyword arguments.
```


```python
Q30. What are Lambda Functions?

Ans:
    Python Lambda Functions are anonymous function means that the function is without a name. 
    As we already know that the def keyword is used to define a normal function in Python. 
    Similarly, the lambda keyword is used to define an anonymous function in Python.
```


```python
Q31. Explain Inheritance in Python with an example?

Ans:
    It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. 
    Inheritance is the capability of one class to derive or inherit the properties from another class.
```


```python
Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?

Ans:
    Not solved
```


```python
Q33. Which methods/functions do we use to determine the type of instance and inheritance?

Ans:
    Python has two built-in functions that work with inheritance: Use isinstance() to check an instance's type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int .
```


```python
Q34.Explain the use of the 'nonlocal' keyword in Python.

Ans:
   The nonlocal is a keyword in python that is used to declare any variable as not local but instead comes from the nearest enclosing scope that is not global.
```


```python
Q35. What is the global keyword?

Ans:
    In Python, the global keyword allows you to change a variable value outside of its current scope. 
    It is used to make changes to a global variable from a local location. 
    The global keyword is only required for altering the variable value and not for publishing or accessing it.
```


```python

```


```python

```
