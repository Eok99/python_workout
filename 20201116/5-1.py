#리스트 []

# 지하철 칸별 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30
#3개의 서로다른 변수를 형태를 리스트로 한번에 넣음
subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하") #append는 더하하는 거
print(subway)

#사이에 넣는거. 유재석/조세호 사이에
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway.pop())
subway.pop(0)
print(subway)

#같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능reverse
num_list.reverse()
print(num_list)

# 모두 지우기 clear
num_list.clear()
print(num_list)

#당야한 자료형 함께 사용
mix_list = ["조세호",20, True]
# print(mist_list)
num_list = [5,4,3,2,1]
#리스트 확장 extend
num_list.extend(mix_list) 
print(num_list)

#5-2사전 키번호
cabinet = {3:"유재석",100:"김태호"}#유재석이 3번키를 받았따 밸류 유재석
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) #get은 값이 없으면 none이나옴
# print(cabinet[5]) #대괄호를 했을때는 값이 없으면 오류
print(cabinet.get(5,"사용 가능"))
print("hi")

print(3 in cabinet) #True #키가 캐비넷에 있냐?
print(5 in cabinet) #False

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
#새손님
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, values 쌍으로 출력
print(cabinet.items())