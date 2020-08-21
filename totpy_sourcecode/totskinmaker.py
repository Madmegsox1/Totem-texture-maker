from PIL import Image, ImageDraw, ImageFilter
import tkinter as tk
import requests
import os



def online():
    main.withdraw()
    def back():
        main.deiconify()
        gui2.destroy()

    def api():
        name1 = entry.get()
        name2 = "/16.png"
        name = name1 + name2
        entry.delete(0, tk.END)
        skin = requests.get("https://minotar.net/armor/body/{}" .format(name))
        file = open("totem.png", "wb")
        file.write(skin.content)
        file.close()
        main.deiconify()
        gui2.destroy()

        






    gui2 = tk.Tk()

    gui2.geometry("200x250")
    gui2.title("Menue")
    gui2.configure(bg='#5D5D66')


    label = tk.Label(gui2, text="Totem skin maker online", bg="#5D5D66", fg="white").pack()

    label = tk.Label(gui2, text="\n", bg="#5D5D66").pack()
    label = tk.Label(gui2, text="Please input your username or uuid", bg="#5D5D66", fg="white").pack()
    entry = tk.Entry(gui2, bg="#787878", bd=0.5, fg="white")
    entry.pack()

    label = tk.Label(gui2, text="\n", bg="#5D5D66").pack()



    button = tk.Button(gui2, text="GO", fg="white", width = 4, bg="#787878", bd=0.5, command=api)
    button.pack() 
    button2 = tk.Button(gui2, text="BACK",fg="white", bg="#787878", bd=0.5, command=back)
    button2.pack()

    







    gui2.mainloop()




