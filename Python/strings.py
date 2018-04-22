#strings can be written with single quotes('...') and double quotes("...")
single_quote = 'Hi! I\'m a string written in single quotes'  #as you have i've used escape character
#if i didn't use it will give me an error
#output:"Hi! I'm a string written in single quotes"
double_quote = "Hi! I'm a string written in double quotes"
#output:"Hi! I'm a string written in double quotes"

print('First line\n new line')  #here \n is used for new line
#output: First line
#        new line
print(r"Here i'm printing \n a raw line")   #here i'm using 'r' in starting
#this will print the result the way i have written the code which means here '\n' will not work
#output:Here i'm printing \n a raw line

# >>> 3*'hello'   #we can also use strings with numbers and can perform arithmetic operations
# 'hellohellohello'

print('''Here i'm using three
    quoted string so that
    i don't need to use new line
    ''')
# ouput: Here i'm using three
#     quoted string so that
#     i don't need to use new line

prefix = 'py'
prefix+ 'thon'
print(prefix)

# >>> prefix = 'py'
# >>> prefix+'thon'
# 'python'

#we can also use indexing to strings
#but we can't reassign a string because strings are immutable

#indexing starts from 0
# >>>word = "computer"
# >>> word[2]
# 'm'   returns the 
# >>> word[-1]
# 'r'
# >>> word[2:]
# 'mputer'
# >>> word[2:4]
# 'mp'
# >>> word[::2]
# 'cmue'
# >>> word[::-1]
# 'retupmoc'
# >>> word[::-2]
# 'rtpo'
