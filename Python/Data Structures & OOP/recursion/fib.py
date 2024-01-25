def fib(n, num=None, list = None):

    if num == None and list == None:
        num = 1
        list = [0]

    if len(list) == n:
        return list[-1]
    else:
        list.append(num)
        return fib(n, list[-1] + list[-2], list)


print(fib(4))


## if len(list) == n: return list. returns list THEN STOPS FUNCTION
## cant do return list[n] cuz len is n but position n is actually position n - 1
## i.e if we want the 6th fib num. we do fib[-1] we get 6th fib num but the 5th position

######
###### DO if num==None and list=None SO WE CAN RESET IT FOR NEXT PRINT(FIB())