CODE2040_API
============

#CODE2040 API Challenge
This repository contains the four programs to complete the CODE2040 API Challenge. Right now, all programs
are in Python. I started the Challenge on Thursday, November 27 of 2014. But, given that it was Thanksgiving, I finished the challenge
on Friday morning. I made some changes to a more readable code in Friday evening (and also documentation).

##Learning Curve
I really liked the challenge. Although I studied the HTTP protocol in my Networking class, it was the first time that
I comunicate with an API. To understand how it works, I followed CodeAcademy quick [tutorial](http://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1) of API to see examples on how the requests and json libraries from Python can be used to communicate with the API. I really feel that I learned a lot just reading the documentation and programming this exercises.

##Stages
The first three stages where very straightforward. The last one, (interval.py) was a bit trikier. Nevertheless,
I manage to get it done using the datetime Python library. 

Although I cannot implement the following in other programming languages such as C++ using the cpp-netlib library due to time constrains (Partial and Final Exams are ahead) is easy to see that it can be programmed very easily:

**Stage 1 reverse a string** - I used a very straightforward implementation a la C++, but there are several ways to do it.

* Using recursion: Solve this using a recursive function is easy.
* Using a stack: Reversing calls for it.
* Using Python slice operator: In Python, one can reverse a string using `reversed_str = string[::-1]` but I decided not to use it because is too Pythonic.
* Use a built-in or a library function: Use of a library that provides a function to reverse a string.

**Stage 2 find the index of given element in an array** - Also easy to code, but in other languages can be implemented with a simple for loop (see the function findNed inside of neddle.py).

**Stage 3 Find all strings that does not contain a given prefix** - In C++ can be done using string methods and a loop. The same holds for other languages.

**Stage 4 Adding a time interval to a date** - More trikier than the others, can use built-in libraries to be efficient. Or, use quotients and remainders (which looks ok to me). In C++: maybe something like [this](http://stackoverflow.com/questions/9527960/how-do-i-construct-an-iso-8601-datetime-in-c).

##Questions?
Any question about the programming exercises? Want to know more about me? Contact me at edwardo.rivera@upr.edu and, happy coding!
    