print("="*50)
print("3. 학생 점수에 가산점 적용하기")
print("="*50)

scores =  [70,85,95,100,60]

#result = map(lambda x : 100 if x + 5 > 100 else x + 5, scores)


result = list(map(lambda x : min(x+5,100),scores))

print(list(result))
