print("="*50)
print(" 8. 최대값 / 최소값 문제")
print("="*50)

scores = [88, 95, 70, 100, 67, 82]

# ① 최고 점수 출력
# max = scores[0]

# for score in scores:
#     if max < score:
#         max = score

# print(f'최고점수:{max}')
print(f'최고점수: {max(scores)}')

# ② 최저 점수 출력
# min = scores[0]

# for score in scores:
#     if min > score:
#         min = score

print(f'최저점수:{min(scores)}')

# ③ 평균 구하기
# total = 0
# for score in scores:
#     total += score
    
# average = total/len(scores)
# print(f'평균: {average:.2f}')
average =sum(scores) / len(scores)
print(f'평균:{average:.2f}')