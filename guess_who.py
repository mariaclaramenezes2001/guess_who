import tkinter as tk


# PARTE 1: CARREGAR IMAGENS DE UMA PASTA guess_who PARA UMA LISTA 
import glob
from PIL import Image, ImageTk

images_paths = glob.glob("/Users/mariaclaramenezes/Desktop/guess_who/*")
images = []

# abre cada imagem e adiciona-a a lista "images", mas se for a redcross entao grava com esse nome fora da lista
for path in images_paths:
    if path != "/Users/mariaclaramenezes/Desktop/guess_who/redcross.jpg":
        img= Image.open(path, mode= "r")
        images.append(img)
    else:
       
        redcross = Image.open(path, mode= "r")
 
    
 
#PARTE 2: METER BOTOES NUMA JANELA
 
    

#isso é standard de começar root window em Tkinter
root = tk.Tk()
root.geometry("800x800")
root.title("Quem é quem?")


#listas onde vou gravar cada fase de transformar imagens em butoes de imagens
imageto =[]
buttonpic =[]
imagebutton = []


#passar a red cross para tamanho definido e para o tipo de imagem dos butoes
redcross = redcross.resize((150,150))
redcrosstkphoto = ImageTk.PhotoImage(redcross)



#essas cores vao para o background e servem so para se avaliar o estado do butao
#ou seja, sao paramentros q a maquina nao altera a toa e da para ver se o butao esta em pessoa ou em cruz
cor_pessoa = 'green'
cor_cross = 'red'



for i in range(len(images)): #cada butao tem de ter tudo soxinho
   
    imageto.append( images[i].resize((150,150)))
    buttonpic.append(ImageTk.PhotoImage(imageto[i]))
    
    #o lambda so conta o ultimo indice entao o i=i atribui o i em especifico da iteração atual senao so alterava a ultima imagem sempre
    btn = tk.Button(root, image = buttonpic[i], bg = cor_pessoa, command = lambda i = i : change_image(i))
    imagebutton.append(btn)
  
    
    #figure out sistema de placement mais decente para caber todas
    #place, grid, pack sao tudo formas de colocar o botao na window, mas escolhi place para poder meter coordenadas em especifico
    if i<4:
        imagebutton[i].place(x=0 + (i*200), y= 0 )
    elif 4<=i<8: 
        imagebutton[i].place(x=0 + ((i-4)*200), y= 200 )
    elif 8<=i<12:
        imagebutton[i].place(x=0 + ((i-8)*200), y= 400 )
    else:
        imagebutton[i].place(x=0 + ((i-12)*200), y= 600 )
        
        

#essa é a função comando de todos os butoes
#se o butao estiver em modo pessoa, vai ter background(bg) verde entao temos de mudar pra cruz (e alterar bg para vermelho)
#se o butao tiver em modo cruz, vai ter o background(bg) vermelho entao temos de mudar para pessoa ao clicar, e altera-se o bg para verde para se saber q mudou o estado



def change_image(p):
   
    if imagebutton[p]['bg'] == cor_pessoa:
       imagebutton[p].config(bg = cor_cross, image = redcrosstkphoto)
    else: 
        imagebutton[p].config(bg = cor_pessoa, image = buttonpic[p])



#coisa standard de tkinter tmb
root.mainloop()


