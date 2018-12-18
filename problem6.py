'''n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!'''

import functools
n = 10
dgsum = lambda x: x%10 if x//10 == 0 else x%10+dgsum(x//10)
print (dgsum(functools.reduce(lambda x,y: x*y, range(1,n+1))))