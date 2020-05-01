import zipfile as z
import sys
import threading import Thread
if len(sys.argv)==3:
   zip=sys.argv[1]
   dict=sys.argv[2]
   f=z.ZipFile(zip)
   dick=open(dict)
   for line in dick.readlines():
      psswd=line.strip('\n')
      try:
             psswd=psswd.encode()
             f.extractall(pwd=psswd)
             print(psswd)
             exit(0)
      except Exception as e:
             pass
else:
    print(" Give first argument as  zip file and  second dictionary file")
