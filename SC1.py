#Name:
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
codplayerdict = {
    'enemy1':{
        'name' : 'clown',
        'health' : 180,
        'damage' : 100
    },
    'enemy2':{
        'name' : 'carlos',
        'health' : 170,
        'damage' : 130
    },
    'enemy3':{
        'name' : 'doc',
        'health' : 190,
        'damage' : 125
    },
    'enemy4':{
        'name' : 'castle',
        'health' : 130,
        'damage' : 110
    },
    'enemy5':{
        'name' : 'art',
        'health' : 160,
        'damage' : 150
    },
}

codplayerdict['enemy1']['damage']=int(input('change clown damage'))
print(codplayerdict['enemy1'])
codplayerdict['enemy2']['damage']=int(input('change carlos damage'))
print(codplayerdict['enemy2'])
codplayerdict['enemy3']['damage']=int(input('change doc damage'))
print(codplayerdict['enemy3'])
codplayerdict['enemy4']['damage']=int(input('change castle damage'))
print(codplayerdict['enemy4'])
codplayerdict['enemy5']['damage']=int(input('change art damage'))
print(codplayerdict['enemy5'])