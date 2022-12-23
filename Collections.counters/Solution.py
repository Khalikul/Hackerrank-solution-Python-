# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *

n = int(input())
k = list(map(int, input().split()))
l = Counter(k)
sumf = 0 
a = int(input())
for i in range(a):
    size, val = list(map(int, input().split()))
    if size in l:
        if l[size] > 0:
            sumf += val 
        l[size] -= 1 
print(sumf)
