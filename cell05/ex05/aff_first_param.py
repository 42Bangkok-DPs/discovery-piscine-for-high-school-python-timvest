import sys

num_param = sys.argv[1:]#starts after said cmd in this case [1:] is from second arg
if num_param:#check if list is empty 
    print(num_param) 
else:
    print("none")