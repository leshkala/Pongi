test_file = open('c:\\Users\\Alex\\Desktop\\test.txt')
text = test_file.read()
test_file2 = open('c:\\Users\\Alex\\Desktop\\test2.txt', 'w')
test_file2.write(text)
test_file2 = open('c:\\Users\\Alex\\Desktop\\test2.txt')
text = test_file2.read()
print(text)