#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Time Complexity: O(n) 

because: (10 * 10 * 10) / (10 * 10) = 10 every iteration a gets added with n * n until a is equal or bigger than n * n * n


b) Time Complexity: O(n log n) 

because we have a for loop with O(n) and a nested while loop whichs loops until the var j (which is 1) got multiplied by 2 every iteration until it reaches the value of n or get higher than n

c) Time Complexity: O(n) 


This a recursive function. When we call bunnyEars(5) the function returs bunnyEars(4) then bunnyEars(3) then bunnyEars(2) then bunnyEars(1) then bunyEars(0) and we trigger the base case : if bunnies == 0: return 0

## Exercise II


- Find the middle and drop an egg form there 

- If this egg breaks, it is determined that the bottom half contains floor(f) and we can go ahead and find the middle of the floor and the bottom half of the building 

- We repeat the procedure until we find a floor lower than the current floor (f), at which point the egg does not brak 

- I dht egg breaks at the first half of the building we do the same with the floors on the higher part until we find the floor (f)

Since binary search has a runtime complexity of O(log n), we assume this algorithm would have a runtime complexity of O(log n)