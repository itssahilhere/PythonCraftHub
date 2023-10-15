# # l=[1,2,3]
# # nl=[n+1 for n in l]
# # print(nl)
# # range=(1,5)

# # nr=[n*2 for n in range(1,5)]
# # print(nr)
# l=['sahil','neha','vaishnavi','muskan']
# nl=[n.upper() for n in l if len(n)>5]
# print(nl)

with open("day 26/file.txt") as a:
    f1=a.readlines()
with open("day 26/file1.txt") as b:
    f2=b.readlines()
result=[int(n) for n in f1 if n in f2]    
print(result)
# result=[n for n in ]