import tkinter as tk
from tkinter import messagebox
from bodies.planet import Planet
from bodies.star import Star
from time_manager import TimeStep
from run import run_simulation
import sys 

bodies = []


def add_body_gui():

    def add_body():

        body_type = body_type_var.get()

        try:

            mass = float(mass_entry.get())
            posx, posy = map(float, position_entry.get().split(","))
            vx, vy = map(float, velocity_entry.get().split(","))
            
            if body_type == "Planet":
                body = Planet(mass, posx, posy, vx, vy)
            elif body_type == "Star":
                body = Star(mass, posx, posy, vx, vy)

            bodies.append(body)
            messagebox.showinfo("Success", f"{body_type} added successfully!")
            clear_entries()

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

#
    def clear_entries():

        mass_entry.delete(0, tk.END)
        position_entry.delete(0, tk.END)
        velocity_entry.delete(0, tk.END)

    add_body_frame = tk.Frame(root, bg ='black')
    add_body_frame.pack(padx=10, pady=10)

    tk.Label(add_body_frame, text="Body Type (Planet/Star):", fg ="white",bg = "black", font = ("Helvetica",12)).grid(row=0, column=0)
    body_type_var = tk.StringVar()
    body_type_var.set("Planet")

    planet_radio = tk.Radiobutton(add_body_frame, text="Planet", variable=body_type_var, value="Planet", bg = "black", fg = "white", font = ("Helvetica",12) )
    planet_radio.grid(row=0, column=1)
    star_radio = tk.Radiobutton(add_body_frame, text="Star", variable=body_type_var, value="Star", fg="white", bg="black", font=("Helvetica", 12))
    star_radio.grid(row=0, column=2)

    tk.Label(add_body_frame, text="Mass (1 to 15 * 10^23 kg):", fg="white", bg="black", font=("Helvetica", 12)).grid(row=1, column=0)
    mass_entry = tk.Entry(add_body_frame, font = ("Helvetica", 12), bg ="white", fg="black")
    mass_entry.grid(row=1, column=1)

    tk.Label(add_body_frame, text="Position (x, y):",fg="white", bg="black", font=("Helvetica", 12)).grid(row=2, column=0)
    position_entry = tk.Entry(add_body_frame, font = ("Helvetica",12), bg ="white", fg = "black")
    position_entry.grid(row=2, column=1)

    tk.Label(add_body_frame, text="Velocity (vx, vy):",font = ("Helvetica",12), bg ="white", fg = "black").grid(row=3, column=0)
    velocity_entry = tk.Entry(add_body_frame,font = ("Helvetica",12), bg ="white", fg = "black" )
    velocity_entry.grid(row=3, column=1)

    add_button = tk.Button(add_body_frame, text="Add Body", command=add_body, font = ("Helvetica", 12), bg = "midnight blue", fg ="white")
    add_button.grid(row=4, columnspan=2)



'''def set_simulation_speed():

    speed = speed_scale.get()
    timeStep.setTempo(f"{speed}x")
    timeStep.step = 0.01 / speed
    messagebox.showinfo("Success", f"Simulation speed set to {speed}x")'''


def create_gui():

    global root
    root = tk.Tk()
    root.title("GRAVITY SIMULATOR")

    root.resizable(False, False)
    tk.Label(root, text="Welcome to the gravity simulation!", font=("Arial", 16), fg = "white", bg = "black").pack(pady=10)

    add_body_gui()

    '''speed_frame = tk.Frame(root)
    speed_frame.pack(padx=10, pady=10)
    tk.Label(speed_frame, text="Simulation Speed (0.1x to 3x):").grid(row=0, column=0)

    speed_scale = tk.Scale(speed_frame, from_=0.1, to=3, orient="horizontal", resolution=0.1, length=50)
    speed_scale.set(1)
    speed_scale.grid(row=0, column=1)

    set_button = tk.Button(speed_frame, text="Set Speed", command=set_simulation_speed)
    set_button.grid(row=1, columnspan=2)'''

    run_button = tk.Button(root, text="Start Simulation", command=lambda: run_simulation(bodies), font = ("Helvetica", 12), bg = "midnight blue", fg = "white")
    run_button.pack(pady=20)
    
    run_button = tk.Button(root, text="Quit", command=sys.exit, font = ("Helvetica", 12), bg = "midnight blue", fg = "white")
    run_button.pack(pady=20)

    root.mainloop()
