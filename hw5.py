num_input = input("세 자리수의 숫자를 입력하세요")

kor_list = ["영","일","이","삼","사","오","육","칠","팔","구"]

def read_single_digit(number):
  print(kor_list[number] , end="")

def read_number(num_input):
  #백의 자릿수
  a = int(num_input[0])
  #십의 자릿수
  b = int(num_input[1])
  #일의 자릿수
  c = int(num_input[2])

  read_single_digit(a)
  read_single_digit(b)
  read_single_digit(c) 

read_number(num_input)
