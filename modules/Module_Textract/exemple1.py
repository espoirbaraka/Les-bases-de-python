import textract
x=textract.process("C:\\Users\\ESPOIR\\Downloads\\codePython.txt")
y=x.decode()
print(y)