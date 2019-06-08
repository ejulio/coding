class ParserError(Exception):
	pass
	
class Sentence(object):
	
	def __init__(self, subject, verb, obj):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]
		
def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	
	return None

def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting:
			return word
	
	return None
	
def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_list)
		