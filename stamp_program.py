"""
start
get the numbers of sheets 
sheets / 5
round answer to next number
end
"""
import math
# input: sheet
def calculcate(sheet):
    # step 1
    answer = sheet / 5.
    # step 2
    rounded = math.ceil(answer)
    print("sheet is : "),sheet
    print("The answer is : "), answer
    print("rounded is: "), rounded
    print("=========================")
    #output: number of stamps needed
    return rounded
output = calculcate (16)

print ("The number of stamps needed is: "), output
