engkor_dict=dict()
while True:
    eng=input("영어 단어: ")
    kor=input("한글 단어: ")
    
    if eng!="" and kor!="":
        engkor_dict[eng]=kor
        continue
    else:
        break
print(engkor_dict)
