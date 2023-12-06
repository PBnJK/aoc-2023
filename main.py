# AOC 2023!

import importlib

from os.path import isfile

def print_solution(module) -> None:
	if hasattr(module, 'solution1'):
		print(f'- 1st Star: {module.solution1()}')
	else:
		print('- 1st Star: Yet to be solved!')
	
	if hasattr(module, 'solution2'):
		print(f'- 2nd Star: {module.solution2()}\n')
	else:
		print('- 2nd Star: Yet to be solved!\n')
		
def run_solution(file_name: str, day: int) -> None:
	if not isfile(file_name + '.py'):
		raise ValueError(f'Path provided is not a valid file ("{file_name}")!')
		
	file_as_import: str = '.'.join( file_name.split('/') )
	module = None
	
	try:
		module = importlib.import_module(file_as_import)		
	except ImportError as e:
		raise ImportError(f'An error occured while importing the module {file_as_import}')
	
	print(f'DAY {day:02}')
	print_solution(module)

def main() -> None:
	for folder_num in range(1, 26):
		run_solution(f'src/day{folder_num:02}/solution', folder_num)

if __name__ == '__main__':
	main()