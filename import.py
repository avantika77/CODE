#mean arthemitic mean (average) of data
import statistics
A=[5,30,45,65,2,7,6,98,89]
mean=statistics.mean(A)
print("the mean of A is",mean)

#median (middle value) of data
import statistics
B=[34,65,76,89]
median=statistics.median(B)
print("the median of B is",median)

#meadian_low (middle value) of data
#low median of the data is the lower of two middle values when the number of data elements is even, else it is the middle value. 
import statistics
a=[34,67,87,90,30.4]
median_low=statistics.median_low(a)
print("the median_low of a is",median_low)

#median_high(): High median of the data is the larger of two middle values when the number of data elements is even, else it is the middle value. 
import statistics
a=[23.5,67,8,90,0]
high_median=statistics.median_high(a)
print("the median_high is",high_median)

#mode(): Mode (most common value) of discrete data. '
import statistics
e=[34,76.9,9,34,65]
most_common_iteam=statistics.mode(e)
print("the most_common_iteam is",most_common_iteam)

#variance(): Return the sample variance of data, an iterable of at least two real-valued numbers. Variance measures the spread of data. A low variance indicates that all the data is clustered around the mean and a high variance indicates that the data is spread out.
import statistics
s=[23.5,67,87,45]
variance=statistics.variance(s)
print("the variance of s is",variance)

#stdev(): Return the sample standard deviation (the square root of the sample variance). 
import statistics
a=[23,4,56,65,67,70]
std=statistics.stdev(a)
print("the stdev of a is",std)

#MATH MODULES
#sqrt(x): Return the square root of x
import math 
x=81
print("the square root of x is",math.sqrt(x))

#ceil(x): Return the ceiling of x, the smallest integer greater than or equal to x
import math
a=89
print ("the ceilof a is ",math.ceil(a))

#floor(x): Return the floor of x, the largest integer less than or equal to x. 
import math
s=4.9
print("the floor of s is",math.floor(s))

#factorial(x): Return x factorial. 
import math 
v=56
print("the factorial of v is ",math.floor(v))

#exp(x): Return e raised to the power x, where e = 2.718281… is the base of natural logarithms. 
import math
x = 2
print('e ^', x,'=', math.exp(x))

#pow(x,y): Return x raised to the power y 
import math
base = 3; 
x = 9
print(base, '^', x, '=', math.pow(base,x))

#log(x, base): With one argument, return the natural logarithm of x (to base e). With two arguments, return the logarithm of x to the given base. 
import math
base=5
x=34
print("log of ", x ,"to the base of", base,"=",math.log(x,base))

#pi: This is actually a the mathematical constant pi = 3.141592…, to available pr    
import math
print('Pi value:', math.pi)

#degrees(x): Convert angle x from radians to degrees.
import math
print("degree of 9 degree is", math.degrees(math.pi/2))

#radians(x): Convert angle x from degrees to radians. 
import math
print('Radians of 30 degrees:', math.radians(30))