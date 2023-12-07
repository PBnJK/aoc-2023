# AOC 2023, Day 02 

from pathlib import Path
import re

re_game_num = re.compile(r"(\d+):")

def get_input():
	with open( Path(__file__).parent / 'input.txt', 'r' ) as f:
		return f.readlines()

def get_games():
	i = get_input()
	games = {}
	
	for game in i:
		game = game.strip()
		
		num = int( re_game_num.search(game).group(1) )
		games[num] = []
		
		sets = game.split(': ')[1]
		sets = sets.split('; ')
		
		for set in sets:
			game_pairs = []
			
			set = set.split(', ')
			
			for pair in set:
				game_pairs.append(pair.split(' '))
			
			games[num].append(game_pairs)
	
	return games
	
def solution1():
	MAX_RED  : int = 12
	MAX_GREEN: int = 13
	MAX_BLUE : int = 14
	
	NUMBER_IDX: int = 0
	COLOR_IDX : int = 1
	
	games = get_games()
	
	id_sum: int = 0
	
	for g in games:
		red_amnt  : int = 0
		green_amnt: int = 0
		blue_amnt : int = 0
		
		for round in games[g]:			
			for pair in round:
				if pair[COLOR_IDX] == 'red':
					red_amnt = max( int(pair[NUMBER_IDX]), red_amnt )
					
				elif pair[COLOR_IDX] == 'green':
					green_amnt = max( int(pair[NUMBER_IDX]), green_amnt )
					
				elif pair[COLOR_IDX] == 'blue':
					blue_amnt = max( int(pair[NUMBER_IDX]), blue_amnt )
			
		if red_amnt <= MAX_RED and green_amnt <= MAX_GREEN and blue_amnt <= MAX_BLUE:
			id_sum += g
				 
	return id_sum
 
def solution2(): 
	NUMBER_IDX: int = 0
	COLOR_IDX : int = 1
	
	games = get_games()
	
	cube_set_power: int = 0
	
	for g in games:
		red_amnt  : int = 0
		green_amnt: int = 0
		blue_amnt : int = 0
		
		for round in games[g]:			
			for pair in round:
				if pair[COLOR_IDX] == 'red':
					red_amnt = max( int(pair[NUMBER_IDX]), red_amnt )
					
				elif pair[COLOR_IDX] == 'green':
					green_amnt = max( int(pair[NUMBER_IDX]), green_amnt )
					
				elif pair[COLOR_IDX] == 'blue':
					blue_amnt = max( int(pair[NUMBER_IDX]), blue_amnt )
			
		cube_set_power += red_amnt * green_amnt * blue_amnt
				 
	return cube_set_power
