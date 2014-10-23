"""
Bowling Score Keeper

This module is designed to take input from bowling alley hardware, and 
update and display player scores accordingly

This module was written by Isaac Dykeman
"""

import random
WIDTH_OF_NAME_COLUMN = 12
FRAMES_PER_GAME = 10
MAX_THROWS_PER_GAME = 2*9+3 # nine frames of 2 balls, and a frame of 2 or 3 balls
PLAYER_ROW_DIVIDER = "--------------------------------------------------------------------------------------"
TABLE_HEADER       = "====================================Current=Scores===================================="
COLUMNS_HEADER     = "|    Name    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |   10  |  Total  |"


class Frame:
	"""
	A single frame in one player's bowling game. Can be a frame of two balls,
	or can be the final frame, which has two or three balls, depending on
	whether the player gets a strike on the first ball of that frame.

	Args:
		num_throws (int): Max possible throws in this frame.

	Attributes:
		_num_throws (int): Max possible throws in this frame.
		_throws (list of int): The scores for each throw
	"""
	def __init__(self, num_throws):
		self._num_throws = num_throws
		self._throws = []

	def get_throw(self,index):
		"""
		Returns the score (int) of a throw at the given index

		Args:
			index (int): The index of the score to return			
		"""
		if index<len(self._throws):
			return self._throws[index]
		return 0	
			
	def get_first_throw(self):
		"""
		Returns the score (int) of the first throw of the frame		
		"""
		return self.get_throw(0)

	def get_second_throw(self):
		"""
		Returns the score (int) of the second throw of the frame		
		"""
		return self.get_throw(1)

	def get_third_throw(self):
		"""
		Returns the score (int) of the third throw of the frame		
		"""
		return self.get_throw(2)

	def get_throws_score_string(self):
		"""
		Returns a string which is a readable representations of the scores the
		player has made on the throws in this frame.
		"""
		if not self.is_three_throw_frame(): 
			# seperate logic for frames 1-9 and frame 10
			first_symbol  = self.get_first_throw()
			second_symbol = self.get_second_throw()
			if self.is_strike():
				return "[X,-]"
			if self.is_spare():
				second_symbol = "/"
			return "[%s,%s]" % (first_symbol,second_symbol)
		else: # is three throw frame
			first_symbol  = self.get_first_throw()
			second_symbol = self.get_second_throw()
			third_symbol  = "-"
			if self.is_spare() or self.is_strike():
				# unless it is a strike or a spare, the third frame shows a 
				# dash as its thrid symbol
				third_symbol = self.get_third_throw()
			if self.is_strike():
				first_symbol  = "X"
			elif self.is_spare():
				second_symbol = "/"
			if self.get_third_throw() == 10:
				third_symbol = "X"

			return "[%s,%s,%s]" % (first_symbol, second_symbol, third_symbol)

	def is_strike(self):
		"""
		Returns True if the first throw scored 10 (if the frame is a strike),
		else returns False
		"""
		return self.get_first_throw()==10

	def is_spare(self):
		"""

		"""
		sums_to_10 = self.get_first_throw() + self.get_second_throw() == 10
		return sums_to_10 and not self.is_strike()

	def is_done(self):
		if not self.is_three_throw_frame():
			return len(self._throws) >= self._num_throws or self.is_strike()
		else:
			if self.get_first_throw() == 10 and self.num_throws_taken()<3:
				#strike: take two more shots
				return False
			elif self.is_spare() and self.num_throws_taken()==2:
				#spare: take another shot
				return False
			else:
				return self.num_throws_taken()>1

	def input_new_throw(self,score):
		assert not self.is_done()
		self._throws.append(score)

	def num_throws_taken(self):
		return len(self._throws)

	def is_three_throw_frame(self):
		return self._num_throws == 3

	def get_num_throws(self):
		return self._num_throws

	def get_score_formatted_for_table_column(self,score):
		'''
		
		'''
		num_characters_to_display_throw_scores = 2+ self._num_throws*2-1
		return str(score).ljust(num_characters_to_display_throw_scores)[:num_characters_to_display_throw_scores]
		#adds trailing spaces or truncates string to fit into table exactly