def offline():
    main.withdraw()

    def back():
        main.deiconify()
        gui.destroy()




    def tot():
        
        
        #img = input("Please input the dir of the img\n> ")
        img = entry.get()
        entry.delete(0, tk.END)

        global img1
        global button
        global button2

        img1 = img



        

        try:    
            im = Image.open(img1)
            label3.pack_forget()
        except:
            print("That isnt a File directory!")
            label3.pack()
            return

            
        



        width, height = im.size

        if width != 64:
            print("Please enter an img with a resolution of 64x64")
            #break
            return
        if height != 64:
            print("Please enter an img with a resolution of 64x64")
            #break
            return
        


        def slim():
            label5.pack_forget()

            global img1

            im = Image.open(img1)

            slim = entry2.get()


            if slim == "y":

                l_arm_L_L1 = 44
                t_arm_L_L1 = 20
                r_arm_L_L1 = 47
                b_arm_L_L1 = 32

                arm_L_L1 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                l_arm_L_L1 = 45
                t_arm_L_L1 = 36
                r_arm_L_L1 = 48
                b_arm_L_L1 = 48

                arm_L_L2 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                arm_L_L2 = arm_L_L2.convert("RGBA")
                arm_L_L1 = arm_L_L1.convert("RGBA")

                arm_L= Image.alpha_composite(arm_L_L1, arm_L_L2)


                l_arm_R_L1 = 37
                t_arm_R_L1 = 52
                r_arm_R_L1 = 40
                b_arm_R_L1 = 64

                arm_R_L1 = im.crop((l_arm_R_L1, t_arm_R_L1, r_arm_R_L1, b_arm_R_L1))

                l_arm_R_L1 = 53
                t_arm_R_L1 = 52
                r_arm_R_L1 = 56
                b_arm_R_L1 = 64

                arm_R_L2 = im.crop((l_arm_R_L1, t_arm_R_L1, r_arm_R_L1, b_arm_R_L1))


                arm_R_L1 = arm_R_L1.convert("RGBA")
                arm_R_L2 = arm_R_L2.convert("RGBA")

                arm_R= Image.alpha_composite(arm_R_L1, arm_R_L2)


                totem = Image.new("RGBA", (16,32), "WHITE")

                totem.putalpha(0)

                totem.paste(head, (4,0))
                #(chest (4,8))
                #totem.paste(arm_R(0,8))
                #totem.paste(arm_L(12,8))
                #totem.paste(legs(4,20))


                imi2 = [head, chest, arm_R, arm_L, legs]
                loc = [4, 4, 1, 12, 4]
                loc2 = [0, 8, 8, 8, 20]
                locnum = 0
                for im in imi2:
                    totem.paste(im, (loc[locnum], loc2[locnum]))
                    locnum += 1
                totem.save("totem.png")
                main.deiconify()
                gui.destroy()
                
            elif slim == "n":

                l_arm_L_L1 = 44
                t_arm_L_L1 = 20
                r_arm_L_L1 = 48
                b_arm_L_L1 = 32

                arm_L_L1 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                l_arm_L_L1 = 44
                t_arm_L_L1 = 36
                r_arm_L_L1 = 48
                b_arm_L_L1 = 48

                arm_L_L2 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                arm_L_L2 = arm_L_L2.convert("RGBA")
                arm_L_L1 = arm_L_L1.convert("RGBA")

                arm_L= Image.alpha_composite(arm_L_L1, arm_L_L2)


                
                l_arm_R_L1 = 36
                t_arm_R_L1 = 52
                r_arm_R_L1 = 40
                b_arm_R_L1 = 64

                arm_R_L1 = im.crop((l_arm_R_L1, t_arm_R_L1, r_arm_R_L1, b_arm_R_L1))

                l_arm_R_L1 = 52
                t_arm_R_L1 = 52
                r_arm_R_L1 = 56
                b_arm_R_L1 = 64

                arm_R_L2 = im.crop((l_arm_R_L1, t_arm_R_L1, r_arm_R_L1, b_arm_R_L1))


                arm_R_L1 = arm_R_L1.convert("RGBA")
                arm_R_L2 = arm_R_L2.convert("RGBA")

                arm_R= Image.alpha_composite(arm_R_L1, arm_R_L2)


                totem = Image.new("RGBA", (16,32), "WHITE")

                totem.putalpha(0)

                totem.paste(head, (4,0))
                #(chest (4,8))
                #totem.paste(arm_R(0,8))
                #totem.paste(arm_L(12,8))
                #totem.paste(legs(4,20))


                imi2 = [head, chest, arm_L, arm_R, legs]
                loc = [4, 4, 0, 12, 4]
                loc2 = [0, 8, 8, 8, 20]
                locnum = 0
                for im in imi2:
                    totem.paste(im, (loc[locnum], loc2[locnum]))
                    locnum += 1

                totem.save("totem.png")


                main.deiconify()

                gui.destroy()




                
            else:
                print("Please answer with y or n")
                label5.pack()

                #break
                return
        
        #/\/\/\/\/\/\/\/\/\HEAD/\/\/\/\/\/\/\/\
        l_head_L1 = 8
        t_head_L1 = 8
        r_head_L1 = 16
        b_head_L1 = 16

        im_head_L1 = im.crop((l_head_L1, t_head_L1, r_head_L1, b_head_L1))

        l_head_L2 = 40
        t_head_L2 = 8
        r_head_L2 = 48
        b_head_L2 = 16

        im_head_L2 = im.crop((l_head_L2, t_head_L2, r_head_L2, b_head_L2))

        background = im_head_L1

        backgroundrgb = background.convert("RGBA")

        im_head_L2rgb = im_head_L2.convert("RGBA")

        head = Image.alpha_composite(backgroundrgb, im_head_L2rgb)

        #/\/\/\/\/\/\/\/\/\LEGS/\/\/\/\/\/\/\/\

        l_legs_L = 4
        t_legs_L = 20
        r_legs_L = 8
        b_legs_L = 32

        im_legs_L_L1 = im.crop((l_legs_L, t_legs_L, r_legs_L, b_legs_L))

        l_legs_L = 4
        t_legs_L = 36
        r_legs_L = 8
        b_legs_L = 48

        im_legs_L_L2 = im.crop((l_legs_L, t_legs_L, r_legs_L, b_legs_L))


        im_legs_L_L1 = im_legs_L_L1.convert("RGBA")

        im_legs_L_L2 = im_legs_L_L2.convert("RGBA")

        L_leg = Image.alpha_composite(im_legs_L_L1, im_legs_L_L2)


        l_legs_R = 20
        t_legs_R = 52
        r_legs_R = 24
        b_legs_R = 64

        im_legs_R_L1 = im.crop((l_legs_R, t_legs_R, r_legs_R, b_legs_R))


        l_legs_R = 4
        t_legs_R = 52
        r_legs_R = 8
        b_legs_R = 64

        im_legs_R_L2 = im.crop((l_legs_R, t_legs_R, r_legs_R, b_legs_R))
        

        im_legs_R_L1 = im_legs_R_L1.convert("RGBA")
        im_legs_R_L2 = im_legs_R_L2.convert("RGBA")

        R_leg = Image.alpha_composite(im_legs_R_L1, im_legs_R_L2)


        legs_background = Image.new("RGBA", (8,12), "WHITE")

        x_offset = 0
        imi = [L_leg, R_leg]
        for im in imi:
            legs_background.paste(im, (x_offset, 0))
            x_offset += 4


        legs = legs_background



        #/\/\/\/\/\/\/\/\/\CHEST/\/\/\/\/\/\/\/\
        im = Image.open(img)

        l_chest_L1 = 20
        t_chest_L1 = 20
        r_chest_L1 = 28
        b_chest_L1 = 32

        chest_L1 = im.crop((l_chest_L1, t_chest_L1, r_chest_L1, b_chest_L1))

        l_chest_L1 = 20
        t_chest_L1 = 36
        r_chest_L1 = 28
        b_chest_L1 = 48

        chest_L2 = im.crop((l_chest_L1, t_chest_L1, r_chest_L1, b_chest_L1))

        chest_L1 = chest_L1.convert("RGBA")
        chest_L2 = chest_L2.convert("RGBA")

        chest = Image.alpha_composite(chest_L1, chest_L2)

        #/\/\/\/\/\/\/\/\/\ARMS/\/\/\/\/\/\/\/\

        #im = Image.open(img)
        label1.pack_forget()
        label2.pack_forget()
        label6.pack()

        entry.pack_forget()
        entry2.pack()

        label7.pack()

        button.pack_forget()
        button = tk.Button(gui, text="ENTER", fg="white", bg="#5D5D66", command=slim)
        button.pack()
        button2.pack_forget()
        button2 = tk.Button(gui, text="BACK", fg="white", bg="#5D5D66", command=back)
        button2.pack()
        


        #slim = input("Is this a slim skin or normal size(y/n)\n> ")








    gui = tk.Tk()
    gui.geometry("200x250")
    gui.title("Totem skin maker - offline")
    gui.configure(bg='#5D5D66')
    label = tk.Label(gui, text="Totem skin maker", bg="#5D5D66", fg="white").pack()
    label1 = tk.Label(gui, text="\n", bg="#5D5D66")
    label1.pack()


    label2 = tk.Label(gui, text="Please input the dir of the img", fg="white", bg="#5D5D66")
    label2.pack()

        
    entry = tk.Entry(gui, bg="#787878", bd=0.5, fg="white")
    entry.pack()
    entry2 = tk.Entry(gui, bg="#787878", bd=0.5, fg="white")


    global button
    global button2
    label4 = tk.Label(gui, text="\n", bg = "#5D5D66").pack()
    label7 = tk.Label(gui, text="\n", bg = "#5D5D66")
    button = tk.Button(gui, text="ENTER", fg="white", bg="#787878", bd=0.5, command=tot)
    button.pack()
    button2 = tk.Button(gui, text="BACK", fg="white", bg="#787878", bd=0.5, command=back)
    button2.pack()

    label6 = tk.Label(gui, text="is your skin style slim (y/n)", fg="white", bg="#5D5D66")

    label3 = tk.Label(gui, text="That isnt a File directory!", fg="white", bg="#5D5D66")
    label5 = tk.Label(gui, text="please put y for yes and n for no", fg="white", bg="#5D5D66")



    gui.mainloop()


main = tk.Tk()

main.geometry("200x250")
main.title("Menue")
main.configure(bg='#5D5D66')

label = tk.Label(main, text="Totem skin maker menue", bg="#5D5D66", fg="white").pack()

label = tk.Label(main, text="\n\n", bg="#5D5D66").pack()

button = tk.Button(main, text="OFFLINE", fg="white", bg="#787878", bd=0.5, command=offline)
button.pack()

label2 = tk.Label(main, text="\n\n", bg="#5D5D66").pack()

button2 = tk.Button(main, text="ONLINE", fg="white", bg="#787878", bd=0.5,command=online)
button2.pack()


main.mainloop()













    




    
    
