import os
import re
# Шаблон поиска имен
name = r"\"[A-Z]+\""
alphabet = 'ABCDEFJHIGKLMNOPQRSTUVWXYZ'

# Функция для нахождения алфавитной суммы
def alpha_sum(name: str):
    sum = 0
    for s in name:
        sum+=name.index(s)+1
    return sum


curDir=os.path.abspath(__file__)
curDir=curDir.replace("\\", '/')
curDir = '/'.join(curDir.split('/')[0:-1])
os.chdir(curDir)

f=open('names.txt','r')
a = f.readline()
sortedNames = re.findall(name,a)
sortedNames.sort()
res=[] #здесь будем хранить результаты произведения порядкового номера слова на алфавитную сумму
for i in range(len(sortedNames)):
    sortedNames[i]=sortedNames[i].strip("\"")
    res.append((i+1)*alpha_sum(sortedNames[i]))
print(sum(res))
