# 퀴즈 나은 해답

from random import*
#print(1st)
#shuffle(1st)
# print(1st)
# print(sample(1st,1))

users = range(1,21) #1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))

# print(users)
shuffle(users)
print(users)

winners = sample(users,4)
print(winners)

print("--당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print("축하합니다")