"""ME 499 Lecture notes
    Week 2 Lecture 1:

    """



from math import cos

print(cos(1))

def fac(n):
    if n == 1:
        return 1
    else:
        return n* fac(n-1)

print(fac(200))

i = 0
while i < 5:
    print(i)
    i += 1

# Example of While loop
i = 0
while True:
    if i == 5:
        break

    print(i)
    i += 1

# Example of for loop
for i in range(10, 20, 3):
    print(i)

# Example of list
a = [1, 2, 3]
b = ['g', 1]
c = [1, 2,[3, 4]]

print(a[1])

for e in a:
    print (e)

for i in range(len(a)):
    print(a[i])

a = a + [4]

#a.append[5, 6, 7 ,8]
print(a[-1])

print(a[:5])
print(a[:])

a[3:5] = 'b'

print(a)

a = [i for i in range(10)]
print(a)
a = [2*i for i in range(2, 10, 3)]
print(a)

# IF you want to make a copy of a :

b = a[:]

print(hash((1,2,3)))

def palindrome_i(text):
    for i in range(len(text)//2):
        if text[i] != text[-1 - i]:
            return False
    return True

def palindrome_r(text):
    if len(text) < 2:
        return True
    else:
        return text[0] == text[-1] and palindrome_r(text[1:-1])

def palindrome_d(text):
    return text == text[::-1]

#print(palindrome_i('racecar'))
print(palindrome_r('racecarz'))
print(palindrome_d('amanaplanacanalpanama'))
