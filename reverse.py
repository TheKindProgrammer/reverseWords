def reverseWords(str):
    lst = str.split()
    ans = []
    for word in lst:
        ans.append(word[::-1])

    soln =  ' '.join(ans)
    return soln


print(reverseWords('Hello my name is Zach'))