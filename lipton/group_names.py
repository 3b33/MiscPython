import os
import random
import re
from googlesearch import search

# abcdefghijklmnopqrstuvwxyz (åäö) (ü)

v = 'aeiou' #vowels
k ='dghjklmnprstv'
#k = 'bcdfghjklmnpqrstvwxz' #consonants

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
'd':100,
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

def group_name(template): # makes a single name, ie. 'Bobba'. Takes vowel+consonant template as input, ie. 'kvkkv'
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
			if rares:
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

	return name.title()

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
		midname = ' '+group_name(consVocals(2,5,2))
	newName = group_name(consVocals(4,7,5))+midname+' '+group_name(consVocals(6,11,6)) # maybe name lengths could have a bias? Random super long ones.
	newName = newName.title() # erkko -> Erkko
	return newName
	#names.append(group_name(r(template))+midname+' '+group_name(r(snt)))
	#print(newName)

# template = ['kvvkv','vkkvk','kvkkvk','kvkvvk'] # name templates

# likeit
# kvkvvk
# nepton
# kvkkvk

templates = []
while len(templates) < 100:
	templates = templates + [consVocals(5,8,6)]
# print(templates)

# why did I want d or g??
# names = ''
# for g in templates:
# 	tempname = group_name(g)
# 	if 'g' in tempname or 'd' in tempname:
# 		# names += (group_name(g)+'\n')
# 		names += (tempname+'\n')

for structure in templates:
	name = group_name(structure)
	nameSearches = search(name, 5)
	nameSearchStr = ''
	for nameSearch in nameSearches:
		nameSearchStr += nameSearch
	if name not in nameSearchStr:
		print(name)

#for n in names:
	#print(n+'\n\n')
# pyperclip.copy(names)
# print('Copied to clipboard.')

# print names
# nameCols = 4
# for nameIndex in range(0,len(names)-(len(names)%nameCols),nameCols):
#	nameRow = ''
#	for nameColIndex in range(nameCols):
#		nameRow += names[nameIndex+nameColIndex].ljust(25, ' ')
#	print(nameRow)

