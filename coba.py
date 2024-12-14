import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main application window
root = tk.Tk()
root.title("Tracing App with Alphabet")

background_canvas = tk.Canvas(root, bg="white", width=800, height=600)
background_canvas.pack()

drawing_canvas = tk.Canvas(root, width=800, height=600, bg="none", highlightthickness=0)
drawing_canvas.place(x=0, y=0)

# Load the image (make sure the image is in the same directory)
try:
    letter_image = Image.open("image\letter-a.png")
    # Resize the image if needed to fit the canvas
    letter_image = letter_image.resize((300, 300), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
    letter_image = ImageTk.PhotoImage(letter_image)
    background_canvas.create_image(400, 300, image=letter_image)
except Exception as e:
    print(f"Error loading image: {e}")

# Initialize the previous x and y coordinates
previous_x = None
previous_y = None

current_mode = "draw"

def draw(event):
    global previous_x, previous_y
    x, y = event.x, event.y
    if previous_x and previous_y:
        if current_mode == "draw":
            # Draw lines in black on the drawing canvas
            drawing_canvas.create_line(previous_x, previous_y, x, y, fill="black", width=3)
        elif current_mode == "erase":
            # Erase lines on the drawing canvas by drawing white lines
            drawing_canvas.create_line(previous_x, previous_y, x, y, fill="white", width=10)
    previous_x, previous_y = x, y

# Define a function to reset the previous position when the mouse button is released
def reset(event):
    global previous_x, previous_y
    previous_x, previous_y = None, None

def toggle_mode():
    global current_mode
    current_mode = "erase" if current_mode == "draw" else "draw"
    mode_button.config(text=f"Mode: {current_mode.capitalize()}")

mode_button = tk.Button(root, text="Mode: Draw", command=toggle_mode)
mode_button.pack()

# Bind the mouse events to the canvas
drawing_canvas.bind("<B1-Motion>", draw)  # Left mouse button drag event
drawing_canvas.bind("<ButtonRelease-1>", reset)

# Run the main application loop
root.mainloop()