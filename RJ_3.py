import shutil
shutil.unpack_archive('sample.zip', '')
input_folder = "./sample"
file_name = "kitamura"

sum = 0
for i in range(1,1000,2):
    f = open('{}/{}_{:0>5d}_kgu.txt'.format(input_folder,file_name,i))
    data = f.read()
    sum += int(data)
print(sum) 