name = input()
print("Hello, " + name + "!" + str(5))
print("Hello, ", name + "!" + str(5))

# can only concatenate str (not "int") to str

print(f"Hello, {name}!")

# f string can be int, string, no matter.

print ("Hello, ", end='')
print(name)

print ("Hello, ", end='I am on the same row!')
print(name)

print ("Hello, ", end='')
print(name)
print("text")