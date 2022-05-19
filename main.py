# 1
def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


print(palindrome(808))


# 2
def rec_len(word):
    if word == '': return 0
    return 1 + rec_len(word[1:])


print(rec_len('asdf'))


# 3
def bubble(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


print(bubble([4, 9, 45, 4, 2, 456, 0]))

