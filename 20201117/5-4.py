# 집합 (set)
# 중복이 안되고 순서가 없음
my_set = {1,2,3,3,3,}
print(my_set)

java = {"금진섭", "이한호", "자바개발자"}
python = set(["금진섭", "이준억"])

# 교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java python 합집합)
print(java | python)
print(java.union(python))

# 차집합 (자바는 할줄 알지만 파이썬은 할줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("자바개발자")
print(python)
print(python - java)
#제거
python.remove("이준억")
print(python-java)