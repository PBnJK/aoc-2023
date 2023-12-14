# AOC 2023, Day 03 

from pathlib import Path
import re

SIZE: int = 140

match_nums = re.compile(r'(\d+)')
match_symb = re.compile(r'([^a-zA-Z0-9.])')

def get_input():
	with open( Path(__file__).parent / 'input.txt', 'r' ) as f:
		return f.readlines()
		
def get_schematic_map():
	i = get_input()
	map = []
	
	x = 0
	
	for line in i:
		for m in match_nums.finditer(line):
			item = []
			num = m.group(1)
		
	return map

def solution1(): 
	return 'Nothing to see here yet' 
 
def solution2(): 
	return 'Nothing to see here yet' 
