print("""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
      
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
      
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
      
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2

4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
      
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
      
The file, Euler_54.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?""")


# 0 High Card: Highest value card.
# 1 One Pair: 4
# 2 Two Pairs: 3
# 3 Three of a Kind: 3
# 4 Straight: 5, S
# 5 Flush: 5, F
# 6 Full House: 2
# 7 Four of a Kind: 2
# 8 Straight Flush: 5, S, F
# 9 Royal Flush: 5, S, F



value = "23456789TJQKA" # 8 = RF

def sort_num(num):
    val = [value.index(each) for each in num]
    val = sorted(val, reverse=True)
    return [value[i] for i in val]

def flush_check(num):
	hand = sort_num(num)
	hand.reverse()
	# print(hand)
	hand = "".join(hand)
	
	if hand in value:
		# print(hand)
		return value.index(hand) + 1
	else:
		return False

def check_cards(player):
	num = [each[0] for each in player]
	suit = set([each[1] for each in player])
    
	if len(suit) == 1:
		Flush = True
	else:
		Flush = False

	# print(sort_num(num))
	s_num = set(num)
	l = len(s_num)

	if l == 2:
		x = num.count(num[0])
		if x == 1 or x == 4:
			# pass # TODO 7
			for each in s_num:
				if num.count(each) == 4:
					s_num.remove(each)	
					return 7,  [each] + sort_num(s_num)
		
		else:
			# pass # TODO 6
			for each in s_num:
				if num.count(each) == 3:
					s_num.remove(each)	
					return 6,  [each] + sort_num(s_num)

	elif l == 3:
		for each in num:
			if num.count(each) == 1:
				pass
			elif num.count(each) == 2:
				# pass # TODO 2
				for each in s_num:
					if num.count(each) == 1:
						s_num.remove(each)	
						return 2, sort_num(s_num) + [each]
			
			else:
				# pass # TODO 3
				for each in s_num:
					if num.count(each) == 3:
						s_num.remove(each)	
						return 3, [each] + sort_num(s_num)

	elif l == 4:
		# pass # TODO 1
		for each in s_num:
			if num.count(each) == 2:
				s_num.remove(each)	
				return 1, [each] + sort_num(s_num)
	
	else:
		Straight = flush_check(num)
		if not Straight: 
			if not Flush:
				# pass # TODO 0
				return 0, sort_num(num)


			else:
				# pass # TODO 5
				return 5, sort_num(num)

		else:
			# print("Straight" , Straight)
			if Flush:
				if Straight == 9:
					# pass # TODO 9
					return 9, []

				else:
					# pass # TODO 8
					return 8, sort_num(num)

			else:
				# pass # TODO 4
				print(sort_num(num))
				return 4, sort_num(num)






with open("Euler_54.txt") as file:
    lines = file.readlines()

p1_win = 0

for line in lines:
	card = line.split()
	p1 = card[:5]
	p2 = card[-5:]
	rank1, nums1 = check_cards(p1)
	rank2, nums2 = check_cards(p2)
	
	# print()
	# check = 4
	# if rank1 == check or rank2 == check: 
	# 	print(p1, rank1, nums1)
	# 	print(p2, rank2, nums2)
	# 	print()
	
	if rank1 < rank2:
		pass
	elif rank1 > rank2:
		p1_win += 1
		# print("p1 win")
	else:
		for i in range(len(nums1)):
			n1 = value.index(nums1[i])
			n2 = value.index(nums2[i])
			if n1 > n2:
				p1_win += 1		
				# print("p1 win")
				break
			elif n1 < n2:
				break

print("Player 1 wins: ", p1_win)