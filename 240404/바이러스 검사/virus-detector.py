import sys
n = int(input())
customers = list(map(int, sys.stdin.readline().split()))
l, m = map(int, input().split())

def required_member_num(customer_num):
	#남은 고객이 없는 경우
	if customer_num <= 0:
		return 0
	#딱 나누어 떨어지는 경우
	elif customer_num % m == 0:
		return customer_num // m
	#나누어 떨어지지 않는 경우
	else:
		return (customer_num // m) + 1

answer = 0
for customer_num in customers:
	#식당마다 팀장은 한 명이 필요
	answer += 1
	#필요한 팀원 수 계산
	answer += required_member_num(customer_num - l)
	
print(answer)