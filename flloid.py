rows=int(input("please enter the number of rows"))
num=1
print("floids triangle")
#outer loops for the number of rows
for i in range(1,rows+1):
    #inner loops for nuber of collins
    for j in range(1,i+1):
        #display result
        print(num,end=" ")
        num=num+1
    print()
