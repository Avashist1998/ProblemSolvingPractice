"""LC: Valid Palendrome"""



def isPalindrome(s: str) -> bool:
	"""Is s an palindrome
	Args:
		s: string
	Returns:
		bool: True if is palendrome or false
	"""
	
	def isAlphaNumeric(ch: str) -> bool:
		if (ord("0") <= ord(ch.lower()) and ord(ch.lower()) <= ord("9")) or (ord("a") <= ord(ch.lower()) and ord(ch.lower()) <= ord("z")):
			return True
		return False

	
	l, r = 0, len(s)-1

	while r-l > 0:
		if isAlphaNumeric(s[l]) and isAlphaNumeric(s[r]):
			if s[l].lower() != s[r].lower():
				return False
			else:
				l += 1
				r += -1
		else:
			if not isAlphaNumeric(s[l]):
				l += 1
			if not isAlphaNumeric(s[r]):
				r += -1
	
	return True
