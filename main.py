~ TypeRacer

import sys
from tkinter import *
import random

root = Tk()

~ variable assignment
speed1 = 0
count = 0
i = 0
speed2 = 0
inc = 0
wcount = 0

def gameframe(xmove):
        app = Tk()

            mylist1 = "As I sit in my room late at night, staring at the computer screen, I decide it would be a good idea to create this text. There isn't much meaning to it, other than to get some simple practice."
                mylist2 = "An appraisal invites the bond. The wine breaks an instructed employer underneath an economics. The domestic exits near a servant. An ancient comic sweeps. A fashioned autumn stumbles inside a criminal"
                    mylist3 = "Lines of weeds criss crossed the cracked parking lot of the Seashell Motor Courts. The flaking paint on the buildings had chalked to a pastel pink on walls covered with graffiti. Many of the windows had been smashed out. Where the sign had been, atop rusting steel posts, only the metal outline of a seashell remained."

                        ~ select random paragraph
                            choice = random.choice([mylist1, mylist2, mylist3])

                                app.geometry("800x400")
                                    app.title("TypeRacer")

                                        ~ text area
                                            x = Text(app, height = 8, width = 70 , bg = "~90cb8d")
                                                x.pack(anchor=NW)

                                                    ~ canvas
                                                        w = Canvas(app, width=800, height=400)
                                                            app.configure(background='~DAF7A6')
                                                                w.configure(background='~cfa672')
                                                                    w.pack()

                                                                        ~ Display the paragraph
                                                                            if choice == mylist1:
                                                                                        text1 = "As I sit in my room late at night, staring at the computer screen, I decide it would be a good idea to \ncreate this text. There isn't much meaning to it, other than to get some simple practice."
                                                                                                w.create_text(410, 180, text=text1, font=("Comic Sans MS", 11))
                                                                                                