print("="*50)
print("3. 단어 출현 횟수 계산하기")
print("="*50)

words = {
    "Python","Java","Oracle",
    "Python","Oracle","FastAPI"
}
word_count= {}


for word in words:
    #print(word)
    word_count[word] = word_count.get(word,0)+1
   # print(word_count)

print(f'word_count:{word_count},{type(word_count)}')