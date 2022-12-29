# Enter your code here. Read input from STDIN. Print output to STDOUTpy
import cmath as cm
z = complex(input())
print(abs(z), cm.phase(z), sep='\n')
