from PIL import Image

def image(nom_image):
    img = Image.open(nom_image)
    largeur = img.width
    hauteur = img.height
    return img,largeur,hauteur


def reset(largeur,hauteur): #rend toute les valeur rgb pair (represente le zero)
    for y in range(hauteur):
        for x in range(largeur):
            L=img.getpixel((x,y))
            r=int(L[0])
            v=int(L[1])
            b=int(L[2])

            if r%2==1:
                new_r=r-1
            else:
                new_r=r
            if v%2==1:
                new_v=v-1
            else:
                new_v=v
            if b%2==1:
                new_b=b-1
            else:
                new_b=b

            img.putpixel( (x,y) , (new_r,new_v,new_b) )


def changement(dico,r,v,b,x,y):
    img.putpixel( (x,y) , (r+dico[0][0],v+dico[0][1],b+dico[0][2]) )
    x+=1
    img.putpixel( (x,y) , (r+dico[1][0],v+dico[1][1],b+dico[1][2]) )



def convertisseur(hauteur,largeur):
    message=input("inserer le message:")
    fin=len(message)-1
    letre=0
    stop=False
    global x
    global y
    y=0
    while y <hauteur and stop==False:
        x=0
        if stop==False:
            while x <largeur and stop==False:
                L=img.getpixel((x,y))
                r=int(L[0])
                v=int(L[1])
                b=int(L[2])
                for k in dico.keys():
                    if message[letre]==k:
                        changement(dico[k],r,v,b,x,y)
                
                
                
                if letre >=fin:
                    stop=True
                else:
                    letre=letre+1
                x+=2
        
        y+=1



dico={
    "a":[[1,0,0],[0,0,0]],
    "b":[[1,1,0],[0,0,0]],
    "c":[[0,1,0],[0,0,0]],
    "d":[[0,1,1],[0,0,0]],
    "e":[[1,1,1],[0,0,0]],
    "f":[[0,0,0],[1,0,0]],
    "g":[[1,0,0],[1,0,0]],
    "h":[[1,1,0],[1,0,0]],
    "i":[[0,1,0],[1,0,0]],
    "j":[[1,1,1],[1,0,0]],
    "k":[[0,0,0],[1,1,0]],
    "l":[[1,0,0],[1,1,0]],
    "m":[[1,1,0],[1,1,0]],
    "n":[[0,1,0],[1,1,0]],
    "o":[[1,1,1],[1,1,0]],
    "p":[[0,0,0],[0,1,0]],
    "q":[[1,0,0],[0,1,0]],
    "r":[[1,1,0],[0,1,0]],
    "s":[[0,1,0],[0,1,0]],
    "t":[[1,1,1],[0,1,0]],
    "u":[[1,0,0],[0,1,1]],
    "v":[[1,1,0],[0,1,1]],
    "w":[[0,0,0],[1,1,1]],
    "x":[[0,1,0],[0,1,1]],
    "y":[[1,1,1],[0,1,1]],
    "z":[[1,0,1],[0,1,1]],
    " ":[[0,0,0],[0,0,0]]
    }



img,largeur,hauteur=image("frog.png")
reset(largeur,hauteur)
convertisseur(largeur,hauteur)

img.show()
print("fini")

#to see the valeur of pixel (for debug lol)
#for ytest in range(2):
#    for xtest in range(128):
#        t=img.getpixel((xtest,ytest))
#        print(t[0],t[1],t[2])