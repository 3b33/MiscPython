import random
import os
import re

# add families = same surname to some folks with logical gender / age distribution

# abcdefghijklmnopqrstuvwxyz (åäö) (ü)

v = 'aeiouy' #vowels
k = 'bcdfghjklmnpqrstvwxz' #consonants

# these are not used anymore, check end
fnt = ['kvvkv','vkkv','vvkv','kvkkvvk','kvkkv'] # first name templates
snt = ['kvkkvk','kvvkvkv','vkvkvk','kvkvvkvkv','kvkkvkv'] # surname templates

# lv? 
banned_combos ={
'a':'eoy',
'b':'cdfgjmnpqvwxz',
'c':'bcfgjkmnpqstvwxyz',
'd':'bcfgjtxz',
'e':'auojv', # a?
'f':'bcdfghjmnqsvwxyz',
'g':'bcfgj',
'h':'fhjkmnprsvw', # m?
'i':'aejouy', # should prevent ia and io only in the start of a name.
'j':'', # check v
'k':'bcfghjlmnpqtvwxz', # t?
'l':'bnqx',
'm':'fhjklnprstvwv',
'n':'hmqvwxz',
'o':'aeuy',
'p':'bfghjkmnqvwx',
'q':'gjkmnqtvwxyz',
'r':'rx',
's':'hjlrxz',
't':'bdgjknpqx',
'u':'aejvy',
'v':'', # v prevented as the first letter in a double consonant
'w':'bcfgjkmpqtvwxz',
'x':'gjkmnqrsvxz',
'y':'abdegjqiuovxyz',
'z':'bcdfgjqvwyxz',
}

banned_ends = 'bcdfghjklmpqrtvwxz'

rare_letters = { # this defines the propability % of these characters
'b':10,
'c':8,
'd':15,
'f':8,
'g':10,
'j':60,
'y':2,
'q':1,
'w':3,
'x':1,
'z':2,
}

def r(x):
	if x:
		return x[random.randint(0,len(x)-1)]
	return ''

def gibberish(template): # makes a single name, ie. 'Bobba'. Takes vowel+consonant template as input, ie. 'kvkkv'
	name = ''
	for i in range(0,(len(template))):
		ic = template[i]
		if ic != ' ':
			vk = eval(ic) # eliminate bad characters from the full vowel or consonant string. ie. eval(k) = actual k variable (consonants).
			if i < len(template)-1:
				if ic == template[i+1] == 'k': # special rule if double consonants: first one cannot be 'v' or 'j'
					vk = vk.replace('v','')
					vk = vk.replace('j','')
			#print(name, ic, vk)
			if len(name) > 0:
				if name[-1] != ' ':
					# remove unwanted letters using banned combinations list
					for x in vk: 
						if x in banned_combos[nl]: vk = vk.replace(x,'')
					# if this is the last character of the name, remove bad end characters from possible options.
					if i == len(template)-1: 
						for x in banned_ends:
							vk = vk.replace(x,'')
			#rarity check
			rares = set(list(vk)).intersection(rare_letters.keys())
			if bool(rares): # is bool needed here?
				for rare in rares:
					if random.randint(0,100) > rare_letters[rare]:
						vk = vk.replace(rare,'')
			if vk != '':
				if i == 0 and ic == template[i+1] == 'v': # special case: If double vocals in the start of the name, don't start with 'i'.
					vk = vk.replace('i','')
				nl = r(vk)
				

			if nl == '':
				nl = 'ü'
			name += nl
		else:
			name += ' '

	return name

