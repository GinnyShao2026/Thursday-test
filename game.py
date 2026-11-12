
def check_pass(score):
    if score > 60:
        return "Pass"
    else:
        return "Fail"


score = 60
print(check_pass(score))
