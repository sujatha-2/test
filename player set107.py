def swapBits(x) : 
even_bits = x
odd_bits = x 
even_bits >>= 1
odd_bits <<= 1 
 return (even_bits | odd_bits)  
 x = 23
 print(swapBits(x)) 
