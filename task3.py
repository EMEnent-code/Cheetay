def longestPalin(s):
    if list(set(s)) == list(s):
        print('Palindrome No: ', s[0])
    else:
        s = list(s)
        result = []
        for t in range(2):
            if t > 0:
                s.reverse()
            else:
                s = s
            for i in range(len(s)):
                original = s[0:len(s) - i]
                if original == original[::-1]:
                    result.append(original)
                else:
                    continue
        result = max(result)
        result = ''.join(result)
        print('Max Palindrome No :', result)


mystring = 'aaaabba'
longestPalin(mystring)
