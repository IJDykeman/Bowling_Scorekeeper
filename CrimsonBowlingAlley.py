"""
Bowling Score Keeper

This module takes input from bowling alley hardware, and update and displays
player scores accordingly

This module was written by Isaac Dykeman
"""

import random
WIDTH_OF_NAME_COLUMN = 12
WIDTH_OF_TOTAL_COLUMN = 9
FRAMES_PER_GAME = 10
MAX_THROWS_PER_GAME = 2*9+3 # nine _frames of 2 balls, and a frame of 2 or 3 balls
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
		Returns the score (int) of a throw at the given index.

		Args:
			index (int): The index of the score to return.			
		"""
		if index<len(self._throws):
			return self._throws[index]
		return 0	
			
	def get_first_throw(self):
		"""
		Returns the score (int) of the first throw of the frame	.	
		"""
		return self.get_throw(0)

	def get_second_throw(self):
		"""
		Returns the score (int) of the second throw of the frame.		
		"""
		return self.get_throw(1)

	def get_third_throw(self):
		"""
		Returns the score (int) of the third throw of the frame.	
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
			if self.get_second_throw() == 10:
				second_symbol = "X"
			if self.get_third_throw() == 10:
				third_symbol = "X"
			return "[%s,%s,%s]" % (first_symbol, second_symbol, third_symbol)

	def is_strike(self):
		"""
		Returns whether the frame is a strike: True if the first throw scored 
		10, else, False
		"""
		return self.get_first_throw()==10

	def is_spare(self):
		"""
		Returns whether the frame is a spare: True if the sum of the first and
		second throw scores is 10 and the frame is not a strike, else, False.
		"""
		sums_to_10 = self.get_first_throw() + self.get_second_throw() == 10
		return sums_to_10 and not self.is_strike()

	def is_done(self):
		"""
		Returns True if there is another ball to be thrown in this frame, else,
		returns False.
		"""
		if not self.is_three_throw_frame():
			return len(self._throws) >= self._num_throws or self.is_strike()
		else: 
			# is a two ball frame
			if self.is_strike() and self.num_throws_taken()<self._num_throws:
				# strike results in two extra throws on the third frame
				return False
			elif self.is_spare() and self.num_throws_taken()==2:
				# spare results in one extra shot
				return False
			else:
				#when not a spare or a strike, the last frame has two throws
				return self.num_throws_taken()>=2

	def input_new_throw(self,score):
		"""
		Adds the players score on a throw to this frame.

		Args:
			score (int): The number of pins the player knocked down on this
				throw.  Be cautious: this is not necesarilly the same as the
				total number of pins that are down at this time.
		"""
		assert not self.is_done() # a full frame cannot accept more thows
		self._throws.append(score)

	def num_throws_taken(self):
		"""
		Returns (int) the number of thows taken in this frame so far.
		"""
		return len(self._throws)

	def is_three_throw_frame(self):
		"""
		Returns True if this is the final frame, which has a max of three
		throws.
		"""
		return self._num_throws == 3

	def get_num_throws(self):
		"""
		Returns (int) the max number of throws possible in this frame.
		"""
		return self._num_throws

	def get_score_formatted_for_table(self,score):
		"""
		Returns (string) the textual representation of the total score of the
		game at this frame.  The length of the result string is trimmed so that
		it does not warp the formatting of the table when it is printed.

		Args:
			score (int): The score that should be displayed in this frame of
			the table.
		"""
		width_of_table_column = 2 + self._num_throws * 2 - 1
		left_justified_score = str(score).ljust(width_of_table_column)
		return left_justified_score[:width_of_table_column]		


