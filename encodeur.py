from PIL import Image

def image(nom_image):
    img = Image.open(nom_image)
    largeur = img.width
    hauteur = img.height
    return img,largeur,hauteur


def reset(largeur,hauteur): #rend toute les valeur rgb pair (represente le zero)
    global r
    global v
    global b
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


def convertisseur(hauteur,largeur):
    message=input("inserer le message:")
    fin=len(message)-1
    letre=0
    stop=False
    y=0
    while y <=hauteur-1 or stop==False:
        x=0
        if stop==False:
            while x <=largeur-1 or stop==False:
                if message[letre-1]=="a":
                   img.putpixel( (x,y) , (r+1,v+0,b+0) )
                   x=x+1
                   img.putpixel( (x,y) , (r+0,v+0,b+0) )
                if message[letre]=="b":
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                if message[letre]=="c":
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                if message[letre]=="d":
                    img.putpixel( (x,y) , (r+0,v+1,b+1) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                if message[letre]=="e":
                    img.putpixel( (x,y) , (r+1,v+1,b+1) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                if message[letre]=="f":
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                if message[letre]=="g":
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                if message[letre]=="h":
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                if message[letre]=="i":
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                if message[letre]=="j":
                    img.putpixel( (x,y) , (r+1,v+1,b+1) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                if message[letre]=="k":
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                if message[letre]=="l":
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                if message[letre]=="m":
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                if message[letre]=="n":
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                if message[letre]=="o":
                    img.putpixel( (x,y) , (r+1,v+1,b+1) )
                    x=x+1
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                if message[letre]=="p":
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                if message[letre]=="q":
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                if message[letre]=="r":
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                if message[letre]=="s":
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                if message[letre]=="t":
                    img.putpixel( (x,y) , (r+1,v+1,b+1) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                if message[letre]=="u":
                    img.putpixel( (x,y) , (r+1,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+1) )
                if message[letre]=="v":
                    img.putpixel( (x,y) , (r+1,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+1) )
                if message[letre]=="x":
                    img.putpixel( (x,y) , (r+0,v+1,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+1) )
                if message[letre]=="y":
                    img.putpixel( (x,y) , (r+1,v+1,b+1) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+1) )
                if message[letre]=="z":
                    img.putpixel( (x,y) , (r+1,v+0,b+1) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+1,b+1) )
                if message[letre]==" ":
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                    x=x+1
                    img.putpixel( (x,y) , (r+0,v+0,b+0) )
                
                
                if letre >=fin:
                    stop=True
                else:
                    letre=letre+1
                x=x+1
        
        y=y+1








img,largeur,hauteur=image("frog.png")
reset(largeur,hauteur)
convertisseur(largeur,hauteur)


img.show()