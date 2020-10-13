#!/usr/bin/env python
# coding: utf-8

# In[11]:


from IPython.display import clear_output
import re
import pdb
#clear_output(wait=True)

converting = True

# Loop
while converting:
    
    # ask which way to convert
    first_input = ""
    while first_input != "binary" and first_input != "decimal":
        clear_output()
        first_input = input("Type 'binary' if you want to convert to binary or 'decimal' to convert from binary to decimal: ")
    
    # ask for a number for *decimal to binary*
    if first_input == "binary":
        
        second_input = ""
        while second_input.isnumeric() == False:
            
            clear_output()
            second_input = input("please input an integer number in decimal: ")
        
        number = int(second_input)
        output = ""
        
        if number == 0:
            output = "0"
            
        while number != 0:
            
            if number%2==0:
                number = number/2
                output = "0" + output
            if number%2==1:
                number = (number-1)/2
                output = "1" + output 
                
        print("Your number in binary is: " + output)
        
        
    # ask for a number for *binary to decimal*
    if first_input == "decimal":
        
        second_input = ""
        pattern = r"[2-9]"
        while second_input.isnumeric() == False or re.findall(pattern,second_input) !=[]:
            second_input = input("please input an integer number in binary: ")
        
        output = 0
        for enum,char in enumerate(second_input[::-1]):
            output = output + int(char)*(2)**(enum)
        
        print(output)
        
    # ask if you want to continue converting
    end_input = input("Type in 'Yes' if you want to stop, otherwise hit enter: ")
    if end_input.lower() == "yes" or end_input.lower() == "y" or end_input.lower() == "stop":
        converting = False

