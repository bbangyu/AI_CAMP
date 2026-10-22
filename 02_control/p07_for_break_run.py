print("="*50)
print("Break 문")
print("="*50)

for i in range(1,11):
    if i == 5:
        break

    print(i)

print("="*50)
print("Continue 문")
print("="*50)

for i in range(1,11):
    if i % 2 == 0:
        continue
    
    print(i)
