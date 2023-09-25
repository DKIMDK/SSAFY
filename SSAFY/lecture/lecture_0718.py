decimal = 10

binary = bin(decimal)[2:]
print(binary)

octal = oct(decimal)[2:]
print(octal)

hexa = hex(decimal)[2:]
print(hexa)

a = 3.2 - 3.1
b = 1.2 - 1.1
print(f'{a:.1f},{b:.1f}')

print(314e-2)
print(314*10**-2)

greeting = 'hi'
print(f'{greeting:>10}')
print(f'{greeting:^10}')
print(f'{greeting:<10}')

greeting = 'hello world'

print(greeting[-5])
print(greeting[:5])
print(greeting[6:])
print(greeting[::-1])
print(len(greeting))
for i in greeting:
    print(i,end="")