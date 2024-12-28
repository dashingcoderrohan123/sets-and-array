#Write a program, to create an array with the following elements-[1,3,5,3,7,9,3]. Then find the number of occurrence of number 3 in an array. Also print the reversed array

import array as arr

array_num=arr.array('i',[1,3,5,3,7,9,3])
print("The original array is:   ",array_num)
print("The number of occurrance of 3 is: "+ str(array_num.count(3)))
array_num.reverse()
print(array_num)
