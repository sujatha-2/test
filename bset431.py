def word count(str):
  counts=dict()
  words=str.split()
for word in words:
   if word in counts:
     counts[word] += 1
 else:
     counts[word] = 1:
     return counts
 print(word count('the quik brown for jump over the lazy dog.'))
