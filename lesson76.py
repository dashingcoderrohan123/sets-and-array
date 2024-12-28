#Write a program to create a set and perform the following operation:1.Create a set with integer elements 2.Create a set with mixed datatype elements 3.Create another set with elements 1,2,3,4,3,2,4 4.Create a set with list of elements 1,2,3,2  5.Print the set after removing the first element from this set 0,1,3,4,5.

int_set={1,2,3,4,5,6}
print(int_set)

mixed_set={1,True,"word",12.5}
print(mixed_set)

third_set={1,2,3,4,3,2,4}
print(third_set)

elements_set= set([1,2,3,2])
print(elements_set)

set_numbers={0,1,3,4,5}
print("The original set is: ",set_numbers)
set_numbers.pop()
print("The duplicate set is: ",set_numbers)


