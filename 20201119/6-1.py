#if

# weather = input("오늘날씨는 어때요? ")

# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else: #이런저런 상황이 아닐때.
#     print("오늘은 준비물이 필요 없어요.")



temp = int(input("기온은 어때요?"))
if 30 <= temp :
    print("너무 더워요 건강을 조심하세요")
elif 10<= temp and temp <30:
    print("적당한 날씨예요")
elif 0<= temp and temp <10:
    print("외투를 챙기세요")
else :
    print("너무 춥습니다 나가지 마세요")