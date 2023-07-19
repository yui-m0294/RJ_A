my_list = []
for i in range(1,471):
    f = open('labels/45353-640_{:0>1d}.txt'.format(i))
    data = f.read()
    data = data.split( )
    try:
        my_list.append(data[0])
        my_list.append(data[6])
        my_list.append(data[12])
        my_list.append(data[18])
        my_list.append(data[24])
        my_list.append(data[30])
        my_list.append(data[36])
        my_list.append(data[42])
        my_list.append(data[48])
        my_list.append(data[54])
        my_list.append(data[60])
        my_list.append(data[66])
        my_list.append(data[72])
        my_list.append(data[78])
        my_list.append(data[84])
    except IndexError:
        a = 1
#print(list(set(my_list)))
print("person,","train,","traffic light,","bench,","backpack,","handbag,","suitcase,","frisbee,","sports ball,","baseball glove,","cup,","chair")


