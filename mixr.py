import random

adjs  = open('adjs.txt').read().splitlines()
nouns = open('nouns.txt').read().splitlines()

base_spirit = ['Whiskey','Rum','Vodka','Gin','Tequila','Brandy','Scotch']
mixers      = ['Kahlua','Tonic','Coke','Triple Sec','Grenadine',"Bailey's","OJ",'Grapefruit Juice','Cranberry Juice']
garnish     = ['Lime','Lemon','Orange','Grapefruit','Pineapple','Mango']
syrup       = ['Simple Syrup','Honey Syrup','Agave Syrup']

title = 'The ' + random.choice(adjs).title() + ' ' +random.choice(nouns).title()
base = random.choice(base_spirit)
mix = random.choice(mixers)
garn = random.choice(garnish)
syr = random.choice(syrup)

num_dashes = random.randint(2,3)

print ''
print 'Introducing...'
print title
print ''
print 'Ingredients:'
print '# ' + str(random.randint(1,3)) + ' oz ' + base
print '# ' + str(random.randint(2,4)) + ' oz ' + mix
print '# ' + str(random.randint(1,2)) + ' slices ' + garn
print '# ' + str(num_dashes) + ' dashes ' + syr

print ''

print "Grab your " + base + ", and add a bit of " + mix + ".\nGarnish with a healthy slice of " + garn + " and add " + str(num_dashes)+ " dashes of " + syr + ".\n\nEnjoy!"
