import math
def sample_variance(x):
    sum1=0
    for i in x:
        sum1+=(i-avg)**2
    return sum1/(len(x)-1)

y=[18,10,25,6,2,13,4,29,9,5,11]
x=sorted(y)
print("Sort: ",x)
print()
avg=sum(y)/len(y)
print("average: ",avg)
print()
print("range: ",max(x)-min(x))
print()
p1=int((len(x)+1)*25/100)
print("25th(index): ",x[p1-1])
print()
p3=int((len(x)+1)*75/100)
print("75th(index): ",x[p3-1])
print()
print("Inter-Quartile Range (IQR) ",x[p3-1]-x[p1-1])
print()
print("sample variance: ",sample_variance(x))
print()
print("sample standard deviation: ",math.sqrt(sample_variance(x)))


