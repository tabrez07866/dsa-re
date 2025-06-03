input='CM'

def RomanToInt(input):
    roman={
        "I":1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        "D":500,
        "M":1000
    }
    res=0
    n=len(input)
    for i in range(n):
        if i+1<n and roman[input[i]]<roman[input[i+1]]:
            res-=roman[input[i]]
        else:
            res+=roman[input[i]]
    return res

print(RomanToInt(input))            