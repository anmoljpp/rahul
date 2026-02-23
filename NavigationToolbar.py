import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# testing tkinter window


def update_plot():
    ax.clear()
    x = np.linspace(0, 10, 100)
    y = np.random.rand(100)
    ax.plot(x, y, color="green")
    ax.set_title("Updated Random Plot")
    canvas.draw()

# Create main window
root = tk.Tk()
root.title("Interactive Matplotlib Dashboard")
root.geometry("900x650")

# Main Frame
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create Figure
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_title("Initial Plot")

# Embed in Tkinter
canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

btn = ttk.Button(main_frame, text="Generate New Plot", command=update_plot)
btn.pack(pady=10)
# Toolbar
toolbar = NavigationToolbar2Tk(canvas, main_frame).update()

# Button to update plot

root.mainloop()

