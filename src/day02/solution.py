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

def get_color_amount_in_games():
	NUMBER_IDX: int = 0
	COLOR_IDX : int = 1
	
	amounts = {}
	
	games = get_games()
	
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
		
		amounts[g] = [red_amnt, green_amnt, blue_amnt]
	
	return amounts

def solution1():
	MAX_RED  : int = 12
	MAX_GREEN: int = 13
	MAX_BLUE : int = 14
	
	id_sum: int = 0
	amounts = get_color_amount_in_games()
	
	for a in amounts:
		rgb = amounts[a]
		
		if rgb[0] <= MAX_RED and rgb[1] <= MAX_GREEN and rgb[2] <= MAX_BLUE:
			id_sum += a
				 
	return id_sum
 
def solution2(): 
	cube_set_power: int = 0
	
	amounts = get_color_amount_in_games()
	
	for a in amounts:
		rgb = amounts[a]
		cube_set_power += rgb[0] * rgb[1] * rgb[2]
				 
	return cube_set_power
