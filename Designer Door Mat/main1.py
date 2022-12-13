# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
PATTERN = ".|."

#top
for i in range(n):
    if not i % 2 == 0:
        print((PATTERN * i).center(m, "-"))
#middle
else:
    print("WELCOME".center(m,"-"))

#bottom

for i in reversed(range(n)):
    if not i%2==0:
        print((PATTERN*i).center(m,"-"))
