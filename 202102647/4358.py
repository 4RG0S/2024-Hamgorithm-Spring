import sys
dict1 = dict()
total = 0
while(True):
    
    a = sys.stdin.readline().rstrip()
    if a =='':
        break
    total+=1
    if a in dict1:
        dict1[a] += 1
    else:
        dict1[a] = 1
dic = dict(sorted(dict1.items()))
for i in (dic):
    key = dic[i]
    percent = (key/total*100)
    print("%s %.4f" %(i,percent))