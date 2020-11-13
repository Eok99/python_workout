# 4-4<문자열 포맷>
print("a" + "b")
print("a", "b")

# 방법1
print("나는 %d살입니다." % 20)
# %뒤의 값을 넣겠다.
# d는 정수를 의미
print("나는 %s을 좋아해요." % "파이썬")

print("Apple 은 %c로 시작해요." % 20)
# c는 캐릭터로 한글자만 받겠다.? %s
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
# 중괄호
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("빨간","파란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간","파란"))
# 뒤에 숫자의 순서를 중괄호에 넣어서 위치 선택가능

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color ="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format( color ="빨간", age = 20))

#방법 4 (v3.6 이상~)
age = 20 
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
