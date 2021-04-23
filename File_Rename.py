#################################
###        Alperen KAYA       ###
###   04/24/2021 - 2:14 AM    ###
#################################

#This script changes the files name throught up folder name be careful!!


import os

#Please copy and paste the location where the files are into '' under this line
top_directory = ''

os.chdir(top_directory) 
general_directory = os.getcwd()
general_directory_1 = os.listdir(general_directory)
general_directory


a=1
for numbara in range(0,len(general_directory_1)):
    a=1
    sub_directory = top_directory + general_directory_1[numbara]
    os.chdir(sub_directory) 
    sub_directory_1 =  os.getcwd()
    sub_list = os.listdir(sub_directory_1)
    for i in sub_list:
        file_extention = i[-3:]  
        os.rename(i,general_directory_1[numbara]+' {}.{}'.format(a,file_extention) )
        if(file_extention == "xml"):
            a = a+1




