#표준 입출력

print("파이썬" , "자바", sep="vs")
#sep사이에 들어 가는 값을 넣을 수 있음.

print("파이썬" , "자바", sep=" , ", end = "?")
# end 마지막에

# # import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)
# # 표준 에러로 처리되는거?? 먼말인지모름.

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.itmes():
#     # print(subject,score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽으로 정렬을 하는데 8칸을 확보하고 정렬.

# 은행 대기 순번표
#001,002,003,004,005, ...
for num in range(1,21):
    print("대기번호 : " +str(num).zfill(3))

answer = input("아무값이나 입력하세요 : ") #input으로 받는것은 str로 된다는것.

print(type(answer))
# print("입력하신 값은 : "+answer + "입니다") #str없이도 잘 출력되는걸 알 수있음