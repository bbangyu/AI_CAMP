print("="*50)
print("3. 문자열에서 모음 찾기")
print("="*50)

word = "Python Programming" # 모음: aeiou

for ch in word:
    if ch.lower() in "aeiou":
        print(ch)
