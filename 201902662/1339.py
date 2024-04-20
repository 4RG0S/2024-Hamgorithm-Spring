def main():
    n = int(input())
    words = [input() for _ in range(n)]
    
    alphabet_value = {}
    for word in words:
        for i in range(len(word)):
            alphabet_value[word[i]] = 0
    
    for word in words:
        for i in range(len(word)):
            idx = len(word)-i-1
            alphabet_value[word[i]] += 10**idx
    
    sorted_alphabet_value = list(alphabet_value.keys())
    sorted_alphabet_value.sort(key=lambda x: alphabet_value[x])
    sorted_alphabet_value = ['_']*(10-len(sorted_alphabet_value)) + sorted_alphabet_value
    
    alphabet_to_num = {}
    for i in range(len(sorted_alphabet_value)):
        alphabet_to_num[sorted_alphabet_value[i]] = i
    
    num = 0
    for word in words:
        for i in range(len(word)):
            idx = len(word)-i-1
            num += alphabet_to_num[word[i]]*(10**idx)
    print(num)
    
if __name__ == "__main__":
    main()