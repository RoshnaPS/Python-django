

def no_of_occurence(tup):
    count=0
    for i in tup:
        if(i==12):
            count=count+1
    return count
tup=(10,12,5,7,12,9,12,3,1)
print(no_of_occurence(tup))