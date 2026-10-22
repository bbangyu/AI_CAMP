import statistics

scores = [80, 90, 100, 60, 70]

avg = statistics.mean(scores)
median = statistics.median(scores)

print(f'평균:{avg}')
print(f'중앙값:{median}')