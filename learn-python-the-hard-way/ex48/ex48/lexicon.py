def scan(sentence):
	words = sentence.split(' ')
	return [token_word(word) for word in words]
	
def token_word(word):
	token = get_token(word)
	if token == 'number':
		word = int(word)
		
	return (token, word)
	
tokens_words = {
	'direction': ['north', 'east', 'south'],
	'verb': ['go', 'kill', 'eat'],
	'stop': ['the', 'in', 'of'],
	'noun': ['bear', 'princess']
}	

def get_token(word):
	for token, words in tokens_words.items():
		if word in words:
			return token
	
	try:
		int(word)
		return 'number'
	except ValueError:
		return 'error'