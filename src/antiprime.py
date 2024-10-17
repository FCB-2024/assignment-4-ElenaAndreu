import sys
## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	i = 1
	c = 0

	while i <= x:
		if x % i == 0:
			c = c + 1
		i = i + 1
	y = x - 1
	b = 0
	while y >= 1 and b < c:
		a = 1
		b = 0
		while a <= y:
			if y % a == 0:
				b = b + 1
			a = a + 1
		y = y - 1
	if b >= c:
		return "not anti-prime"

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	return "anti-prime"

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT

	#print(main(x))
	if len(sys.argv) == 2:
		x = int(sys.argv[1])
		if x > 0:
			print(main(x))
