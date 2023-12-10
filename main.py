from tkinter import filedialog, Tk, Canvas, Button, Scrollbar, BOTH
from PIL import Image, ImageTk, ImageEnhance

# global variables to store the original image, the Tkinter image, and the select button
original_image = None
tk_image = None
select_button = None

# function to select an image
def select_image():
    global original_image, select_button

    # open a file dialog to select the image
    path = filedialog.askopenfilename()
    if not path:
        return

    # open the image using PIL
    image = Image.open(path)

    # deep fry the image using PIL
    original_image = deep_fry(image)

    # display the fried image using Tkinter
    display_image(original_image)

    # hide the select button
    select_button.place_forget()

# function to deep fry the given image using PIL
def deep_fry(image):
    # deep fry the image using PIL
    converter = ImageEnhance.Color(image)
    converter.enhance(5).save("sat-deepfry-image.png") # saturates
    image = Image.open('sat-deepfry-image.png')
    converter = ImageEnhance.Sharpness(image)
    converter.enhance(15).save('comp-image.png') # sharpens
    image = Image.open('comp-image.png')

    return image

# function to display the given image using Tkinter
def display_image(image):
    global tk_image

    # calculate the aspect ratio of the image
    aspect_ratio = image.width / image.height

    # calculate the new dimensions of the image
    new_width = min(image.width, 800)
    new_height = int(new_width / aspect_ratio)

    # resize the image for display purposes
    display_image = image.resize((new_width, new_height))

    # convert the resized image to Tkinter format
    tk_image = ImageTk.PhotoImage(display_image)

    # adjust the size of the canvas to match the image
    canvas.config(width=new_width, height=new_height)

    # display the resized image in the canvas
    canvas_image = canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.config(scrollregion=canvas.bbox("all"))

    # add a button to save the image
    save_button = Button(canvas, text="Download", command=save_image)
    canvas.create_window(10, 10, anchor="nw", window=save_button)

    # adds a scrollbar
    canvas_image = canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.config(scrollregion=canvas.bbox("all"))

# function to save the given image
def save_image():
    global original_image

    # open a file dialog to select the save path
    path = filedialog.asksaveasfilename(defaultextension=".png")
    if not path:
        return

    # save the image using PIL
    original_image.save(path)

# create the root window
root = Tk()

# set the size of the window to 800x500 pixels
root.geometry("800x500")

# create a canvas to display the image
canvas = Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# creates image scrollbar
scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# configure the canvas to scroll with the scrollbar
canvas.config(yscrollcommand=scrollbar.set)

# add a button to select an image
select_button = Button(root, text="Select Image", command=select_image)
select_button.place(x=1, y=1)

# start the Tkinter main loop
root.mainloop()
