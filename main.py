set1={1,2,3}
set2={"a","b","c"}
result=list(zip(set1,set2))
print(result)
list1=[1,2,3,4]
list2=[5,6,7,8]
for i,j in zip(list1,list2[::-1]):
    print(i,j)