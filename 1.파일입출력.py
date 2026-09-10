#파일 쓰기 기본: w
file=open("test.txt","w",encoding="utf-8")
file.write("안녕하세요")
file.close()

#권장 방식: with open()
with open("test.txt","w",encoding="utf-8")as file:
	file.write("안녕하세요")

#파일 위치 개념
with open("memo.txt","w",encoding="utf-8")as file:
	file.write("오늘은 파일 입출력을 배웁니다.")

#여러줄 저장
with open("test.txt","w",encoding="utf-8")as file:
	file.write("1일차 학습\n")
	file.write("2일차 학습\n")
	file.write("3일차 학습\n")

#파일 읽기: r
with open("memo.txt","r",encoding="utf-8")as file:
	content=file.read()

print(content)

#파일 읽기 방식 3가지
# 1) read()- 전체를 하나의 문자열로 읽습니다.
# 2) readline()  - 한 줄씩 읽습니다.
with open("test.txt","r",encoding="utf-8")as file:
	line1=file.readline()
	line2=file.readline()

print(line1)
print(line2)

# 3) readlines()  - 여러 줄을 읽습니다.
with open("test.txt","r",encoding="utf-8")as file:
	lines=file.readlines()

print(lines)

#줄바꿈과 공백 제거 
for line in lines:
	print(line.strip())


#파일에 내용 추가: a
with open("test.txt","a",encoding="utf-8")as file:
	file.write("4일차 학습\n")

######################################
#사용자 입력을 메모장에 저장하기
memo=input("메모를 입력하세요: ")

with open("memo.txt","w",encoding="utf-8")as file:
	file.write(memo)

#여러 메모를 계속 추가하기
while True:
	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

	if memo.lower()=="q":
		break
	
	with open("memo.txt","a",encoding="utf-8")as file:
		file.write(memo+"\n")
	
	print("메모 저장이 완료되었습니다.")

#학생 점수 txt파일 저장하기
students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

with open("students.txt","w",encoding="utf-8")as file:
	for student in students:
		file.write(f"{student['name']},{student['score']}\n")


#학생 점수 txt 파일 읽기
students = []

with open("students.txt", "r", encoding="utf-8") as file:
    lines = file.readlines() #문자로 되어있는 데이터 읽기

for line in lines:             
    data = line.strip().split(",")  #공백제거, (,)을 기준으로 나누기
	
    #딕셔너리화
    student = {
        "name": data[0],
        "score": int(data[1])
    }

    students.append(student)

print(students)

####################################################
#예외처리와 연결하기
#파일이 없는 경우
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

else:
    print(content)
	
#숫자가 없는 경우
line = "민수,팔십오"

try:
    data = line.strip().split(",")
    name = data[0]
    score = int(data[1])

except ValueError:
    print("점수는 숫자로 입력해야 합니다.")

else:
    print(name, score)

#############################################################
# 파일 입출력 함수로 묶기
# 학생 데이터 저장 함수
def save_students(students, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            line = f"{student['name']},{student['score']}\n"
            file.write(line)

students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

save_students(students,"students.txt")

# 학생 데이터 읽기 함수
def load_students(filename):
    students = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(",")

        student = {
            "name": data[0],
            "score": int(data[1])
        }

        students.append(student)

    return students

students=load_students("students.txt")
print(students)

##################################################3
#현재 작업 폴더와 파일 존재 여부 확인
import os

print(os.getcwd())


if os.path.exists("ranking.txt"):
    print("랭킹 파일이 있습니다.")
else:
    print("랭킹 파일이 없습니다.")

#랭킹 한 건 저장
def save_ranking(name, count):
    with open("ranking.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{count}\n")

name = input("이름을 입력하세요: ")
count = 4

save_ranking(name, count)