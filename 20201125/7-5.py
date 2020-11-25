#가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름은 : {0}\t나이 : {1}\t".format(name,age), end =" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("유재석", 20, "python", "java","C","c++","c#")
# profile("김태호",25,"kotlin","swift","","","")


#사람 많아지면 복잡해지니까 다른 방식 #다변인자.
def profile(name, age, *language):
    print("이름은 : {0}\t나이 : {1}\t".format(name,age), end =" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java","C","c++","c#","java script")
profile("김태호",25,"kotlin","swift")