def square(n):
    result = 0
    x = n
    y = n 

    shift = 0
    while y > 0:
        if y & 1: 
            result += x << shift
        y >>= 1   
        shift += 1
    return result

print(square(int(input("Enter the number: "))))
