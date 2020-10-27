list1=[2,3,4,6,7]
list2=[4,6,9,0,2]
list3=[]
for i in list1:
    if(i%2!=0):
        list3.append(i)

for i in list2:
    if(i%2==0):
        list3.append(i)
 
print(list3)     
