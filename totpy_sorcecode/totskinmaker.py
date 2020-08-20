from PIL import Image, ImageDraw, ImageFilter
import tkinter as tk

a = True
while a == True:
    a = False






    def tot():
        
        
        #img = input("Please input the dir of the img\n> ")
        img = entry.get()
        entry.delete(0, tk.END)

        global img1
        global button

        img1 = img



        

        try:    
            im = Image.open(img1)
            label3.pack_forget()
        except:
            print("That isnt a File directory!")
            label3.pack()
            a = True
            return

            
        



        width, height = im.size

        if width != 64:
            print("Please enter an img with a resolution of 64x64")
            a = True
            #break
            return
        if height != 64:
            print("Please enter an img with a resolution of 64x64")
            a = True
            #break
            return
        


        def slim():
            label5.pack_forget()

            global img1

            im = Image.open(img1)

            slim = entry.get()

            if slim == "y":

                l_arm_L_L1 = 44
                t_arm_L_L1 = 20
                r_arm_L_L1 = 47
                b_arm_L_L1 = 31

                arm_L_L1 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                l_arm_L_L1 = 45
                t_arm_L_L1 = 36
                r_arm_L_L1 = 48
                b_arm_L_L1 = 47

                arm_L_L2 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                arm_L_L2 = arm_L_L2.convert("RGBA")
                arm_L_L1 = arm_L_L1.convert("RGBA")

                arm_L= Image.alpha_composite(arm_L_L1, arm_L_L2)


                l_arm_R_L1 = 37
                t_arm_R_L1 = 52
                r_arm_R_L1 = 40
                b_arm_R_L1 = 63

                arm_R_L1 = im.crop((l_arm_R_L1, t_arm_R_L1, r_arm_R_L1, b_arm_R_L1))

                l_arm_R_L1 = 53
                t_arm_R_L1 = 52
                r_arm_R_L1 = 56
                b_arm_R_L1 = 63

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
                gui.destroy()
                exit()
                
            elif slim == "n":

                l_arm_L_L1 = 44
                t_arm_L_L1 = 20
                r_arm_L_L1 = 48
                b_arm_L_L1 = 31

                arm_L_L1 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                l_arm_L_L1 = 44
                t_arm_L_L1 = 36
                r_arm_L_L1 = 48
                b_arm_L_L1 = 47

                arm_L_L2 = im.crop((l_arm_L_L1, t_arm_L_L1, r_arm_L_L1, b_arm_L_L1))

                arm_L_L2 = arm_L_L2.convert("RGBA")
                arm_L_L1 = arm_L_L1.convert("RGBA")

                arm_L= Image.alpha_composite(arm_L_L1, arm_L_L2)


                
                l_arm_R_L1 = 36
                t_arm_R_L1 = 52
                r_arm_R_L1 = 40
                b_arm_R_L1 = 63

                arm_R_L1 = im.crop((l_arm_R_L1, t_arm_R_L1, r_arm_R_L1, b_arm_R_L1))

                l_arm_R_L1 = 52
                t_arm_R_L1 = 52
                r_arm_R_L1 = 56
                b_arm_R_L1 = 63

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

                gui.destroy()
                exit()



                
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

        label2.pack_forget()
        label6.pack()
        


        #slim = input("Is this a slim skin or normal size(y/n)\n> ")
        button.pack_forget()
        button = tk.Button(gui, text="ENTER", fg="white", bg="#5D5D66", command=slim).pack()







    gui = tk.Tk()
    gui.geometry("200x250")
    gui.title("Totem skin maker")
    gui.configure(bg='#5D5D66')
    label = tk.Label(text="Totem skin maker", bg="#5D5D66", fg="white").pack()
    label1 = tk.Label(text="\n", bg="#5D5D66").pack()


    label6 = tk.Label(text="is your skin style slim (y/n)", fg="white", bg="#5D5D66")

    label2 = tk.Label(text="Please input the dir of the img", fg="white", bg="#5D5D66")
    label2.pack()


    
        
    entry = tk.Entry(bg ="#5D5D66", fg="white")
    entry.pack()


    global button
    label4 = tk.Label(text="\n", bg = "#5D5D66").pack()
    button = tk.Button(gui, text="ENTER", fg="white", bg="#5D5D66", command=tot)
    button.pack()

    label3 = tk.Label(text="That isnt a File directory!", fg="white", bg="#5D5D66")
    label5 = tk.Label(text="please put y for yes and n for no", fg="white", bg="#5D5D66")

    gui.mainloop()












    




    
    
