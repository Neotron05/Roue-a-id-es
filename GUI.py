from tkinter import *
from tkinter import ttk
import random, json, JSONS, math, time

objects = JSONS.read('things.json')
spining_jeu = True
sections = []
center_of_wheel = [350, 350]
radius = 300
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
jeu = ""
langage = ""


class section:
    def __init__(self, i):
        # angles beetween the limits of the section and the center of the wheel
        self.angle1 = math.radians(i * 60 + 30)
        self.angle2 = math.radians((i + 1) * 60 + 30)
        # positions of the limits of the section
        self.x1 = center_of_wheel[0] + radius * math.cos(self.angle1)
        self.y1 = center_of_wheel[1] + radius * math.sin(self.angle1)
        self.x2 = center_of_wheel[0] + radius * math.cos(self.angle2)
        self.y2 = center_of_wheel[1] + radius * math.sin(self.angle2)
        # position of the center of the section
        self.x3 = (((self.x1 + self.x2) / 2) + center_of_wheel[0]) / 2
        self.y3 = (((self.y1 + self.y2) / 2) + center_of_wheel[1]) / 2
        # position of the color circle
        self.x4 = center_of_wheel[0] + radius * math.cos((self.angle1 + self.angle2) / 2)
        self.y4 = center_of_wheel[1] + radius * math.sin((self.angle1 + self.angle2) / 2)

        sections.append(self)


def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)


# Create a window
def window():
    root = Tk()
    root.title("GUI")
    root.geometry("1200x800")
    # add a spin the wheel in a canvas
    canvas = Canvas(root, width=1000, height=700)
    canvas.pack()
    wheel = create_circle(center_of_wheel[0], center_of_wheel[1], radius, canvas)
    # add a label to display the result
    label = Label(root, text="")
    label.pack()
    idees, langages = rand_Pick()
    # add a button to spin the wheel
    button = Button(root, text="Spin", command=lambda: spin(canvas, wheel, label, root, idees, langages))
    button.pack()
    for i in range(6):
        section(i)
    draw(canvas, wheel, label, root, idees, langages)
    root.mainloop()


def draw(canvas, wheel, label, root, idees, langages):
    global spining_jeu
    list = langages
    if spining_jeu:
        list = idees
    canvas.delete("all")
    wheel = create_circle(center_of_wheel[0], center_of_wheel[1], radius, canvas)
    for i in range(6):
        canvas.create_line(center_of_wheel[0], center_of_wheel[1], sections[i].x1, sections[i].y1)
        canvas.create_text(sections[i].x3, sections[i].y3, text=list[i])
        # draw a circle in the center of the arc of the section
        canvas.create_oval(sections[i].x4 - 10, sections[i].y4 - 10, sections[i].x4 + 10, sections[i].y4 + 10,
                           fill=colors[i])
    # draw a triangle at the end of the wheel
    canvas.create_polygon(center_of_wheel[0] + radius + 100, center_of_wheel[1],
                          center_of_wheel[0] + radius + 300, center_of_wheel[1] + 100,
                          center_of_wheel[0] + radius + 300, center_of_wheel[1] - 100, fill="red")


# spin the wheel
def spin(canvas, wheel, label, root, idees, langages):
    global spining_jeu, jeu, langage
    list = langages
    if spining_jeu:
        list = idees
    rand = random.randint(40, 75)
    for j in range(rand):
        last_of_list = list[0]
        last_color = colors[0]
        for i in range(6):
            if i == 5:
                list[i] = last_of_list
                colors[i] = last_color
            else:
                list[i] = list[i + 1]
                colors[i] = colors[i + 1]
        draw(canvas, wheel, label, root, idees, langages)
        time.sleep(3 / rand)
        canvas.update()
    # add a label to display the result
    if spining_jeu:
        jeu = idees[-1]
        label.config(text=jeu)
        spining_jeu = False
    else:
        langage = langages[-1]
        label.config(text=langage)
        spining_jeu = True
        button = Button(root, text="Afficher resultat",
                        command=lambda: draw_result(canvas, root))
        button.pack()


def rand_Pick():
    # pick 6 random objects from idees and langages
    idees = random.sample(objects['idees'], 6)
    langages = random.sample(objects['langages'], 6)
    # keep only the attribute "nom" of the objects
    for i in range(6):
        idees[i] = idees[i]['nom']
        langages[i] = langages[i]['nom']
    return idees, langages


# draw the results of the spins
def draw_result(canvas, root):
    root.destroy()
    root = Tk()
    root.title("GUI")
    root.geometry("1200x800")
    canvas = Canvas(root, width=1000, height=700)
    canvas.pack()
    result_jeu = Label(canvas, text=jeu)
    result_jeu.pack()
    result_langage = Label(canvas, text=langage)
    result_langage.pack()

    restart_button = Button(canvas, text="Restart", command=lambda: restart(root))
    restart_button.pack()
    canvas.update()


def restart(root):
    root.destroy()
    window()
