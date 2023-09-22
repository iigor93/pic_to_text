import os


files = os.listdir('pic/')
file_names = []


for file in files:
    file_names.append(file.split('.')[0] + '\n')
    
with open("file_names/names.txt",'w',encoding = 'utf-8') as f:
   f.writelines(sorted(file_names))
    
