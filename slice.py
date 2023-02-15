

a="karnatata"
print(a[0:3]) #print 1st 3 letter
print(a[3:6]) # print 4th, 5th and 6th index
print(a[:2]) # print 1st 2 letter
print(a[-2:]) # print last 2 index letter
print(a[2:]) # print from 3rd letter/2nd index
print(a[:-2]) # print all lelter except last 2
print(len(a))
print(a[0:7:3]) # slice(start:end:step)

b=[10,20,23,24,25,26,27,282,292,30]
print(b)
print(b[0:2])
print(b[-4:])
print(len(b))
print(b[:10])
print(b[7:9])
print(b[0:6:2])


#create one list as a from 1-100,
#then create another list b from a[] value and parten will e 1,3,5....using slice logic
a=[]
b=[]
for i in range(1,100):
    #print(i)
    a.append(i)
print(a)
b=a[0:100:2]
print(b)

