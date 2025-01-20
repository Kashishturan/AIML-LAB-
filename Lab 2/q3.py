my_list =[1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_list[2]=25
print("Modified list : ",my_list)
try:
    my_tuple[2]=14
except TypeError as e:
    print("error: ",e)
print("original tuple : ",my_tuple)
  