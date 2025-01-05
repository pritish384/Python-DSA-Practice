import time
start1 = time.time()
n = 12
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"({i},{j}) ", end="")
end1 = time.time()
print(f"\nTotal Time: {end1-start1}")

n = 15
start2 = time.time()
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"({i},{j}) ", end="")
end2 = time.time()
print(f"\nTotal Time: {end2-start2}")