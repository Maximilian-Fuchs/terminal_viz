 while True:
     i += 1
     print("*"*int(A*sin(2*i*pi*f)+60))
     if random.randint(0,100) > 85:
         reverse = not reverse
         if reverse:
             A += 5
         else:
             A -= 5
     sleep(0.1)
