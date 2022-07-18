alpah = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w','x','y','z',]
n = input()
lst = []
for i in alpah:
    if i != n:
        lst.append(i)
    else:
        lst.append(i)
        break
lst = (' ').join(lst)
print(lst)
