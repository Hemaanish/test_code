input=input('enter a list of numbers'+' ')
i_list=list(map(int,input.split(',')))
output={}
for i in range(1,10):
    count = 0
    for j in i_list:
        if j%i==0:
            count+=1
    output[i]=count
print(output)
