line1 = input()
line2 = input()
count = 0
#print(line1)
#print(line2)
for i, (x,y) in enumerate(zip(line1, line2)):
        if x == y:
            #print('helloworld')
            count = count+1
print(count)