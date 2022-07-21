def find_student(name,student_dict):
    if name in student_dict:
        print(f'{name}의 전화번호는 {student_dict[name]}입니다.')
        
    else:
        print("등록된 학생이 아닙니다.")
        
        
student = {
    '홍길동':'010-1111-1111',
    '이순신':'010-1111-2222',
    '강감찬':'010-1111-3333'
}

a = "아래 학생들의 전화번호를 조회할 수 있습니다. \n홍길동\n이순신\n강감찬\n전화번호를 조회하고자 하는 학생의 이름을 입력하십시오."

print(a)
name = input()
find_student(name, student)