try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
def get_square(x, y, radius):
    '''
    given the center=(x,y) and radius
    calculate the square for the circle to fit into
    return x1, y1, x2, y2 of square's ulc=(x1,y1) and lrc=(x2,y2)
    '''
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    return x1, y1, x2, y2

# create the basic window, let's call it 'root'
root = tk.Tk()
# create a canvas to draw on
cv = tk.Canvas(root, width=640, height=480, bg='white')
cv.grid()


# draw a series of close spaced circles to create a moire pattern
for k in range(1, 320, 2):
    cv.create_oval(get_square(k, k, k), outline='red')
    cv.create_oval(get_square(640-k, k, k), outline='blue')
    cv.create_oval(get_square(k, 480-k, k), outline='red')
    cv.create_oval(get_square(640-k, 480-k, k), outline='blue')
# start the event loop
root.mainloop()