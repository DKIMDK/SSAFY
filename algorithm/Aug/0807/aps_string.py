# s1 = input()
# s2 = input()
# s3 = s1 + s2
# s4 = s1 * 3
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# # def strlen(a):
# #     i = 0
# #     while a[:] != '\0':
# #         i += 1
# #     return i
# #
# # a = ['a', 'b', 'c', '\0']
# # print(strlen(a))
#
# algorithm = list('algorithm')
# print(algorithm)
# for i in range (len(algorithm)//2):
#     algorithm[i], algorithm[len(algorithm) -i -1] = algorithm[len(algorithm) -i -1], algorithm[i]
# print(''.join(algorithm))
# algorithm.reverse()
# print(algorithm)
#
# s1 = 'abc'
# s2 = 'abc'
# s5 = s1[:2] + 'c'
# s3 = 'def'
# s4 = s1
# print(s1 == s2)
# print(s1 == s3)
# print(s1 == s4)
# print(s1 == s5)
# print('---')
# print(s1 is s2)
# print(s1 is s3)
# print(s1 is s4)
# print(s1 is s5)

def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord('0')
    return i

# s = '123'
# a = atoi(s)
# print(a+1)
def itoa(a):
    s = ''
    while a > 0:
        s += chr(ord('0') + a % 10)
        a //= 10
    return s[::-1]

s = 123
a = itoa(s)
print(a + 'b')