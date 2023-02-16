import tkinter as tk
import PIL
from PIL import ImageEnhance
from tkinter import filedialog
from PIL import Image, ImageTk

# function to open a file dialog and select an image
def select_image():
    # open the file dialog
    path = filedialog.askopenfilename()
    if not path:
        return

    # open the image using PIL
    image = Image.open(path)

    # deep fry the image using PIL
    image = deep_fry(image)

    # display the fried image using Tkinter
    display_image(image)

# function to deep fry the given image using PIL
def deep_fry(image):
    # deep fry the image using PIL
    converter = PIL.ImageEnhance.Color(image)
    converter.enhance(5).save("sat-deepfry-image.png") # saturates
    image = PIL.Image.open('sat-deepfry-image.png')
    converter = PIL.ImageEnhance.Sharpness(image)
    converter.enhance(15).save('comp-image.png') # sharpens
    image = PIL.Image.open('comp-image.png')

    return image

# function to display the given image using Tkinter
def display_image(image):
    # convert the image to Tkinter format
    image = ImageTk.PhotoImage(image)

    # display the image in the label widget
    label = tk.Label(root, image=image)
    label.image = image
    label.pack()

    # add a button to save the image
    save_button = tk.Button(root, text="Download", command=lambda: save_image(image))
    save_button.pack()

# function to save the given image
def save_image(image):
    # open a file dialog to select the save path
    path = filedialog.asksaveasfilename(defaultextension=".png")
    if not path:
        return

    # save the image using PIL
    image = image._PhotoImage__photo.subsample(2)
    image.write(path)

# create the root window
root = tk.Tk()

# set the size of the window to 500x500 pixels
root.geometry("500x500")

# add a button to select an image
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack()

# start the Tk
root.mainloop()
