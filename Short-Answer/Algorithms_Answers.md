#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    Explanation:
    a = 0 #O(1)
  
  
  <!-- a = 0 #O(1)
    while (a < n * n * n): #O(n) + O(1)
      a = a + n * n # O(1)
    #O(1) + O(n) + O(1)
    # O(2) + O(n)
    #O(n) -->


b) O(n^2)

<!-- sum = 0 #O(1)
    for i in range(n): #O(n) + #O(1)
      j = 1 #O(1)
      while j < n: #O(n) + #O(1) + #O(1)
        j *= 2  #O(1)
        sum += 1 #O(1)
        #(O(1) + #O(n) + #O(1)) * (#O(n) + #O(1) + #O(1))
        #O(2) + #O(n) * #O(2) + #O(n)
        # O(n) * O(n)
        # O(n^2) -->


c) O(n)

<!-- def bunnyEars(bunnies): #O(n)
      if bunnies == 0: #O(1)
        return 0 #O(1)
      return 2 + bunnyEars(bunnies-1) #O(n)
      #O(n^2) -->

## Exercise II


- Find the middle and drop an egg form there 

- If this egg breaks, it is determined that the bottom half contains floor(f) and we can go ahead and find the middle of the floor and the bottom half of the building 

- We repeat the procedure until we find a floor lower than the current floor (f), at which point the egg does not brak 

- I dht egg breaks at the first half of the building we do the same with the floors on the higher part until we find the floor (f)

Since binary search has a runtime complexity of O(log n), we assume this algorithm would have a runtime complexity of O(log n)