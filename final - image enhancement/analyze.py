import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('dog_prob.csv')
#print(df.head())
#print(df.columns)

df_dark = df['dark']
df_auto = df['auto']
df_msrcr = df['msrcr']
df_msrcp = df['msrcp']

#print(df_auto)

dark = []
auto = []
msrcp = []
msrcr = []


# if > 0.9 yes
all = 0
positive = 0
for index, row in df_dark.iteritems():
    #print(row)
    #print(type(row))
    dark.append(row)
    all += 1
    if row >= 0.7:
        positive += 1

print("dog:", positive)
print("not dog:", all-positive)
print("acc_dark:", positive/all)

# if > 0.9 yes
all = 0
positive = 0
for index, row in df_auto.iteritems():
    auto.append(row)
    #print(row)
    #print(type(row))
    all += 1
    if row >= 0.7:
        positive += 1

print("dog:", positive)
print("not dog:", all-positive)
print("acc_auto:", positive/all)

# if > 0.9 yes
all = 0
positive = 0
for index, row in df_msrcp.iteritems():
    msrcp.append(row)
    #print(row)
    #print(type(row))
    all += 1
    if row >= 0.7:
        positive += 1

print("dog:", positive)
print("not dog:", all-positive)
print("acc_msrcp:", positive/all)

# if > 0.9 yes
all = 0
positive = 0
for index, row in df_msrcr.iteritems():
    msrcr.append(row)
    #print(row)
    #print(type(row))
    all += 1
    if row >= 0.7:
        positive += 1

print("dog:", positive)
print("not dog:", all-positive)
print("acc_msrcr:", positive/all)

print("length:", len(dark),len(auto), len(msrcp), len(msrcr))


#折线图
x = range(10)

plt.plot(x,dark[555:565],'o-',color = 'r',label="Dark")#s-:方形
plt.plot(x,auto[555:565],'o-',color = 'g',label="AutomatedMSRCR")#o-:圆形
plt.plot(x,msrcr[555:565],'o-',color = 'b',label="MSRCR")#s-:方形
plt.plot(x,msrcp[555:565],'o-',color = 'y',label="MSRCP")#s-:方形
plt.xlabel("# picture")#横坐标名字
plt.ylabel("probability")#纵坐标名字
plt.legend(loc = "best")#图例
plt.grid()
plt.show()


