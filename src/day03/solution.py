# AOC 2023, Day 03 

from pathlib import Path
import re

SIZE: int = 140

match_nums = re.compile(r'(\d+)')
match_symb = re.compile(r'([^a-zA-Z0-9.])')
match_aste = re.compile(r'(\*)')

def get_input():
	with open( Path(__file__).parent / 'input.txt', 'r' ) as f:
		return f.readlines()

def solution1():
	i = get_input()
	map = []
	
	for ln, line in enumerate(i):
		for m in match_nums.finditer(line):
			num = int(m.group(1))
			s1, s2 = m.span()
			
			symbols: str = ''
			
			left  = s1 - 1 if s1 > 0 else s1
			right = s2 if s2 < 139 else s2 - 1
			
			symbols += line[left]
			symbols += line[right]
			
			if ln > 0:
				top = i[ln - 1]
				symbols += top[left:right + 1]
			if ln < 139:
				bottom = i[ln + 1]
				symbols += bottom[left:right + 1]
			
			map.append((num, symbols, m.span()))
	
	total = 0
	
	for n in map:
		if match_symb.search(n[1]) != None:
			total += n[0]
	
	return total
 
def solution2(): 
	i = get_input()
	map = []
	
	gear = 0
	
	for ln, line in enumerate(i):
		for m in match_aste.finditer(line):
			s1, s2 = m.span()
			
			top = i[ln-1][s1-3:s2+3]
			bottom = i[ln+1][s1-3:s2+3]
			
			nums = []
			
			for txt in (top, bottom):
				for n in match_nums.finditer(txt):
					ns1, ns2 = n.span()
					
					if ns1 in (2, 3, 4) or ns2 in (3, 4, 5):
						nums.append(n.group(1))
			
			if line[s1-1] != '.':
				for ls in match_nums.finditer(line[s1-3:s1]):
					nums.append(ls.group(1))
			
			if line[s2] != '.':
				for rs in match_nums.finditer(line[s2:s2+3]):
					nums.append(rs.group(1))
			
			if len(nums) == 2:
				gear += int(nums[0]) * int(nums[1])
	
	return gear
