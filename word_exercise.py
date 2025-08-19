file_object = open('words.txt')
first_line =file_object.readline()
print(first_line.strip())


second_line = file_object.readline()
print(second_line.strip())


Third_line = file_object.readline()
print(Third_line.strip()) 


forth_line = file_object.readline()
print(forth_line.strip())


line=file_object.readline()
word = line.strip()
print(word)  


line = file_object.readline()
word = line.strip()
print()




for line in open('words.txt'):
    word = line.strip()
    # print(word)


# print(word)


x = 5
x = 7
x = x + 1


print(x)


y = 0
y = y + 1
print(y)



total = 0


for line in open('words.txt'):
    word = line.strip()
    total = total + 1


print(total)


total = 0
count = 0

def has_e(word):
    for letter in word:
        if letter == "E" or letter == "e":
            return True
    else:
        return False
        
print('\n')
print(has_e("Mujaheed"))
print(has_e("ekorede"))
print(has_e("ayman"))


for line in open('words.txt'):
    word = line.strip()
    total = total + 1
    if has_e(word):
        count = count + 1
        m = count / total * 100
print(m)


