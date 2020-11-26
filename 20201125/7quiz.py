# 표준 체중을 구하는 프로그램
# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1: 표준 체중은 별도의 함수내 계싼
#         함수명 : std_weight
#         전달값 : 키(height), 성별(gender)
# 조건 2: 표준체중 소수 둘째자리 까지 표시
# ex 키 175cm 남자의 표준 체중은 67.39kg 입니다


# 내가 처음에 만든거
# def std_weight(height, gender):
#     std_weight = round(height * height * 22 /10000,2)
#     print("키 {0} {1}의 표준 체중은 {2}입니다.".format(height,gender,std_weight))
# std_weight(173,"남자")

# 컨닝 슬쩎한번봄
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
height = 162
gender = "여자"
weight = round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height,gender,weight))