class Player:

	def __init__(self,new_name):
		self._name = new_name
		self.frames = []
		self.current_frame = 0
		for dummy_idx in range(FRAMES_PER_GAME-1):
			self.frames.append(Frame(2))
		self.frames.append(Frame(3))

	def get_name(self):
		'''returns the player's name'''
		return self._name

	def get_score_at(self,ball_idx):
		if(len(self.scores)>ball_idx):
			if self.scores[ball_idx]==-1:
				return 0
			return self.scores[ball_idx]
		return 0

	def get_name_formatted_for_table(self):
		'''
		Gets this players name limitted to the width of the Name field in the score chart.  
		This way, names cannot destort the spacing of the table.
		'''
		return self._name.ljust(width_of_name_column)[:width_of_name_column]#adds trailing spaces or truncates string to fit into table exactly

	def print_score(self):
		'''
		prints the line of the score table that describes this player's scores
		'''
		print(PLAYER_ROW_DIVIDER)

		raw_scores_line = "|            |"
		for i in range(FRAMES_PER_GAME):
			raw_scores_line += self.frames[i].get_throws_score_string()+"|"
		raw_scores_line += "         |"
		print(raw_scores_line)


		accumulated_scores = self.get_score_list()
		accumulated_score_line = "|            |"
		for i,frame in enumerate(self.frames):
			accumulated_score_line += frame.get_score_formatted_for_table_column(str(accumulated_scores[i])) + "|"
		accumulated_score_line += "         |"
		print(accumulated_score_line)

	def get_value_of_two_throws_after_frame(self, index): 
		#TODO: improve name of index
		return self.get_value_of__first_throw_after_frame(index) + self.get_value_of__second_throw_after_strike_on_frame(index)

	def get_value_of__first_throw_after_frame(self, index):
		if index == 9:
			return self.frames[9].get_third_throw()
		else:
			return self.frames[index+1].get_first_throw()

	def get_value_of__second_throw_after_strike_on_frame(self, index):
		if self.frames[index].is_three_throw_frame():
			return self.frames[index].get_third_throw()
		else:
			if not self.frames[index+1].is_strike():
				return self.frames[index+1].get_second_throw()
			else:
				return self.get_value_of__first_throw_after_frame(index+1)

	def get_score_list(self):
		accumulated_score=0
		result = []
		for i, frame in enumerate(self.frames):
			if frame.is_three_throw_frame():
				accumulated_score += frame.get_first_throw()
				accumulated_score += frame.get_second_throw()
				accumulated_score += frame.get_third_throw()
			else:
				if(frame.is_strike()):
					accumulated_score+=10
					accumulated_score += self.get_value_of_two_throws_after_frame(i)
				elif(frame.is_spare()):
					accumulated_score+=10
					accumulated_score += self.get_value_of__first_throw_after_frame(i)
				else:
					accumulated_score += frame.get_first_throw() + frame.get_second_throw()
			result.append(accumulated_score)
		return result

	def has_another_throw_to_make_in_game(self):
		return self.current_frame < 10

	def score(self, score):
		if self.has_another_throw_to_make_in_game():
			if not self.get_current_frame().is_done():
				self.get_current_frame().input_new_throw(score)
				if self.get_current_frame().is_done():
					self.current_frame += 1	

	def get_current_frame(self):
		return self.frames[self.current_frame]


def print_score_sheet(players):
	print(TABLE_HEADER)
	print(COLUMNS_HEADER)
	for player in players:
		player.print_score();


def all_players_done(players): #TODO improve with idiomatic solution?
	for player in players:
		if player.has_another_throw_to_make_in_game():
			return False
	return True

def get_score_input(player_name):
	input = raw_input("enter pin state for %s: " %(player_name))
	if input.isdigit():
		return int(input)
	else:
		return(get_score_input())

def run():
	num_players = int(raw_input("enter the number of players: "))
	players = []
	for i in range(1,num_players+1):
		new_player = Player(raw_input("enter the name of player "+str(i)+": "))
		players.append(new_player)
	while not all_players_done(players):
		for player in players:
			start_frame = player.get_current_frame()
			while player.has_another_throw_to_make_in_game() and start_frame == player.get_current_frame():
				player.score(get_score_input(player.get_name()))
		print_score_sheet(players)

def random_run():
	num_players = int(raw_input("enter the number of players: "))
	players = []
	for i in range(1,num_players+1):
		new_player = Player(raw_input("enter the name of player "+str(i)+": "))
		players.append(new_player)
	while not all_players_done(players):
		print("Round complete!")
		for player in players:
			start_frame = player.get_current_frame()
			while player.has_another_throw_to_make_in_game() and start_frame == player.get_current_frame():
				score = 10#random.randrange(0,11-start_frame.get_first_throw())
				player.score(score)

		print_score_sheet(players)


run()