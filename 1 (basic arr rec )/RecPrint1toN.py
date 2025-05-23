# def fun(i,n):
#     if i>n:
#         return
#     print(i)
#     fun(i+1,n)
#     print(i)
# fun(1,10)

def fun(n):
    if(n==0):
        return
    print(n)
    fun(n-1)
    print(n)

fun(10)    