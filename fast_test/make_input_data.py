import os 

f = open(os.path.dirname(os.path.abspath(__file__)) + '/input1.txt', 'w')
for i in range(10 ** 6):
    f.write(str(1)+" ")
f.close()

f = open(os.path.dirname(os.path.abspath(__file__)) + '/input2.txt', 'w')
for i in range(10 ** 6):
    f.write(str(1)+"\n")
f.close()

f = open(os.path.dirname(os.path.abspath(__file__)) + '/input3.txt', 'w')
for i in range(10 ** 6):
    f.write(str(1)+" ")
    if (i+1) % 1000 == 0:
        f.write("\n")
f.close()