import sys

# write a function to take the entire contents of a file and load it into a variable
def get_book_text(path_to_file):
	book_contents = None
	with open(path_to_file) as f:
		book_contents = f.read()
	return book_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
		
	num_words=0
	get_text_as_string, path_to_file = "", ""
	char_dist, sorted_dict = {},{}

	path_to_file = sys.argv[1]
	print(f"path to file: {path_to_file}")
	# count the number of words in a file
	from stats import count_words # import function from stats.py file
	get_text_as_string = get_book_text(path_to_file) 
	num_words = count_words(get_text_as_string)
	
	# count the number of times each character appears in a file
	from stats import count_characters # import function from stats.py file
	char_dist = count_characters(get_text_as_string) # run count_characters function
	# print the character distribution 
	
	#reformat and sort the char_dist into a dictionary of dictionaries
	from stats import sort_dictionary # import function from stats.py file
	sorted_dict = sort_dictionary(char_dist)

	#print out all the results in the required format
	from stats import print_dict # import function from stats.py file
	print_dict(path_to_file, num_words, sorted_dict)



main()
