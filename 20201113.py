#탈출문자
print("백문이 불여일견\n백견이 불여일타")
# \n 문장내에서 줄바꿈

#저는 "이준억" 입니다 
print("저는 '이준억'입니다.") #1번 작은 따옴표
print('저는 "이준억"입니다.')
print("저는 \"이준억\"입니다.") #역슬래쉬 넣어줌.
print("저는 \'이준억\'입니다.")

# \\ : 문장 내에서 \로 바뀜.
print("D:\\라이브러리\\Desktop\\github\\python_workout>")

#또다른 탈출문자 \r 커서를 맨앞으로 이동
print("Red Apple\rPine") 

# \b 백스페이스 한글자 삭제
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

##퀴즈 사이트별로 비밀번호를 만들어주는 프로그램
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분을 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                  (nav)              (5)          (1)           (!)
# 예) 생선된 비밀번호 : nav51!

url = "https://www.google.com"
first = url.replace("https://www.","") #규칙1
print(first)
first =  first[:first.index(".")] #규칙2
#first[0:5] -> 0~5 직전까지. (0,1,2,3,4,5)
print(first)
password = first[0:3] + str(len(first)) + str(first.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

