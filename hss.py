print ("Enter 'o' for exist.");
ch=input("Enter any character:");
if ch =='o':
  exit();  
else:
   if((ch>='a' and ch<='z') or(ch>='A' and ch<='Z')):
     print ( ch,"is an alphabet.");
  else:
     print(ch,"is not an alphabet.");