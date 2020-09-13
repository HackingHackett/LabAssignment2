"""
start
get the numbers of sheets 
sheets / 5
round answer to next number
end
"""
# sheet = 16
# answer = sheet / 5
# rounded = round(answer,1)
# print("sheet is : ", sheet)
# print("The answer is : ", answer)
# print("rounded is: ", rounded)
# # answer = rount(sheet / 5) 


def calculcate(sheet):
    answer = sheet / 5
    rounded = round(answer)
    print("sheet is : "),sheet
    print("The answer is : "), answer
    print("rounded is: "), rounded
    print("=========================")
    return rounded
output = calculcate (16)

print ("the return statment is: "), output
