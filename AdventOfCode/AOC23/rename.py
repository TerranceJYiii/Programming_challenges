import os

# Function to rename multiple files
def main():
	i = 0
	path="C:/Users/USER/Downloads/Y5 SEM1 2024/MasterProject/Chess_Piece_Image/Mix_Chess/"
	for filename in os.listdir(path):
		my_dest ="M" + str(i) + ".jpg"
		my_source =path + filename
		my_dest =path + my_dest
		os.rename(my_source, my_dest)
		i += 1
# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()