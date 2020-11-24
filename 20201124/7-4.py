#키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

# profile("이준억", 26, "한국어")
profile(name="이준억",main_lang="파이선",age=26)
profile(main_lang="자바",name="금진섭",age=26)

#함수에서 전달받는 매개값을 키워드로 받으면 순서 뒤섞여도 잘 전달됨
