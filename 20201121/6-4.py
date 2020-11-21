#continue 와 break
absent = [2,5] #결석
no_book = [7] # 책 x
for student in range (1,11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘수업 여기까지. {0}는 교무실로 와라".format(student))
        break
    print("{0}, 책을 읽어봐.".format(student))

