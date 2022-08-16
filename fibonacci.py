count = 0
t1 = 0
t2 = 1
n = int(input("Enter the number of terms"))
print("Fibonacci series")
while count < n:
    print(t1)
    count = count + 1
    next_term = t1 + t2
    t1 = t2
    t2 = next_term
    
    