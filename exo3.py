slkj = 'a'

# coverting `char` into int
d = ord(slkj)
print(d)

# incrementing
d += 2

# casting the resultat int to char
s = chr(d)
print(s)


separator = '-'*12

""" Print the alphabet using a for loop """
print(separator, 'Exo 1', separator)
first_code = ord('a')
last_code = ord('z')
for i in range(first_code, last_code + 1):
    print(chr(i))
print(separator*2)

print(separator, 'Exo 3', separator)
alphabet_list = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(alphabet_list)
print(separator*2)
