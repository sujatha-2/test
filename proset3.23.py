def isCircular(path): 
 x = 0
    y = 0
    dir = N v
    for i in xrange(len(path)): 
     move = path[i] 
   if move == 'R': 
            dir = (dir + 1)%4
        elif move == 'L': 
            dir = (4 + dir - 1)%4
             else:    
            if dir == N: 
                y += 1
            elif dir == E: 
                x += 1
            elif dir == S: 
                y -= 1
            else: 
                x -= 1
  
    return (x == 0 and y == 0) 