def consVocals(nameLenMin,nameLenMax,bias):
	doubleVocals = False
	doubleConsonants = False
	CVS = '' # consonant vocal string (ie. 'kvvkv')
	if random.random() < 0.5: CVS += 'k'
	else: CVS += 'v'
	if CVS == 'k': CVS += 'v' # kk... is a bad start
	else:
		if random.random() < 0.8: CVS += 'k' # double vocal start is often not the best
		else: CVS += 'v'
	nameLen = random.randint(nameLenMin,nameLenMax)
	while 1/(abs(nameLen-bias)+1) > random.random()*2: # first try for bias
		nameLen = random.randint(nameLenMin,nameLenMax)

	for i in range(2,nameLen):
		if 'kk' in CVS: doubleConsonants = True
		if 'vv' in CVS: doubleVocals = True
		if i == nameLen-1 and CVS[-1] == 'k': CVS += 'v' # ...kk is a bad ending
		else:
			if CVS[-2] == CVS[-1] == 'k': CVS += 'v'
			elif CVS[-2] == CVS[-1] == 'v': CVS += 'k'
			else:
				chance = 0.55 # chance for a consonant
				if CVS[-1] == 'v': 
					chance = .8 # restrict double vocals
					if doubleVocals: chance = 1 # only one set of double vocals permitted per name
				if CVS[-1] == 'k' and doubleConsonants: chance = .2 # only small chance of more than one set of double consonants
				if random.random() < chance: CVS += 'k'
				else: CVS += 'v'
	return CVS

def gibberName():
	midname = ''
	if random.randint(0,100) < 10: # PROPABILITY for a second name / title
		midname = ' '+gibberish(consVocals(2,5,2))
	newName = gibberish(consVocals(4,7,5))+midname+' '+gibberish(consVocals(6,11,6)) # maybe name lengths could have a bias? Random super long ones.
	newName = newName.title() # erkko -> Erkko
	return newName
	#names.append(gibberish(r(fnt))+midname+' '+gibberish(r(snt)))
	#print(newName)

names = []
for g in range(60):
	names.append(gibberName())

#for n in names:
	#print(n+'\n\n')

print()

# print names
nameCols = 2
for nameIndex in range(0,len(names)-(len(names)%nameCols),nameCols):
	nameRow = ''
	for nameColIndex in range(nameCols):
		nameRow += names[nameIndex+nameColIndex].ljust(25, ' ')
	print(nameRow)

print()

# print some gibberish sentences

# create some short words to repeat later
rep = []
for repeating in range(3):
	rep.append(gibberish(consVocals(2,3,2)))
# rep = ['###']

print('Repeating words: '+', '.join(rep)+'.\n')
text = ''
capitalize = True
nameGend = False # name generated
for sentence in range(20):
	repd = True # no repeating words as the first word
	# one sentence
	wordCount = random.randint(3,10)
	if wordCount > 7: wordCount = random.randint(3,10)
	for word in range(wordCount):
		if word == wordCount-1: repd = True # no repeating words as the last word
		repdToFalse = True
		nameGendToFalse = True
		addText = ''
		chooser = random.random()
		if chooser < .02:
			addText = gibberName()
			nameGend = True
			nameGendToFalse = False
		elif chooser < .04:
			addText = gibberish(consVocals(4,7,5)).title()
			nameGend = True
			nameGendToFalse = False
		elif chooser < .34 and not repd:
			addText = r(rep)
			repd = True
			repdToFalse = False
		else: addText = gibberish(consVocals(3,10,5))
		if capitalize:
			addText = addText.title()
			capitalize = False
		text += addText
		if repdToFalse: repd = False
		if nameGendToFalse: nameGend = False

		# add a space or a comma between words unless at last word of sentence.
		if word != wordCount-1:
			if random.random() < 0.9 or repd == True or word == wordCount-1: text += ' '
			else:
				text += ', '
				repd = True # no repeating words after a comma

	# ending of the sentence
	#while text[-1] == ' ' or text[-1] == ',': text = text[:-1]
	capitalize = True
	if random.random() < .8:
		text += '.'
	else:
		if random.random() < .4:
			text += '?'
		elif random.random() < .9: text += '!'
		else: text += ':'
		capitalize = True
	#if sentence % 2 != 0: text += '\n'
	text += ' '
	

print(text)
print()