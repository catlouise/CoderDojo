import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]
print 'Type your question to get an answer'
print 'Type "end" or "quit" to stop playing' 
while True:
	print " "
	print "~~~~~~~~~~~~~~~~"
	print "~~~~~~MAGIC~~~~~"
	print "~~~~~~//\\~~~~~~"
	print "~~~~~//  \\~~~~~"
	print "~~~~// 8  \\~~~~"
	print "~~~//      \\~~~"
	print "~~-==========-~~"
	print "~~~~~~~~~~~~~~~~"
	print " "
	n = raw_input()
	if n.lower() == 'end' or n.lower() == 'quit':
		break
	else:
		print (random.choice(answers))
		
