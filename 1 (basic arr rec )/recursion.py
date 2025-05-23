def fun(x,n):
    if n==0:
        return
    print(x)
    fun(x,n-1)

fun(15,4)