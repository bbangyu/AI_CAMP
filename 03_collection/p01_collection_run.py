print("="*50)
print("컬렉션")
print("="*50)

scores = [80,70,83,82,81]
total = 0


for score in scores:
    print(score)
    total += score

count=len(scores)
print(f'count:{count}')

average = total/len(scores)

print(f'합계: {total}')
print(f'평균: {average}')