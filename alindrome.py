Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # function to check string is 
# palindrome or not 
def isPalindrome(str): 

	# Run loop from 0 to len/2 
	for i in xrange(0, len(str)/2): 
		if str[i] != str[len(str)-i-1]: 
			return False
	return True

# main function 
s = "malayalam"
ans = isPalindrome(s) 

if (ans): 
	print("Yes") 
else: 
	print("No") 
