#기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("이준억", 26, "한국어")
# profile("금진섭", 26, "자바")

# #같은 학교 같은 반 같은 수업일 경우.
# 이때 사용하는게 

def profile(name, age=26, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("이준억")
profile("금진섭")