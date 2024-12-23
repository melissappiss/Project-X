import tkinter as tk
from tkinter import messagebox
from bodies.planet import Planet
from bodies.star import Star
from time_manager import TimeStep
from run import run_simulation
import sys 

#bg (background) = imposta il colore di sfondo di un widget, 
#fg (foreground) = imposta il colore del testo del w,
#pady aggiunge uno spazione verticale, aumentando la distanza tra il widget e gli altri elementi sopra o sotto di esso

#Lista per memorizzare i corpi inseriti
bodies = []

#Funzione ch egestisce la parte dell'interfaccia per aggiugere i corpi celesti
def add_body_gui():

    #Funzione per inserire i dati eseguita quando l'utente clicca sul pulsante 'add body'
    def add_body():
        body_type = body_type_var.get()
        #print(f"Selected body type: {body_type}")

        try:

            mass = float(mass_entry.get())
            posx, posy = map(float, position_entry.get().split(","))
            vx, vy = map(float, velocity_entry.get().split(","))
            
            if body_type == "Planet":
                body = Planet(mass, posx, posy, vx, vy)
            elif body_type == "Star":
                body = Star(mass, posx, posy, vx, vy)
            
            #Aggiunta alla lista body e messaggio di conferma
            bodies.append(body)
            messagebox.showinfo("Success", f"{body_type} added successfully!")
            clear_entries()
        
        #Apparirà un messaggio di errore se l'utente inserisce dati non validi
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")



    #Funzione che cancella i valori inseriti nei campi di input dopo che un corpo è stato aggiunto con successo
    def clear_entries():
        mass_entry.delete(0, tk.END)
        position_entry.delete(0, tk.END)
        velocity_entry.delete(0, tk.END)



    add_body_frame = tk.Frame(root, bg ='black')
    add_body_frame.pack(padx=10, pady=10)
    
    #Radiobutton per scegliere il tipo di corpo celeste
    tk.Label(add_body_frame, text="Body Type (Planet/Star):", fg ="white",bg = "black", font = ("Helvetica",12)).grid(row=0, column=0)
    body_type_var = tk.StringVar()
    body_type_var.set("Planet")
    

    planet_radio = tk.Radiobutton(add_body_frame, text="Planet", variable=body_type_var, value="Planet", bg="black", selectcolor="black", indicatoron = 1, fg="white", font = ("Helvetica",12) )
    planet_radio.grid(row=0, column=1)
    star_radio = tk.Radiobutton(add_body_frame, text="Star", variable=body_type_var, value="Star", bg="black", selectcolor="black", indicatoron = 1, fg="white", font = ("Helvetica",12))
    star_radio.grid(row=0, column=2)
    
    #Campo per scegliere la massa 
    tk.Label(add_body_frame, text="Mass (1 to 15 * 10^23 kg):", fg="white", bg="black", font=("Helvetica", 12)).grid(row=1, column=0)
    mass_entry = tk.Entry(add_body_frame, font = ("Helvetica", 12), bg ="black", fg="white")
    mass_entry.grid(row=1, column=1)
    
    #Campo per la posizione (x, y)
    tk.Label(add_body_frame, text="Position (x, y):", fg="white", bg="black", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w")

    posx_entry = tk.Entry(add_body_frame, font=("Helvetica", 12), bg="black", fg="white", width=7)
    posx_entry.grid(row=2, column=1, padx=(5, 0))

    posy_entry = tk.Entry(add_body_frame, font=("Helvetica", 12), bg="black", fg="white", width=7)
    posy_entry.grid(row=2, column=2)

    #Campo per la velocità (vx, vy)
    tk.Label(add_body_frame, text="Velocity (vx, vy):", fg="white", bg="black", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w")

    vx_entry = tk.Entry(add_body_frame, font=("Helvetica", 12), bg="black", fg="white", width=7)
    vx_entry.grid(row=3, column=1, padx=(5, 0))

    vy_entry = tk.Entry(add_body_frame, font=("Helvetica", 12), bg="black", fg="white", width=7)
    vy_entry.grid(row=3, column=2)

    #Pulsante per aggiungere il corpo
    add_button = tk.Button(add_body_frame, text="Add Body", command=add_body, font=("Helvetica", 12), bg="midnight blue", fg="white")
    add_button.grid(row=4, columnspan=4, pady=10)


#Funzione per impostare la velocità della simulazione
def set_simulation_speed():
    speed = speed_scale.get()
    TimeStep.setTempo(f"{speed}x")
    TimeStep.step = 0.01 / speed

#Funzione che gestisce l'intera interfaccia grafica della finestra principale 
def create_gui():
    global root
    root = tk.Tk()
    root.title("GRAVITY SIMULATOR")

    root.config(bg='black')
    
    #I valori False servono per mantenere fisse le dimensioni della finestra principale dell'interfaccia
    root.resizable(False, False)
    tk.Label(root, text="Welcome to the gravity simulation!", font=("Arial", 16), fg = "yellow", bg = "black").pack(pady=10)

    add_body_gui()

    speed_frame = tk.Frame(root, bg ="black")
    speed_frame.pack(padx=10, pady=10)
    tk.Label(speed_frame, text="Simulation Speed:",font = ("Helvetica",12), bg ="black", fg = "white").grid(row=0, column=0)

    speed_scale = tk.Scale(speed_frame, from_=0.1, to=3, orient="horizontal", resolution=0.1, length=50, bg="midnight blue", fg="white")
    speed_scale.set(1)
    speed_scale.grid(row=1, column=0)

    set_button = tk.Button(speed_frame, text="Set Speed", command=set_simulation_speed, bg="midnight blue", fg="white",font=("Helvetica", 12))
    set_button.grid(row=2, columnspan=2)
    
    #Pulsante per avviare la simulazione, quindi i corpi si troveranno nelle posizioni e si muoveranno con le velocità scelte in input
    run_button = tk.Button(root, text="Start Simulation", command=lambda: run_simulation(bodies), font = ("Helvetica", 12), bg = "midnight blue", fg = "white")
    run_button.pack(pady=20)
    
    #Pulsante per chiudere l'applicazione
    run_button = tk.Button(root, text="Quit", command=sys.exit, font = ("Helvetica", 12), bg = "midnight blue", fg = "white")
    run_button.pack(pady=20)

    root.mainloop()
