#Name:Carlos L
#Class: 6th Hour
#Assignment: HW11

#1. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg


#import random library
import random
#Create a temperature variable, give it a value (random from 1 to 30).
random.randint(1,30)
#Make an if statement to see if temperature variable is above 20
#   - If yes, print it's hot
#   - If no, bring it to next if statement
a=random.randint(1,30)
b=random.randint(1,30)
if a>b:
  print('its hot')
#Make an if statement to see if temperature variable is above 10
#   - If yes, print it's mild
#   - If no, print it's cold
a=random.randint(1,30)
b=random.randint(1,30)
if a>b:
 print('its mild')
elif a < b:
 print('its mild')
#Print "Thank you!" and end the code
print('thank you')