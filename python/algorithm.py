'''
Recursion
1 to 10 print using by recursion
'''
def recursion(n):
	if n <= 0:
		return 1
	print(n)
	return recursion(n-1)

print("Input your number: ")
n = int(input())
recursion(n)

'''
Linear Search
'''

import random
def linear_search(a_list, n):
	"""
	find n in a_list and 
	if n was in a_list, return True
	"""
	for i in a_list:
		if i == n:
			return True
		return False
	

a_list = random.choices(range(1,10), k = 10) # 복원 추출 방식=중복O, 1~10개 숫자 중 10개를 뽑아라

print(linear_search(a_list, 10))


'''
Binary Search
'''

def binary_search(a_list, n):
	first = 0
	last = len(a_list)-1
	while last >= first:
		mid = (first+last) // 2 # 나눠서 나온 몫을 mid로 설정.
		if a_list[mid] == n:
			return True
		elif a_list[mid] < n:
			first = mid + 1
		else:
			last = mid - 1
	return False #루프가 종료되었다면, 찾는 숫자를 끝까지 못 찾은 것이기에 False 반환