# 유저의 숫자 입력을 10개 받아서
# 그 숫자 기록과, 그 합을 파일에 저장하는 프로그램

user_input_list = []
for i in range(0, 10):
    user_input = input(f"숫자를 입력해주세요({i}/10)")
    user_input = float(user_input)
    user_input_list.append(user_input)


f = open("result.txt", "w")
sum = 0
for number in user_input_list:
    f.write(str(number))
    sum += number
f.write(str(sum))