#Quiz) 
# 댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
# 추첨프로그램
# 조건1 : 편의상 댓글은 20명이 작성, 아이디는 1~20 가정
# 조건2 : 내용상관없이 무작위 추첨 중복불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

# (출력예제)
# 당첨자 발표
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# 축하합니다

from random import*
apply = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(apply)

apply=set(apply)
first=sample(apply,1)
first = set(first)
elsething = apply - first
second = sample(elsething,3)
first =str(first)
second =str(second)

print("--당첨자 발표--")
print("1등 당첨자 :" + first)
print("2등 당첨자 :" + second)

#되게조잡함