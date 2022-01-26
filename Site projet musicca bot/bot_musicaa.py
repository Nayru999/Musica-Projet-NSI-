import pyautogui,time
jojo=['j','v','v','b','n','b','v','f','v','b','j' """clic""",'(','f','v','b','v','f',';',',','j']
sil=[')','f','v','v','f','v','b','b','b','j','b','v','b','v','p','v','j','j','b','v','b','b','p','f',',',',','j','b','j','b','v','click si',';','v','click si',';','v','v','f','v','b','j','v']
moz=['u','u','u','r','y','t','e','e','t','y','r','r','y','t','e']
def press(touche):

    
    pyautogui.keyDown(touche)
    pyautogui.keyUp(touche)
    
    
    
def click(x,y):
    
    pyautogui.click(x,y)
    
    pass
def note_vers_touche(note):
    dico={
    "do-":'w',
    "doré-":'s',
    "ré-":'x',
    "rémi-":'d',
    "mi-":'c',
    "fa-":'a',
    "fasol-":'é',
    "sol-":'z',
    "solla-":'"',
    "la-":'e',
    "lasi-":"'",
    "si-":'r',
    "do":'t',
    "doré":'-',
    "ré":'y',
    "rémi":'è',
    "mi":'u',
    "fa":'i',
    "fasol":'ç',
    "sol":'o',
    "solla":'à',
    "la":'p',
    "lasi":'=',
    "si":')',
    "do+":'^',
    "doré+":'f',
    "ré+":'v',
    "rémi+":'g',
    "mi+":'b',
    "fa+":'n',
    "fasol+":'j',
    "sol+":',',
    "solla+":'k',
    "la+":';',
    "lasi+":'l'
   }
    return dico[note]

def piano(note):
    touche = note_vers_touche(note)
    press(touche)
    
click(1097,512)


while len(jojo)!=0 :
    for i in range(11):
        if len(jojo)!=0:
            note = jojo.pop(0)
            press(note)
click(1704,754)

time.sleep(3)


while len(sil)!=0 :
    for i in range(11):
        if len(sil)!=0:
            note = sil.pop(0)
            press(note)
click(1704,754)



time.sleep(3)


while len(moz)!=0 :
    for i in range(11):
        if len(moz)!=0:
            note = moz.pop(0)
            press(note)

