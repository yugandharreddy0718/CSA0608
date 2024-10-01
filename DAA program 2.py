num1=[2,3,2]
num2=[1,2]
answer1= len([i for i in num1 if i in num2])
answer2=len([i for i in num2 if i in num1])
result=[answer1,answer2]
print(result)
