"""
You are given a list of integers [7, 11, 2, 15] and a target integer 9. Write a function to
find the two numbers in the list that add up to the target. Your function should
return the indices of the two numbers in the list that add up to the target 9.
"""

def find_target_nums(input_list):
    
    for i in input_list:
        for j in input_list:
            if i+j==9:
                return (input_list.index(i),input_list.index(j))
                
                

find_target_nums([7, 11, 2, 15])