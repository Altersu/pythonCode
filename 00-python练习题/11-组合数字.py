count = 0
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if i != j and i != m and  j != m:
                count +=1
                print(f'{i}{j}{m}')
print(count)