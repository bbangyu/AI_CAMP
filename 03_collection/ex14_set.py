print("="*50)
print("4. 학생별 평균과 합격 여부 구하기")
print("="*50)

students = {
	"Kim" :[80,90,85],
	"Lee" :[50,60,55],
	"Park" :[90,95,100]
}
print(students)

for name, scores in students. items():
    # print(name,scores)

    average = sum(scores)/len(scores)
    result = ""

    #평균 60이상 합격
    # print(f'average:{average}')

    if average >= 60:
        result = "합격"
    else:
        result = "불합격"

    print(f'{name}: 평균{average:.1f}점, {result}')