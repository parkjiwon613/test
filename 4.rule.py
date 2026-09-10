#입력 규칙
class Rule:
    def __init__(self):
        self.guess_list=[]

    def one(self):
        print("한 번에 한 글자만 입력해주세요")
                
    def alpha_only(self):
        print("알파벳만 입력해주세요")

    def duplication(self):
        print("이미 입력한 글자입니다.")

    def note(self):
        while True:
            guess = input("글자를 입력하세요: ")
            guess = guess.lower() 
            
            if len(guess) != 1:
                self.one()
                continue
            
            if not guess.isalpha():
                self.alpha_only()
                continue

            if guess in self.guess_list:
                self.duplication()
                continue
            
            return guess 

