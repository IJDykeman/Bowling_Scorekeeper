import random # needed to test the program with random scores
width_of_name_column = 12
frames_per_game = 10




class Player:
	def __init__(self,new_name):
		self.name = new_name
		self.scores = [] # list of the number of pins the player knocks down on each throw
	def get_score_at_ball(self,ball_idx):
		if(len(self.scores)>ball_idx):
			if ball_idx%2==0 and self.scores[ball_idx]==10:
				return "X" # X to indicate strike
			elif (ball_idx-1)%2==0 and self.scores[ball_idx-1]==10:
				return " " # if a strike was scored on the first ball of the frame, the second ball space is blank
			elif (ball_idx-1)%2==0 and self.scores[ball_idx]+self.scores[ball_idx-1]==10:
				return "/" # / to indicate spare
			return str(self.scores[ball_idx])
		return"-"
	def print_score(self):
		'''
		prints the line of the score table that describes this player's scores
		'''
		print("------------------------------------------------------------------------------------")

		raw_scores_line = "|            |"
		for i in range(frames_per_game):
			raw_scores_line = raw_scores_line+"["+self.get_score_at_ball(i*2)+","+self.get_score_at_ball(i*2+1)+"]|"
		raw_scores_line = raw_scores_line+"         |"

		print(raw_scores_line)
		print("|"+self.get_name_formatted_for_table()+"|     |     |     |     |     |     |     |     |     |     |         |")
	def get_name_formatted_for_table(self):
		'''
		Gets this players name limitted to the width of the Name field in the score chart.  
		This way, names cannot destort the spacing of the table.
		'''
		return self.name.ljust(width_of_name_column)[:width_of_name_column]#adds trailing spaces or truncates string to fit into table exactly
	def score(self, score):
		self.scores.append(score)
		#if(score == 10):
		#		self.scores.append(0) # if the player strikes, they do not throw a second ball for that frame



def print_score_sheet():
	print("==================================Current=Scores====================================")
	print("|    Name    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  Total  |")
	for player in players:
		player.print_score();

num_players = int(raw_input("enter the number of players: "))
players = []


for i in range(1,num_players+1):
	new_player = Player(raw_input("enter the name of player "+str(i)+": "))
	players.append(new_player)
	new_player.print_score();
	for dummy_idx in range(20):
		total_frame_score = int(random.randrange(0,11))
		first_score = 10
		if(total_frame_score != 0 and random.random()<.9):
			first_score = total_frame_score-int(random.randrange(0,total_frame_score))
		second_score = total_frame_score-first_score
		new_player.score(first_score)
		new_player.score(second_score)




print_score_sheet()


