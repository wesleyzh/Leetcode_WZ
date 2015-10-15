# Complete the function below.


def  getIntegerComplement( n):
    
    bin_n = bin(n)
    new_n = ""
    
    cnt = 0
    for bit in bin_n:
        if cnt >1:
            if bit == "1":
                new_n += "0"
            else:
                new_n += "1"
                
        cnt +=1
            
    result = int(new_n, 2)
    
    return result
    
    
print getIntegerComplement( 50)


'''
getIntegerComplement( n)