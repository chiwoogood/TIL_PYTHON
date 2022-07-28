n = input()
lst = ['C','A','M','B','R','I','D','G','E']
newlst = []
for i in n:
    if i not in lst:
        newlst.append(i)
newlst = ''.join(newlst)
print(newlst)
