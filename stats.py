	# count the number of words in a string and return the number
def count_words(text_as_string):
	word_count = len(text_as_string.split())
	print(f"Found {word_count} total words")
	return word_count

	# count the number of words in a string and return the number
def count_char(text_as_string):
	char_count = len(list(text_as_string))
	print(f"Found {char_count} total characters")
	return char_count

# count the number of times each character appears in a string and build it as a dictionary
# e.g. {'p': 6121, 'r': 20818, 'o': 25225, ...  
def count_characters(text_as_string):
	count = 0
	char_count = {}
	text_as_lower = text_as_string.lower()
	# build a dictionary of character distribution using the characters from the set of unique characters as the index.
	for i in range (0, len(list(text_as_lower))):
		if (text_as_lower[i] in char_count) :
			# print(f"current count of {text_as_lower[i]} is {char_count[text_as_lower[i]]}") # debug
			count = char_count[text_as_lower[i]] + 1
			char_count[text_as_lower[i]] = count
			# print(f"{text_as_lower[i]} - incrememnting - {char_count[text_as_lower[i]]}") # debug
		else:	
			char_count[text_as_lower[i]] = 1
			# print(f"adding {text_as_lower[i]} to dictionary") # debug
	# return the dictionary
	print(char_count)
	return char_count

def sort_on(keys):
	return keys["num"]


def sort_dictionary(dictionary):
	# take 'dictionary' and convert to a list[] of dictionaries{}
	unsorted_dictionary_list = list(dictionary.items())
	
	# convert old dictionaries from {'character': number} to {"char": 'character', "num": number})
	new_format_dict=[]
	for key, value in unsorted_dictionary_list :
			new_format_dict.append({"char": key, "num": value})

	# sort the list of dictionaries in reverse (greatest to least) and using the key "num"
	new_format_dict.sort(reverse=True, key=sort_on)

	# return the sorted dictionary of dictionaries
	return new_format_dict
	
def	print_dict(path_to_book,word_count,dict_to_print) :
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_book}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	# print out the alphabetical character and their count
	for dict in dict_to_print :
		if dict["char"].isalpha():
			print(f"{dict['char']}: {dict['num']}")
	print("============= END ===============")