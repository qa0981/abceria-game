import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Tracing App with Background Image and Eraser Feature")
screen.bgcolor("white")

# Load and set the background image
try:
    screen.bgpic("letter_a.gif")  # Set the background image (must be in .gif format)
except Exception as e:
    print("Error loading background image:", e)

# Create an invisible turtle for drawing
drawer = turtle.Turtle()
drawer.hideturtle()  # Hide the turtle cursor
drawer.speed(0)  # Fastest drawing speed
drawer.width(3)  # Set pen width

# Variable to hold the current mode (draw or erase)
current_mode = "draw"

# Function to set the turtle to draw mode
def set_draw_mode():
    global current_mode
    current_mode = "draw"
    drawer.color("black")  # Set pen color to black for drawing
    screen.title("Tracing App - Mode: Draw")

# Function to set the turtle to erase mode
def set_erase_mode():
    global current_mode
    current_mode = "erase"
    drawer.color("white")  # Set pen color to white for erasing (matches bg color)
    screen.title("Tracing App - Mode: Erase")

# Function to toggle between draw and erase mode
def toggle_mode():
    if current_mode == "draw":
        set_erase_mode()
    else:
        set_draw_mode()

# Function to start drawing when the mouse is clicked
def start_drawing(x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

# Function to draw or erase as the mouse is dragged
def draw_or_erase(x, y):
    if current_mode == "draw":
        drawer.goto(x, y)  # Draw when in draw mode
    elif current_mode == "erase":
        drawer.goto(x, y)  # Erase when in erase mode (by drawing with the background color)

# Key bindings for mode toggling
screen.listen()
screen.onkey(toggle_mode, "space")  # Press Space to toggle between draw and erase modes

# Bind mouse events to start drawing on click and drag to draw or erase
screen.onscreenclick(start_drawing)  # Start drawing on mouse click
drawer.ondrag(draw_or_erase)  # Draw or erase while dragging the mouse

# Initialize in draw mode
set_draw_mode()

# Keep the window open until closed by the user
screen.mainloop()