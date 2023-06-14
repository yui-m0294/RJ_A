with open('data.txt') as f:
    datas = f.readlines()
sum = 0
for i in range(len(datas)):
    try:
        sum += int(datas[i])
    except ValueError:
        continue
print(sum)