class Player:
	"""
	Represents a single player of a bowling game.  Contains that player's score
	data and name, and tracks which frame the player is currently on

	Args:
		name (string): The name of the player.

	Attributes:
		_name (string): Player's name.
		_throws (list of Frame): Player's frames
		_current_frame (int): The index of the frame the player is on.
	"""
	def __init__(self,name):
		self._name = name
		self._frames = []
		self._current_frame = 0
		for dummy_idx in range(FRAMES_PER_GAME-1):
			self._frames.append(Frame(2))
		self._frames.append(Frame(3))

	def get_name(self):
		"""
		Returns (string) the player's name.
		"""
		return self._name

	def get_name_formatted_for_table(self):
		"""
		Returns (string) this players name limitted in length to the width of 
		the Name column in the score chart.  This way, names cannot destort
		the spacing of the table.
		"""
		return self._name.ljust(WIDTH_OF_NAME_COLUMN)[:WIDTH_OF_NAME_COLUMN]
	def get_total_score_formatted_for_table(self, score):
		"""
		Returns (string) this score limitted in length to the width of the 
		Total column in the score chart.  This way, names cannot destort the
		spacing of the table.
		"""
		return str(score).ljust(WIDTH_OF_TOTAL_COLUMN)[:WIDTH_OF_TOTAL_COLUMN]

	def print_score(self):
		"""
		Prints the lines of the score table that describe this player's scores.
		"""
		print(PLAYER_ROW_DIVIDER)

		raw_scores_line = []
		raw_scores_line.append("|%s|" % (self.get_name_formatted_for_table()))
		for i in range(FRAMES_PER_GAME):
			raw_scores_line.append(self._frames[i].get_throws_score_string())
			raw_scores_line.append("|")
		raw_scores_line.append("         |")
		print(''.join(raw_scores_line))

		accumulated_scores = self.get_score_list()
		accumulated_score_line = []
		accumulated_score_line.append("|            |")
		for i,frame in enumerate(self._frames):
			score = str(accumulated_scores[i])
			formatted_score = frame.get_score_formatted_for_table(score) + "|"
			accumulated_score_line.append(formatted_score)
		total_score = max(accumulated_scores)
		formatted_total = self.get_total_score_formatted_for_table(total_score)
		accumulated_score_line.append(formatted_total)
		accumulated_score_line.append("|")
		print(''.join(accumulated_score_line))


	def get_value_of_two_throws_after_strike_on_frame(self, frame_index): 
		"""
		Returns (int) the sum of the scores of the two throws the player makes
		after scoring a strike on the frame at frame_index.

		Args:
			frame_index (int): The index of the frame on which the strike was
				scored.
		"""
		return self.get_score_of__first_throw_after_frame(frame_index) \
			+ self.get_score_of__second_throw_after_strike_on_frame(frame_index)

	def get_score_of__first_throw_after_frame(self, frame_index):
		"""
		Returns (int) the value of the first throw made after the completion
		of the frame at frame_index.

		Args:
			frame_index (int): The index of the frame before the throw whose
				value should be returned.
		"""
		if self._frames[frame_index].is_three_throw_frame():
			return self._frames[frame_index].get_third_throw()
		else:
			return self._frames[frame_index+1].get_first_throw()

	def get_score_of__second_throw_after_strike_on_frame(self, frame_index):
		"""
		Returns (int) the values of the second throw made after the completion
		of the frame at frame_index.  This is only used when calculating the
		value of a strike.

		Args:
			frame_index(int):  The index of the frame with the strike, two
				throws after which the throw whose score is returned was made.
		"""
		if self._frames[frame_index].is_three_throw_frame():
			return self._frames[frame_index].get_third_throw()
		else:
			if not self._frames[frame_index+1].is_strike():
				# A strike with a strike after it returns the sum of the scores
				# (20) of those two throws, plus the score of the next throw.
				return self._frames[frame_index+1].get_second_throw()
			else:
				return self.get_score_of__first_throw_after_frame(frame_index+1)

	def get_score_list(self):
		"""
		Returns (list of int) a list of the scores for the game to be displayed
		on each frame of the score table.  There is one element in the list per
		frame of the game.  If the game is not complete, the list contains the 
		total score so far in the game for all incomplete frames.
		"""
		accumulated_score=0
		result = []
		for i, frame in enumerate(self._frames):
			if frame.is_three_throw_frame():
				accumulated_score += frame.get_first_throw()
				accumulated_score += frame.get_second_throw()
				accumulated_score += frame.get_third_throw()
			else:
				if(frame.is_strike()):
					accumulated_score += 10
					accumulated_score += self.get_value_of_two_throws_after_strike_on_frame(i)
				elif(frame.is_spare()):
					accumulated_score += 10
					accumulated_score += self.get_score_of__first_throw_after_frame(i)
				else:
					accumulated_score += frame.get_first_throw() + frame.get_second_throw()
			result.append(accumulated_score)
		return result

	def has_another_throw_to_make_in_game(self):
		"""
		Returns (boolean) True if the player must make another throw before the
		end of the game, else, returns False.
		"""
		return self._current_frame < 10

	def score(self, score):
		"""
		Handles the new score information by adding the given number of pins
		the palyer knocked down with a throw to the frame currently being
		played.  

		Args:
			score (int): The number of pins the player knocked down with her
				latest throw.
		"""
		if self.has_another_throw_to_make_in_game():
			if not self.get_current_frame().is_done():
				self.get_current_frame().input_new_throw(score)
				if self.get_current_frame().is_done():
					self._current_frame += 1	

	def get_current_frame(self):
		"""
		Returns (Frame) the frame the player is currently on, that is, the
		first frame in this player's game which is not complete.
		"""
		return self._frames[self._current_frame]


def print_score_sheet(players):
	"""
	Prints the whole score table for the game so far.
	"""
	print(TABLE_HEADER)
	print(COLUMNS_HEADER)
	for player in players:
		player.print_score();


def all_players_done(players):
	"""
	Returns (boolean) True if all the players in the game have made all of
	their throws for this game, else, returns False.
	"""
	for player in players:
		if player.has_another_throw_to_make_in_game():
			return False
	return True

'''def get_score_input(player_name):

	input = raw_input("enter pin state for %s: " %(player_name))
	if input.isdigit():
		return int(input)
	else:
		return(get_score_input(player_name))'''

def get_num_pins_down(player_name):
	input = raw_input("enter pin state for %s: " %(player_name))
	input = input.upper();
	if len(input)!=10:
		print ("invalid pin state string")
		return get_num_pins_down(player_name)
	return input.count('F')

def play_one_frame(player):
	start_frame = player.get_current_frame()
	num_pins_down = 0
	while player.has_another_throw_to_make_in_game() and start_frame == player.get_current_frame():
		num_pins_down_on_this_throw = get_num_pins_down(player.get_name())
		player.score(num_pins_down_on_this_throw-num_pins_down)
		num_pins_down = num_pins_down_on_this_throw


def run():
	num_players = int(raw_input("enter the number of players: "))
	players = []
	for i in range(1,num_players+1):
		new_player = Player(raw_input("enter the name of player "+str(i)+": "))
		players.append(new_player)
	while not all_players_done(players):
		for player in players:
			play_one_frame(player)
		print_score_sheet(players)

'''def random_run():
	num_players = int(raw_input("enter the number of players: "))
	players = []
	for i in range(1,num_players+1):
		new_player = Player(raw_input("enter the name of player "+str(i)+": "))
		players.append(new_player)
	while not all_players_done(players):
		print("Round complete!")
		for player in players:
			play_one_frame(player)

		print_score_sheet(players)'''


run()