def check(numbers):
    if(len(numbers)) == len(set(numbers)):
        return True
    else:
        return False

print(check([1,2,3,4]))
print(check([1,1,2,3,5,5]))