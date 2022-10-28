"""
built in methods/functions for numbers; int and float, boolean
int, conjugate, float, bool

built in methods/functions for strings; 
capitalize, upper, lower, title, isdigit, str

built in methods/functions for boolean; 

Logical statements -- output of boolean
logical operators; ==, and, or, not, !=, <=, >=, &, |

if, elif, else

if statements:
  code
elif statements:
  code
else:
  code

-- create a software to work with an AI to check if the weather cold or hot
	
BMI Categories:
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater

BMI = weight (lb) ÷  height2 (inches) * 703

-- create a software to calculate Body mass index then print out the condition of the 
patient; bare mind you need to accept weight and height as inputs


"""

temperature = int(input("Get temperature: "))
if temperature < 24:
  print("It's cold")
elif 25 <= temperature < 30:
  print("It's warm")
else:
  print("It's hot")


