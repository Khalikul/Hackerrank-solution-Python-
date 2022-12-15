from itertools import combinations as combi
s, k = input().split()
for i in range(1, int(k)+1):
    print("\n".join(list(map("".join,combi(sorted(s), i)))))
