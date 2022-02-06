m = input("문자열 입력:")
fw = open("python.txt","w")
fw.write(m)
fw.close()

n = int(input("n 입력:"))
fr = open("python.txt","r")
fr.seek(n)
print(n," bytes 떨어진 위치에 있는 문자 :",
fr.read(1))
fr.close()
