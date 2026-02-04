from PIL import Image

def image(nom_image):
    global img
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
    x=x+1
    img.putpixel( (x,y) , (r+dico[1][0],v+dico[1][1],b+dico[1][2]) )



def convertisseur(hauteur,largeur):
    message=input("inserer le message:")
    fin=len(message)-1
    letre=0
    stop=False
    global x
    global y
    y=0
    hauteur=hauteur
    largeur=largeur
    while y <=hauteur and stop==False:
        x=0
        if stop==False:
            while x <=largeur and stop==False:
                L=img.getpixel((x,y))
                r=int(L[0])
                v=int(L[1])
                b=int(L[2])
                if message[letre]==dico["a"]:
                    changement(dico["a",r,v,b,x,y])
                elif message[letre]==dico["b"]:
                    changement(dico["b",r,v,b,x,y])
                elif message[letre]==dico["c"]:
                    changement(dico["c",r,v,b,x,y])
                elif message[letre]==dico["d"]:
                    changement(dico["d",r,v,b,x,y])
                elif message[letre]==dico["e"]:
                    changement(dico["e",r,v,b,x,y])
                elif message[letre]==dico["f"]:
                    changement(dico["f",r,v,b,x,y])
                elif message[letre]==dico["g"]:
                    changement(dico["g",r,v,b,x,y])
                elif message[letre]==dico["h"]:
                    changement(dico["h",r,v,b,x,y])
                elif message[letre]==dico["i"]:
                    changement(dico["i",r,v,b,x,y])
                elif message[letre]==dico["j"]:
                    changement(dico["j",r,v,b,x,y])
                elif message[letre]==dico["k"]:
                    changement(dico["k",r,v,b,x,y])
                elif message[letre]==dico["l"]:
                    changement(dico["l",r,v,b,x,y])
                elif message[letre]==dico["m"]:
                    changement(dico["m",r,v,b,x,y])
                elif message[letre]==dico["n"]:
                    changement(dico["n",r,v,b,x,y])
                elif message[letre]==dico["o"]:
                    changement(dico["o",r,v,b,x,y])
                elif message[letre]==dico["p"]:
                    changement(dico["p",r,v,b,x,y])
                elif message[letre]==dico["q"]:
                    changement(dico["q",r,v,b,x,y])
                elif message[letre]==dico["r"]:
                    changement(dico["r",r,v,b,x,y])
                elif message[letre]==dico["s"]:
                    changement(dico["s",r,v,b,x,y])
                elif message[letre]==dico["t"]:
                    changement(dico["t",r,v,b,x,y])
                elif message[letre]==dico["u"]:
                    changement(dico["u",r,v,b,x,y])
                elif message[letre]==dico["v"]:
                    changement(dico["v",r,v,b,x,y])
                elif message[letre]==dico["w"]:
                    changement(dico["w",r,v,b,x,y])
                elif message[letre]==dico["x"]:
                    changement(dico["x",r,v,b,x,y])
                elif message[letre]==dico["y"]:
                    changement(dico["y",r,v,b,x,y])
                elif message[letre]==dico["z"]:
                    changement(dico["z",r,v,b,x,y])
                elif message[letre]==dico[" "]:
                    changement(dico[" ",r,v,b])
                
                
                if letre >=fin:
                    stop=True
                else:
                    letre=letre+1
                x=x+1
        
        y=y+1



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