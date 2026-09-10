import random
nums =[]
result=[]

#로그인
def login():
    id_key='jiwon'
    password_key='1234'

    for i in range(1,4):
        id  = input('아이디: ')
        password = input('비밀번호: ')

        if id == id_key and password == password_key:
            print('로그인에 성공했습니다.')
            menu()
            break

        if i < 3:
            print(f"로그인에 실패했습니다. 남은 기회는 {3-i}번 입니다.")
            
        elif i == 3:
            print(f'로그인에 {i}회 실패했습니다. 프로그램을 종료합니다.')
            break


#기존 로또 과거 이력을 TXT로 저장하기
def save_lotto(lotto):
    line = ""

    for i in range(len(lotto)):
        line += str(lotto[i])

        if i < len(lotto) - 1:
            line += ","

    with open("lotto_history.txt", "a", encoding="utf-8") as file:
        file.write(line + "\n")

# 로또 추첨 (자동 or 수동)
def lotto_auto(): #로또 자동추첨
    while True:
        print('자동추첨')
        num =[] 
        while len(num) < 6:
            number = random.randint(1, 45)
            if number in num:
                continue
            num.append(number)
        num.sort()
        break
    print_lotto(num)


#범위검사
def range_check(number,num):
    while True:
        if number < 1 or number > 45:
            print("1~45 사이의 번호를 입력하세요.")
            continue
        
        break
    duplication_check(number,num)

#중복검사
def duplication_check(number,num):       
    while True:
        if number in num:
            print("이미 입력한 번호입니다.")
            return
        num.append(number)
        break

#로또 수동추첨
def lotto_hand(): 
    while True:
        print('수동추첨')
        num =[] 
        count = int(input("직접 입력할 번호 개수(0~6) : "))
        while len(num) < count:

            number = int(input(f"{len(num) + 1}번째 번호 : "))
            range_check(number,num)

        # 부족한 번호 자동 생성
        while len(num) < 6:
            number = random.randint(1, 45)
            if number in num:
                continue
            num.append(number)
        num.sort()
        break
    print_lotto(num)


#############################
# 로또 결과 출력
def print_lotto(num):
    print("추천 로또 번호 :", *num)
    save_lotto(num)

#############################

# 업앤다운 게임

def updown(max_number):
    
    tn = 1
    name =  input('이름을 입력하세요: ')
    dummies = []
    target = random.randint(1,max_number) 
    while True:
        
        num = int(input('숫자를 입력하세요: '))
        if target > num:
            print('더 높게 입력하세요')
            tn += 1
        elif target < num:
            print('더 작게 입력하세요')
            tn += 1
        elif target == num:
            print('정답입니다!')
            dummies = [tn,name]
            result.append(dummies)
            result.sort()
            save_ranking(tn,name)
            break

###############################################################   
###############################################################
## 이력 및 랭킹
#로또 이력 보기

def load_lotto_history():
    lotto_history = []

    try:
        with open("lotto_history.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")
            lotto = []

            for number in data:
                lotto.append(int(number))

            lotto_history.append(lotto)

        for i in range(len(lotto_history)):
            print(i + 1, "회차 :", lotto_history[i])

    except FileNotFoundError:
        print("아직 저장된 로또 이력이 없습니다.")

    return lotto_history


###########################################################3
# 랭킹 보기(업앤다운)
#랭킹 파일 생성
def save_ranking(count, name):
    with open("ranking.txt","a",encoding="utf-8") as file:
        file.write(f"{name},{count}\n")

#업앤다운 랭킹 파일 다시 불러오기            
def load_ranking():
    players = []

    try:
        with open("ranking.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")

            player = {
                "name": data[0],
                "시도횟수": int(data[1])
            }

            players.append(player)

        for i in range(len(players) - 1):
            for j in range(len(players) - 1 - i):
                if players[j]["시도횟수"] > players[j + 1]["시도횟수"]:
                    temp = players[j]
                    players[j] = players[j + 1]
                    players[j + 1] = temp

        for i in range(len(players)):
            print(f"{i + 1}위 : {players[i]['name']} / {players[i]['시도횟수']}회")
           
    except FileNotFoundError:
        print("아직 저장된 랭킹이 없습니다.")

    return players

#################################
# 업앤다운 난이도 고르기
def updown_level():
    level = input("난이도를 고르시오(상, 중, 하): ")
    if level == '상':
        updown(500)
    elif level == '중':
        updown(300)
    elif level == '하':
        updown(100)

# 로또 수동 자동 고르기
def auto_or_hand():
    lotto = input('수동 or 자동: ')
    if lotto == '수동':
        lotto_hand()
    elif lotto =='자동':
        lotto_auto()

# 메뉴 출력
def print_menu():
    print("1. 게임 시작")
    print("2. 랭킹 보기")
    print("3. 게임 종료")

# 메인 메뉴
def menu():
    while True:
        print_menu()
        m = int(input('메뉴를 설정하세요: '))

        if m == 1:
            print("1.로또 번호 추출기 \n2.업앤다운 게임")
            botton1 = int(input("번호를 선택해주세요: "))

            if botton1 == 1:
                auto_or_hand()

            elif botton1 == 2:
                updown_level()

        elif m == 2:
            print('2.과거이력 및 랭킹보기👀\n')
            print("1.과거이력 \n2.랭킹보기")
            botton3 = int(input("번호를 선택해주세요: "))

            if botton3 == 1:
                load_lotto_history()
            elif botton3 == 2:
                load_ranking()     

        elif m == 3:
            print('종료하기👋')
            break
        
login()
