def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
print(5)



def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) *n

print(fact(2))
print(fact(4))



def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

    fruits =["mango","litchi", "apple", "banana"]
    print_list(fruits)



    #factorial(n) = n * factorial(n-1)
    def factorial(n):
        if(n==0 or  n==1):
            return 1
        else:
            return n * factorial(n-1)
