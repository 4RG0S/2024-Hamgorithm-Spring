def main():
    n = int(input())
    words = [input() for _ in range(n)]
    
    alphabet_value = {}
    first_alphabet = {}
    for i in range(65, 75):
        alphabet_value[chr(i)] = 0
        first_alphabet[chr(i)] = False
    
    for word in words:
        digit = 1
        for i in range(len(word)-1, -1, -1):
            alphabet_value[word[i]] += digit
            digit *= 10
        first_alphabet[word[0]] = True
    
    sorted_alphabet_value = list(alphabet_value.keys())
    sorted_alphabet_value.sort(key=lambda x: alphabet_value[x])
    
    if first_alphabet[sorted_alphabet_value[0]]:
        for i in range(1, 10):
            if first_alphabet[sorted_alphabet_value[i]]:
                continue
            tmp = sorted_alphabet_value.pop(i)
            sorted_alphabet_value = [tmp] + sorted_alphabet_value
            break

    alphabet_to_num = {}
    for i in range(len(sorted_alphabet_value)):
        alphabet_to_num[sorted_alphabet_value[i]] = i
    
    ans = 0
    for word in words:
        for i in range(len(word)):
            idx = len(word)-i-1
            ans += alphabet_to_num[word[i]]*(10**idx)
    print(ans)
    
if __name__ == "__main__":
    main()