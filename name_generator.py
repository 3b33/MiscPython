import random
import os
import re

# add families = same surname to some folks with logical gender / age distribution
# lower chance for double vocals / consonants? Why vv is still present?
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
'j':'ghjlmnstrq',
'k':'bcfghjlmnpqtvwxz', # t?
'l':'bnqx',
'm':'fhjklnprstvwv',
'n':'hmqvwxz',
'o':'aeuy',
'p':'bfhjkmnqvwx',
'q':'gjkmnqtvwxyz',
'r':'rx',
's':'hjlrxz',
't':'dgjknpqx',
'u':'aejvy',
'v':'bcdfghjklmnpqrstvwxz', # l? vv still present!
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

def name_maker(template): # makes a single name, ie. 'Bobba'. Takes vowel+consonant template as input, ie. 'kvkkv'
	name = ''
	for i in range(0,(len(template))):
		ic = template[i]
		if ic != ' ':
			vk = eval(ic) # focus on eliminating bad characters from the full vowel or consonant string. Why eval? What does this mean??
			if len(name) > 0:
				if name[-1] != ' ':
					# remove unwanted letters using banned combinations database
					for x in banned_combos[nl]: 
						vk = vk.replace(x,'')
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
				nl = r(vk) # what is going on here??
			if nl == '':
				nl = 'ü'
			name += nl
		else:
			name += ' '

	return name.title()

names = []

def consVocals(nameLenMin,nameLenMax):
    CVS = ''
    if random.random() < 0.5: CVS += 'k'
    else: CVS += 'v'
    if CVS == 'k': CVS += 'v' # kk... is a bad start
    else:
        if random.random() < 0.65: CVS += 'k'
        else: CVS += 'v'
    nameLen = random.randint(nameLenMin,nameLenMax)
    for i in range(2,nameLen):
        if i == nameLen-1 and CVS[-1] == 'k': CVS += 'v' # ...kk is a bad ending
        else:
            if CVS[-2] == CVS[-1] == 'k': CVS += 'v'
            elif CVS[-2] == CVS[-1] == 'v': CVS += 'k'
            else:
				chance = 0.55
				if CVS[-1] == 'v': chance = 0.7 # restrict double vocals
                if random.random() < chance: CVS += 'k'
                else: CVS += 'v'
    return CVS

for x in range(90):
    midname = ''
    if random.randint(0,100) < 10:
        midname = ' '+name_maker(consVocals(2,4))
    newName = name_maker(consVocals(4,6))+midname+' '+name_maker(consVocals(6,10))
    #names.append(name_maker(r(fnt))+midname+' '+name_maker(r(snt)))
    newName = newName.ljust(18, ' ') # https://thispointer.com/python-how-to-pad-strings-with-zero-space-or-some-other-character/
    names.append(newName)

for i in range(0,len(names),3):
    if i < len(names)-2:
        print('%s\t%s\t%s' % (names[i], names[i+1], names[i+2]))

