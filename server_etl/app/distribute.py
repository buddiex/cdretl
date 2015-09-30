
# coding: utf-8

# In[4]:


# -*- coding: utf-8 -*-
no_file=250
no_thread=20


# create the files -- this will be the array from ls
files=['file_name_'+ str(i)+'.txt' for i in range(no_file)]
# create dir or in this case array that contain the sub dir or array that amount to the number of thread
cdr=[[] for i in range(no_thread)]
# allocate spaces for the number of files to go into each thread based on the number of files coming
for file in files:
    cdr[i].append(file)
    i+=1
    if i==20:
        i=0
        
for i in range(20):
    print len(cdr[i])
    print cdr[i]
    #process_cdr (cdr[i], i)
        
# for i in range(20):
#     print len(cdr[i]),i
#     #process_cdr (cdr[i], i)
    


# In[89]:

"""this program distributes files in such so the the files are in the folders sequecially i.e  folder one contains files 1-10 , folder 2 files 11 to 22 
it will actually be the first 20 files form the number of files coming and folder 2 will contain the next twenty file. this is different from
the other implimentation in the sense that in that incoming files are placed in sequencial folder, i.e file 1 goes to folder 1 and file 2 to folder 2
when it gets to 20 or number of threads it resets to start file 21 in folder 1."""

no_file=250
no_thread=20
# create the files -- this will be the array for listing the directory
files=['file_name_'+ str(i)+'.txt' for i in range(no_file)]
# create dir or in this case array that contain the sub dir or array that amount to the number of thread
cdr=[[] for i in range(no_thread)]
# allocate spaces for the number of files to go into each thread based on the number of files coming
interval=no_file/no_thread
mod_int= no_file%no_thread
for i in range(no_thread):
    for j in range (interval):
        cdr[i].append([])
   
    if i <= mod_int-1:
        cdr[i].append([])
#         print mod_int,i 

n=0
for i in range (no_thread):
#     print 'filse', i, len(cdr[i])
#     print n, n+len(cdr[i])
    cdr[i]=files[n:n+len(cdr[i])]
    n=n+len(cdr[i])
    
for i in range(no_thread):
    print len(cdr[i])
    print cdr[i]
#     process_cdr (cdr[i], i)
    

