    
    변수 #값을 저장하는 공간
    name = "연탄이" #연탄이를 저장
    
    연산자
    is_ault = age >=3 #True or Fale 정수와 같이 문자형으로 바꿔줘야함
    str= #숫자(정수)를 문자로바꾸기
    int= 문자를 숫자로 바꾸기 #소수점없애기
    #문자에서 +말고도 ,쉼표로도 추가가능 하지만 ,사용시 점프한개입력
    #,의 장점은 str을 사용안하고도 숫자를 출력가능
    같지않다는 != 같다는 ==
    and 그리고 or 아니면

    퀴즈퀴즈
    변수를 이용하여 다음 문장을 출력
    변수명station
    변수값 사당 신도림 인천공항 순서대로 입력
    출력문장 땡떙행 열차가 들어오고잇습니다
    station = "사당"
    print(station + "행 열차가 들어오고 있습니다.")

    수식
    nuber = 2 + 3 * 4 #14
    nuber = nuber + 2 #16
    nuber += 2 #18 위에 식이랑 완전히 똑같음 간단히만든거
    nuber *= 2 #36
    nuber /= 2 #18
    nuber -= 2 #16

    숫자처리함수
    print(abs(값)) 절대값 #소수점 없애기
    print(pow(4,2)) 4의 2승 #16
    print(max(5,12))큰거#5 작은거#12 min 반올림 round

    라이브러리이용
    from 땡땡 import *(모두) #math, random
    math
    print(floor(4.99)) #내림 4
    print(ceil(3.14)) #올림 4
    print(sqrt(16)) #제곱근 4

    랜덤함수
    print(random()) #0.0~ 1.0미만
    print(random()*10) #0.0~ 10.0 미만 
    print(int(random()*10)) #0~10미만
    print(int(random()*10)+1) #0~10이하
    print(randrange(1,45)) #1~45미만
    print(randint(1,45)) #1~45이하
    print(타이틀[1]) #두번째글씨가져오기
    print(타이틀[0:1])0부터 #첫번째 글씨가져오기

    퀴즈퀴즈
    당신은 최근에 코딩 스터디 모임을 새로만들엇다.
    월4회 스터디를 하는데 3번은 온라인으로하고 1번은 오프라인으로한다.
    아래조건에 맞는 오프라인 모임날짜는 정해주는 프로그램을 작성하라

    조건1 랜덤으로 날짜를 뽑아야함
    조건2 월별 날짜는 다름을 감안하여 최소 일수인 28일이내로 정함
    조건3 매월 1-3일은 스터디 준비를 해야 하므로 제외
    출력문 예제
    오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
    #from random import *
    day = randint(4,28)
    print("오프라인 스터디 모임 날짜는 매월", day , "일로 선정 되었습니다")

    문자처리함수
    python = "Python is Amazing"
    print(python.lower()) #소문자로출력 .upper대문자로출력
    print(python[0].isupper()첫번째잇는게대문자가맞니?
    (len(python)) #몇글자인지 알려줘
    print(python.repalce("python","java")) #파이썬글자를 자바로 바꿔줘
    index= python.index("n") 몇번째에잇니 #짜르기 ?
    index= python.index("n", index + 1) 두번째n 은어디에잇니
    print(index)
    print(python.find("n")) 몇번째에잇니 #값이없을경우 -1주고 진행됨 
    print(python.index("n")) 값이없을경우 #오류내고 끝냄
    print(python.count("n")) #몇번등장하니

    슬라이싱
    ID = "940825-1234567"
    print ("성별: " + ID[7]) #0부터시작하므로 7번째로 성별 정보 파악가능 
    print ("연:" + ID[0:2]) #0부터 2직전까지 가져오기
    print ("생년월일:" +ID[:6]) #처음부터 7직전까지

    문자열포맷[합치기].format
#   첫번째방법
    print("나는 %d살입니다" %20) #%d정수만가능
    print("나는 %s를 좋아해요" %"파이썬") #%s문자열
    print("apple 은 %c로 시작해요" %"a") #%c캐릭터(한글자만)
    %s를 쓰면 만능출력가능
    print("나는 %s색과 %s색을 좋아해요" %("빨간색","파란색"))
#   두번째방법
    print("나는 {}살입니다".format(20))
    print("나는 {0}색과 {1}색을 좋아합니다" .format("빨간색","파란색"))
#   세번째방법
    print("나는 {age}살이며, {color}색을 좋아해요" .format(age=20, color=빨강))
#   네번째방법
    age=20
    color="빨강"
    print(f"나는 {age}살이며, {color}색을 좋아해요)

    탈출문자
#   \n : 줄바꿈
#   \ : 큰따옴표앞에 넣으면 큰따옴표 같이 출력가능
#   \\ : 문장내에서 \
#   \r : 커서를 맨앞으로 이동
#   \b : 백스페이스
#   \t : 탭
    print("백문이 불여일견 \n백견이 불여일타")
    print("저는 \"나도코딩\"입니다")
    print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
    print("Red Apple\rPine")
    print("Redd\b Apple")
    print("Red\tApple") 탭효과

    퀴즈퀴즈
#   예)http://naver.com
#   규칙1 : http:// 부분은 제외 ==> naver.com
#   규칙2 : 처음만나는 점(.) 이후 부분은 제외 ==> naver.com
#   규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자내 'e'갯수 + "!"로구성
#   예) 생성된 비밀번호 : nav51!
    url = "http://naver.com"
    my_str = url.replace("http://","") # 규칙1
    print(my_str)
    my_str = my_str[:my_str.index(".")] #규칙2
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "1"
    print("{0}의 비밀번호는 {1} 입니다".format(url, password))
-----------------------------------------------------------------------------------
    리스트[]
    # 지하철 칸별로 10명,20명,30명
    subway1 = 10
    subway2 = 20
    subway3 = 30
    subway = [10,20,30]리스트 손쉽게 만들기
    subway = ["유재석","조세호","박명수"]
    print = (subway.index("조세호")) 조세호는 몇번째칸에잇니 #몇번째
    #하하가 다음정류장에서 다음칸에 탐
    subway.append("하하") #추가하기
    #정형돈을 유재석/조세호 사이에 탐
    subway.insert(1,"정형돈") #사이에끼워넣기
    #한명씩 뒤에서 꺼냄
    print(subway.pop()) #뒤에서부터 삭제
    print(subway)
    #같은 이름의 사람이 몇명있는지..
    subway.append("유재석") #추가
    print(subway)
    print(subway.count("유재석")) #몇명인지 카운터
    #정렬도가능
    num_list=[5,2,4,3,1]
    num_list.sort() #순서대로 정렬
    print(num_list)
    #순서뒤집기가능
    num_list.reverse() #뒤에서부터 정렬
    print(numlist)
    #모두지우기
    num_list.clear() #모두지우기
    #다양한 자료와함께사용
    num_list=[5,2,4,3,1]
    mix_list=["조세호".20,True]
    print(mix_list)
    #리스트 확장
    num_list.extend(mix_list) #두개합치기
    
    사전 {}
    #방법1
    cabinet = {3:"유재석",100:"김태호"}
    print(cabinet[3]) == "유재석" #값가져오기1
    print(cabinet.get(3)) #값가져오기2
    print(cabinet[5]) #키가없으면 종료
    print(cabinet.get(5)) #키가없으면 none출력후 값이어가기가능
    print(cabinet.get(5,"사용 가능")) #키가없으면 "사용가능"이라 출력하기
    print(3 in cabinet) #True
    print(5 in cabinet) #Fale
    #방법2
    cabinet = {"a-3":"유재석","b-100":"김태호"}
    print(cabinet["a-3"])
    print(cabinet["b-100"])
    #새손님
    print(cabinet)
    cabinet["a-3"]="김종국"
    cabinet["c-20"]="조세호"
    #간손님
    del cabinet["a-3"]
    #key 들만 출력
    print(cabinet.keys())
    #value 들만 출력
    print(cabinet.values())
    #둘다출력
    print(cabinet.items())
    #목욕탕 폐점
    cabinet.clear()

    튜플
    #내용변경 추가변경불가 속도는 리스트보다빠름
    menu = ("돈가스","치즈가스")
    print(menu(0))
    print(menu(1))
    menu.add("생선가스") #불가능
    name = "김종국"
    age = 20
    hobby = "코딩"
    print(name, age, hobby)
    (name, age, hobby) = "김종국", 20, "코딩"
    print(name, age, hobby)

    집합(set) #중복안됨, 순서없음
    my_set = {1,2,3,3,3}
    print(my_set) #1,2,3
    java = {"유재석","김태호","양세형"}
    python = set(["유재석","박명수"])
    # 교집합 (java와 python 을 모두할수있는사람)
    print(java and python) #"유재석"
    print(java.intersection(python)) #위에랑 똑같음
    # 합집합 (java나 python을 할수 있는사람)
    print(java or python) 
    print(java.union(python))
    # 차집합 (java는 할줄알지면 python 못하는사람)
    print(java - python)
    print(java.difference(python))
    #python 할줄아는 사람 늘어남 값더하기
    python.add("김태호")
    #java를 잊었어요 값빼기
    java.remove("김태호")

    자료구조의 변경
    menu = {"커피", "우유", "주스"}
    print(menu, type(menu)) #class 'set'
    menu = list(menu)
    print(menu, type(menu)) #class 'list'
    menu = tuple(menu)
    print(menu, tuple(menu)) #class 'tuple'

    퀴즈퀴즈
    #당신의 학교에서는 파이썬 코딩 대회를 준비합니다.
    #참석률을 높이기 위해 댓글이벤트를 진행하기로 하였습니다.
    #댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.
    #추첨 프로그램을 작성하십시오.

    #조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
    #조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
    #조건3 : random 모듈의 shuffle 과 sample을 활용
    (출력예제)
    --당첨발표--
    치킨 당첨자 : 1
    커피 당첨자 : [2,3,4]
    --축하합니다--
    (활용예제)
    from random import *
    1st = [1,2,3,4,5]
    print(1st) #1,2,3,4,5
    shuffle(1st) #리시트안에있는 값을 무작위로 바꿈
    print(1st) #2,3,4,1,5 처럼 무작위로랜덤
    print(sample(1st,1)) #리스트중에서 한개를 무작위로 뽑겟다
    -정답
    from random import *
    users = range(1,21) #1부터 20까지 숫자를 생성
    print(type(users)) #range 타입이라 list함수를 쓸수가없음
    users=list(users) #list 타입으로 변환
    print (users) #1~20까지 생성
    shuffle(users) #무작위로 랜덤
    print(users) #1~20까지 무작위로 생성
    winners = sample(users,4) #4명중에서 1명치킨 3명은 커피
    print("당첨자발표")
    print("치킨당첨자 : {0}".format(winners[0])) #1명
    print("커피당첨자 : {0}".format(winners[1:])) #3명
    print("축하합니다")

    분기(만약)
    weather = "비"
    if 조건:
        실행명령문
    if weather == "비":
        print("우산을 챙기세요") #우산을챙기세요
    if weather == "맑음":
        peinr("우산을 챙기세요") #조건이 해당안됨
         elif weather == "미세먼지": #다음조건
          print("마스크를 챙기세요")
         else:
           print("나가세요") #둘다아니면
    weather = input("오늘 날씨는 어때요?") #조건을 찾으면 바로대답함
    #다른예제
    temp = int(input("기온은 어때요?"))
    if 30 <= temp:
        print("너무 더워요 나가지 마세요")
        elif 10 <= temp and temp < 30:
            print("괜찮은 날씨에요")
        elif 0 <= temp and temp < 10:
            print("외투를 챙기세요")
        else:
            print("너무 추워요 나가지마세요")

    반복문
    print("대기번호 : 1")
    print("대기번호 : 2")

    for waiting_no in [0,1,2,3,4]:
        print("대기번호 : {0}".format(wating_no))
    ==
    for waiting_no in range(5): #0,1,2,3,4 = #randrange()
                      range(1,6): #1부터 6미만[1,2,3,4,5]
    #다른예제
    starbucks = ["아이언맨","토르","아이엠그루브"]
    for customer in strbucks:
        print("{0}, 커피가 준비되었습니다".format(customer))#돌아가면서 3번다부름
    #while
    customer = "토르"
    index = 5
    while (조건): 조건을 만족할때까지 반복해라

    while index >= 1:
        print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
        index -= 1
        if index == 0:
            print("커피는 폐기처분되었습니다.")
        #토르 커피가 준비되었습니다 5번남앗어요 ...1번남았어요
        #폐기처분되엇습니다.
    #다른예제
    customer = "아이언맨"
    while True:
        print("{0},커피가 준비 되었습니다 호출 {1}회".format(customer, index))
        index +=1 #아이언맨 커피가 준비되었습니다 호출 무한회 = 무한루프 컨트롤c중단
    #다른예제
    customer = "토르"
    person = "Unknown"

    while person != customer :
        print("{0}, 커피가 준비 되었습니다".format(customer))
        person = input("이름이 어떻게 되세요?") #만족할때 까지 무한루프
        #토르 커피가 준비되었습니다.
        #이름이 어떻게 되세요 ? 아이언맨
        #토르 커피가 준비되었습니다
        #이름이 어떻게 되세요 ? 토르 #탈출성공

    반복문 Continue 와 Break
    absent = [2, 5] # 결석
    no_book = [7] # 책을깜빡했음
    for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10
        if student in absent:
            continue
        elif student in no_book:
            print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
            break
        print("{0}, 책을 읽어봐".format(student))

    한줄 For
    #출석번호가 1 2 3 4 , 앞에 100을 붙이기로함 = 101, 102, 103, 104
    sutdents = [1,2,3,4,5]
    students = [i+100 for i in students]
    #학생이름을 길이로 변환
    students = ["Iron man", "Thor", "I am groot"]
    students = [len(i) for i in students]
    #학생 이름을 대문자로 변환
    students = [i.upper() for i in students]

    퀴즈퀴즈
    당신은 cocoa서비스를 이용하는 택시기사님입니다.
    50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
    조건1 : 승객별 운행소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
    조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
    (출력문예제)
    [0]1번째 손님 (소요시간 : 15분)
    []2번째 손님 (소요시간 : 50분)
    총탑승승객 : {}분
    
    from random import *
    cnt = 0 # 총탑승 승객수
    for i in range(1,51): # 1~50 이라는 수 (승객)
        time = randrange(5,51) # 5분 ~ 50분 소요시간
        if 5 <= time  <=15: # 5분~15분 이내의 손님(매칭성공), 탑승 승객수 증가처리
            print("[0] {0}번째 손님 (소요시간 : {1}분").format(i, time)
            cnt += 1
        else: #매칭 실패할경우
            print("[ ] {0}번째 손님 (소요시간 : {1}분").format(i, time)
    print("총 탑승승객 : {0}분".format(cnt))

    함수
    def open_account():
        print("새로운 계좌가 생성되었습니다")
    open_account()
    전달값과 변환값
    def deposit(balance,moneey): #입금
        print("입금이 완료되었습니다 잔액은 {0}원 입니다".format(balance + money))
        return balance+moneey
    balance = 0 #잔액
    balance = deposit(balance, 1000)
    print(balance)

    def withdraw(balance, money): #출금
        if balance >= money: #잔액이 출금보다 많으면
            print("출금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance - money))
        else:
            print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
            return balance

    def withdrwa_night(balance,money): #저녁에 출금
        commission = 100 #수수료100원
        return commission, balance - money - commission

    balance = 0 #잔액
    balance = deposit(balance, 1000)
    commission, balance = withdraw_night(balance, 500)
    print("수수료 {0}원이며, 잔액은 {1}원입니다".format(commission,balance))
    함수기본값
    def profile(name, age, main_lang)
        print("이름 : {0}\t나이: {1} \t주 사용언어 : {2}"\
            .format(name, age, main_lang))
    profile("유재석", 20,"파이썬")
    profile("김태호", 25,"자바")
    키워드값
    def profile(name, age, main_lang)
        print(name,age,main_lang)
    profile()
    가변인자
    # def profile(name, age, lang1,lang2,lang3,lang4,lang5):
    #     print("이름:{0}\t나이:{1}\t".format(name,age),end="")
    #     print(lang1,lang2,lang3,lang4,lang5)
    def profile(name, age, *language):
        print("이름:{0}\t나이:{1}\t".format(name,age),end="")
        for lang in language:
            print(lang, end="")
        print()
    profile("유재석", 20, "python","java","c","c++","c#")
    profile("김태호",25,"kotlin","swift","","","")
    2시 48분
        
    지역변수와 전역변수
    지역변수(함수내에서만 쓸수있는거, 함수가끝나면 사라짐)
    전역변수(모든공간에서 사용가능) global(코드관리가힘듬)
    gun = 10

    def checkpoint(soldiers) : #경계근무
        gun = gun - soldiers
        print("[함수 내] 남은 총 : {0}".format(gun))

    print("전체 총 : {0}".format(gun))
    checkpoint(2) #2명이 경계 근무 나감
    print("남은 총 : {0}".format(gun))


    

    



    
    

    
        






