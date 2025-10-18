file1 = open('Codingal.txt',
                        'r')
file2 = open('CodingalUpdated.txt',
                        'w')

for line in file1.readlines():


    if not (line.startswith('Coding')):

        print(line)


        file2.write(line)
file1.close()
file2.close()
file1 = open('codingal1.txt',
                        'r')
file2 = open('codingalupdated1.txt',
                        'w')
cont = file1.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 !=0):
        file2.write(cont[i-1])
    else:
          pass
    

file2.close()



file2.close()
file1.close()
