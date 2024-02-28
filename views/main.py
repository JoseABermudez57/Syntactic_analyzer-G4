from pathlib import Path

from tkinter import Tk, Canvas, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\views\assets\frame")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x580")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=580, width=600, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(300.0, 290.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(300.0, 419.0, image=image_image_2)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(300.0, 419.0, image=entry_image_1)
entry_1 = Text(bd=0, bg="#B8FAFF", fg="#000716", highlightthickness=0)
entry_1.place(x=82.0, y=329.0, width=436.0, height=178.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"),
                  relief="flat")
button_1.place(x=330.43621826171875, y=264.17242431640625, width=93.48816680908203, height=33.198299407958984)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"),
                  relief="flat")
button_2.place(x=175.92105102539062, y=264.17242431640625, width=93.48816680908203, height=33.198299407958984)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(300.0, 191.0, image=image_image_3)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(300.0, 190.5, image=entry_image_2)
entry_2 = Text(bd=0, bg="#B8FAFF", fg="#000716", highlightthickness=0)
entry_2.place(x=67.0, y=149.0, width=466.0, height=81.0)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(300.0, 100.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(300.0, 100.0, image=image_image_5)

if __name__ == '__main__':
    window.resizable(False, False)
    window.mainloop()
