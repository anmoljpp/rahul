import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Create main window
root = tk.Tk()
root.title("Matplotlib in Tkinter")
root.geometry("800x600")

# Create a Frame for plot
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(5, 4))

# Sample data
x = np.linspace(0, 10, 100)
y = np.tan(x)

# Plot data
ax.plot(x, y, label="sin(x)")
ax.set_title("Sine Wave")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.legend()

# Embed figure in Tprogramkinter
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()

# Place canvas in window
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Add toolbar
toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()

root.mainloop()