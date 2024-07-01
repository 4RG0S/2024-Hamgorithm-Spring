n = int(input())
words = [input() for _ in range(n)]
dictionary = {"a": "A", "b": "B", "k":"C", "d": "D", "e":"E", "g":"F", "h":"G",
           "i":"H", "l":"I","m":"J", "n":"K", "ng": "L", "o":"M", "p":"N", "r":"O",
           "s":"P", "t":"Q", "u":"R", "w":"S","y":"T" }
        
result = {}
for i in words: 
    tmp = i.replace("ng", "L")
    for k, v in dictionary.items() :
        tmp = tmp.replace(k, v)
    result[i] = tmp
result = sorted(result.items(), key= lambda x : x[1])

for i in result :
    print(i[0])