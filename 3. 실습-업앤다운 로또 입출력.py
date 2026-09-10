import random

class LoginManager:
    def __init__(self, id_key, password_key, max_attempts=3):
        self.id_key = id_key
        self.password_key = password_key
        self.max_attempts = max_attempts

    def login(self):
        for i in range(1, self.max_attempts+1):
            id  = input('아이디: ')
            password = input('비밀번호: ')

            if id == self.id_key and password == self.password_key:
                print('로그인에 성공했습니다.')
                return True

            if i < 3:
                print(f"로그인에 실패했습니다. 남은 기회는 {3-i}번 입니다.")
                
            elif i == 3:
                print(f'로그인에 {i}회 실패했습니다. 프로그램을 종료합니다.')
                return False

class RankingBoard:
    def __init__(self, lotto_game):
        self.result = []
        self.lotto_game = lotto_game

    # 게임 종료 후 랭킹 텍스트 파일에 저장
    def add(self, tries, name): 
        dummies = [tries, name]
        self.result.append(dummies)
        with open("ranking.txt", "a", encoding="utf-8") as file:
            file.write(f"{name},{tries}\n")

    # 과거 이력(로또) - txt 에서 불러오기
    def past(self, botton):
        if botton == 1:
            print('1.과거 이력 보기')
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

    # 랭킹 보기(업앤다운) - txt에서 불러오기 및 정렬
    def ranking(self, botton): 
        if botton == 2:
            print("2. 랭킹 보기")
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

                # 시도횟수 기준 오름차순 정렬
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


class Lottogame:
    def __init__(self):
        self.nums = []
        
    # 수동 자동 선택
    def auto_or_hand(self):
        lotto = input('수동 or 자동: ')
        if lotto == '수동':
            self.lotto_hand()
        elif lotto == '자동':
            self.lotto_auto()

    # 로또 자동 추첨
    def lotto_auto(self):
        while True:
            print('자동추첨')
            num = [] 
            while len(num) < 6:
                number = random.randint(1, 45)
                if number in num:
                    continue
                num.append(number)
            num.sort()
            break
        self.print_lotto(num)

    # 범위검사
    def range_check(self, number, num):
        if number < 1 or number > 45:
            print("1~45 사이의 번호를 입력하세요.")
            return
                
        self.duplication_check(number, num)

    # 중복검사
    def duplication_check(self, number, num):        
        while True:
            if number in num:
                print("이미 입력한 번호입니다.")
                return
            num.append(number)
            break

    # 로또 수동추첨
    def lotto_hand(self): 
        while True:
            print('수동추첨')
            num = [] 
            count = int(input("직접 입력할 번호 개수(0~6) : "))
            while len(num) < count:
                number = int(input(f"{len(num) + 1}번째 번호 : "))
                self.range_check(number, num)

            # 부족한 번호 자동 생성
            while len(num) < 6:
                number = random.randint(1, 45)
                if number in num:
                    continue
                num.append(number)
            num.sort()
            break
        self.print_lotto(num)

    #############################
    # 로또 결과 출력
    def print_lotto(self, num):
        print("추천 로또 번호 :", *num)
        self.save_lotto(num)

    #############################
    # 로또 이력 txt로 저장
    def save_lotto(self, num):
        self.nums.append(num.copy())
        line = ""
        for i in range(len(num)):
            line += str(num[i])
            if i < len(num) - 1:
                line += ","

        with open("lotto_history.txt", "a", encoding="utf-8") as file:
            file.write(line + "\n")
            
        return self.nums


class UpDowngame:
    def __init__(self, max_number):
        self.max_number = max_number
        self.target = random.randint(1, max_number) 
        self.dummies = []
        self.tn = 0

    def input_number(self):
        while True:
            try:
                num = int(input('숫자를 입력하세요: '))
                return num
            except ValueError:
                print('숫자만 입력하세요')

    def guesswhat(self, num):
        if self.target > num:
            print('더 높게 입력하세요')
        elif self.target < num:
            print('더 작게 입력하세요')

    def play(self):
        print(f"1부터 {self.max_number} 사이의 숫자를 입력하세요")

        while True:
            num = self.input_number()
            self.tn += 1
            if num == self.target:
                print('정답입니다!')
                print(f'시도횟수: {self.tn}회')
                name = input('이름을 입력하세요: ')
                return self.tn, name
            
            self.guesswhat(num)


class App:
    def __init__(self):
        self.login_manager = LoginManager('jiwon', '1234')
        self.lotto_game = Lottogame()
        self.ranking_board = RankingBoard(self.lotto_game)

    # 메뉴 출력
    def print_menu(self):
        print("\n1. 게임 시작")
        print("2. 랭킹 보기")
        print("3. 게임 종료")

    def menu(self):
        while True:
            try:
                m = int(input('메뉴를 설정하세요: '))
                return m
            except ValueError:
                print('숫자만 입력해주세요')

    def run(self):
        if not self.login_manager.login():
            return
        
        while True:
            self.print_menu()
            m = self.menu()

            if m == 1:
                print("1.로또 번호 추출기 \n2.업앤다운 게임")
                botton1 = int(input("번호를 선택해주세요: ")) 

                if botton1 == 1:
                    self.lotto_game.auto_or_hand()

                # 업앤다운 난이도 기능 반영
                elif botton1 == 2:
                    level = input("난이도를 고르시오(상, 중, 하): ")
                    if level == '상':
                        game = UpDowngame(500)
                    elif level == '중':
                        game = UpDowngame(300)
                    elif level == '하':
                        game = UpDowngame(100)
                        
                    tn, name = game.play() # tn, name return받음
                    self.ranking_board.add(tn, name)

            elif m == 2:
                print('2.과거이력 및 랭킹보기👀\n')
                print("1.과거이력 \n2.랭킹보기")
                botton = int(input("번호를 선택해주세요: "))

                if botton == 1:
                    self.ranking_board.past(botton)
                elif botton == 2:
                    self.ranking_board.ranking(botton)

            elif m == 3:
                print('종료하기👋')
                break

            else:
                print('잘못된 메뉴입니다.')
                                    
app = App()
app.run()
