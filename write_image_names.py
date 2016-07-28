import os

f = open('\\data\\img_name.txt', 'w')

d=4
for person in range(25):
    for i in range(5):
        f.write('data\\' + str(d) + '\\s' +str(person+1)+'\\'+str(i+1)+'.pgm\n')

f.close()
