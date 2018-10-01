fname = input("Enter file name: ")
 num lines = 0
 with open (fname,'r') as f:
   for line in f:
     num lines += 1
 print(" Number of lines:")
 print(num lines)
   
