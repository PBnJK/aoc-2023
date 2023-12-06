# AOC 2023, Day 01 

from pathlib import Path

SUB_KEY = [
	['one',   'one1one'],
	['two',   'two2two'],
	['three', 'three3three'],
	['four',  'four4four'],
	['five',  'five5five'],
	['six',   'six6six'],
	['seven', 'seven7seven'],
	['eight', 'eight8eight'],
	['nine',  'nine9nine'],
]

def get_input():
	with open( Path(__file__).parent / 'input.txt', 'r' ) as f:
		return f.readlines()

def solution1(): 
	total_sum: int = 0
	
	for cmd in get_input():
		l_num: int = -1
		r_num: int = -1
	
		cmd = cmd.strip()
		
		for l in cmd:
			if l.isdigit():
				if l_num == -1:
					l_num = int(l)
					r_num = l_num
				else:
					r_num = int(l)
		
		total_sum += ( l_num * 10 ) + r_num
		
	return total_sum
	
def solution2(): 
	total_sum: int = 0
	
	for cmd in get_input():
		l_num: int = -1
		r_num: int = -1

		cmd = cmd.strip()
		
		for i in range(9):
			cmd = cmd.replace( SUB_KEY[i][0], SUB_KEY[i][1] )
		
		for l in cmd:
			if l.isdigit():
				if l_num == -1:
					l_num = int(l)
					r_num = l_num
				else:
					r_num = int(l)
		
		total_sum += ( l_num * 10 ) + r_num
		
	return total_sum
