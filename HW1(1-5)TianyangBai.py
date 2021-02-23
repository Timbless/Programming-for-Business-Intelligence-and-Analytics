# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:17:22 2021

@author: hulkb
"""

#Question 1

#compute and print both roots of the quadratic equation x^2 -5.86x + 8.5408

#for algorithm, we can use the quadratic formula to solve this question:
#The quadratic formula is a*x^2 +b*x +c = 0
print("")
print("Question 1: ")
import math # we use math package, because we want to use sqrt() function.
def QuadraRoots(a, b, c): 
    #pass three variables, which indicate the coefficients of our formula
    if b ** 2 - 4 * a * c < 0 : # Check the real roots condition
        return -1 # -1 which indicates the equation does not have real roots
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a) #based on quadratic formula
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
        print("The first root is {:.2f}, and the second root is {:.2f}".format(x1, x2))
        #I use :.2f for decimal precision, and print out our solutions
QuadraRoots(1, -5.86, 8.5408) 
#the quadratic equation x^2 -5.86x + 8.5408
#which means we have a = 1, b = -5.86, c = 8.,5408

#Question 1
#Use a for loop to print the decimal representations of 
#1/2, 1/3, ... , 1/10, one on each line

from fractions import Fraction as f # rename fraction as f, just for easy to use

for n in range(2, 11): 
    #since our denominator is from 2 to 10, so our range is from 2 to 11
    a = f(1, n) #declare a variable a
    print('for ' + str(a) + ', the decimal representation is ' + str(float(a)))
    #the reason why I declare a is because I can use built-in function str(), and float()
    #str() is to print out our solution into string type
    #float() is to find our decimal representations.


#Question 2

#Use a for loop to compute the 10th triangular number. The n-th triangular 
#number is defined as 1+2+3+...+n
print("")
print("Question 2: ")
sum = 0 #initialize a variable = 0, named sum
n = 10 # in our question, we need to find 10-th triangular number, so n = 10
# we can change n to any other number we want to find triganular sum number
for i in range(1, n + 1): # the range is from 1 to 10
    sum = sum + i
    for j in range(1, i + 1): #create a nested loop is to get expression for each ellipsis
        if j < i : # when j < i, we can add '+' in the end
            print(str(j) + ' +' , end = ' ') #corret our format
        else: print(str(j), end = ' ')# when j = i, there is no '+'
    print('= ' + str(sum)) # each expression result

def TriangularSum(n):
    total = n * (n + 1) / 2
    print("Use the formala, the answer is " + str(total))

print("Checking our result.")
print("plug 10 into the formula")
TriangularSum(10) #plug 10 into our TriangularSum function


#Question 3
#Use a loop to compute 10! Recall that the factorial n is 1*2*3*...*n.
#The first line of your solution will be n = 10. After that, your solution should
#not use 10 again, though your solution will use n. In other words,
#your code (after the n = 10 line) should work for any value for n.
print("")
print("Question 3: " )
n = 10 #declare a variable that we want to find its factorial
def factorial(n): #define a function
    f = 1 #declare a variable that presents our function start point
    for i in range(1, n + 1): #the range from 1 to n
        f = f * i
        print('{}! = {}'.format(i, f))
        #similar format to Triangular numbers, print out our result 
        
factorial(n)
        

#Question 4
#write code to print the first 10 factorials, in reverse order.
#In other worlds, write code that prints 10!, then prints 9!, then prints 8!
#Its literal output will be: 3628800, 2622880, 40320 ...
print("")
print("Question 4: ")


n = 10 #declare a variable that we want to find its factorial
list_factorial = []  #create a list that stores each factorial
def newfactorial(n): #define a function
    f = 1 #declare a variable that presents our factorial start point
   
    for i in range(1, n + 1): # n = 10, the factorial range from 1 to 10
        f = f * i    
        list_factorial.append(f) #add elements to our list

newfactorial(n)
for j in range(0, n): #use for loop to show our iteration
    print(str(list_factorial[10-j-1]))# show the element from the last to the first

print("")    
print("Question 5: method 1 double loops")

 
n = 10 #declare a variable that we want to find its factorial
def naturallog(n): #define a function
    fac = 1  #declare a variable that presents our factorial start point
    nlog = 1 #create the first value of natural logarithms
    list_natural = []#create a list that stores each factorial
    for i in range(1, n + 1): # n = 10, the factorial range from 1 to 10
        fac = fac * i
        list_natural.append(fac) #add elements to our list
    for j in range(0, n): #use another loop to add each factorial element to our nature logarithms
        nlog = nlog + 1/list_natural[j]# our factorial element should be denominator 
    print(nlog)#print out our result
    
naturallog(10)#we want to find n = 10, so we plug 10 into our function naturallog


print("Question 5: method 2 nested loop")
numlines = 10  #declare a variable that we want to find its factorial
reversef = 1   #declare the initial natural logarithms = 1
list_f = [] #create a list stores factorial number
for i in range(0, numlines): 
    #the range from 0 to numlines, because the list we create is only 10 elements
    #and list index from 0 to numlines - 1
    factorial = 1 #declare a variable that presents our factorial start point
    for j in range(1, numlines + 1):# numlines = 10, the factorial range from 1 to 10
        factorial = factorial * j 
        list_f.append(factorial) # add elements to our list
    reversef = reversef + 1/list_f[i] # add the first elements up to the last elements

print(reversef) # print our result
    





























