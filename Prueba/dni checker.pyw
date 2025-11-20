from tkinter import *
from tkinter import messagebox

# Inicializo variables
letras = "TRWAGMYFPDXBNJZSQVHLCKEO"

# Ventana principal
ventana = Tk()
ventana.geometry("370x200")
ventana.config(bg="#E8773F")  # Fondo naranja
ventana.title("Bienvenido al Sistema")
# ventana.iconbitmap('img/icono2.ico')  # Descomenta si tienes un icono

# Etiquetas
etiqueta1 = Label(ventana, text="Bienvenido", font=("Arial Bold", 16), bg="#E8773F", fg="#FEFEFE")
etiqueta2 = Label(ventana, text="Nombre: ", font=("Arial", 14), bg="#E8773F", fg="#FEFEFE")
etiqueta3 = Label(ventana, text="DNI: ", font=("Arial", 14), bg="#E8773F", fg="#FEFEFE")

etiqueta1.grid(column=1, row=0)
etiqueta2.grid(column=0, row=1)
etiqueta3.grid(column=0, row=2)

# Entradas
cajaNombre = Entry(ventana, width=15)
cajaNombre.grid(column=1, row=1)

cajaDNI = Entry(ventana, width=15)
cajaDNI.grid(column=1, row=2)

# Función para validar DNI
def Pulsar():
    nombre_usuario = cajaNombre.get().strip()
    dni = cajaDNI.get().strip().upper()

    # Validaciones básicas
    if not nombre_usuario:
        messagebox.showerror("Error", "Ingrese su nombre")
        return

    if len(dni) < 9:
        messagebox.showerror("Error", "El DNI debe tener 8 números y 1 letra")
        return

    numero_str = dni[:-1]
    letra = dni[-1]

    if not numero_str.isdigit():
        messagebox.showerror("Error", "Los primeros 8 caracteres deben ser números")
        return

    numeros = int(numero_str)
    letraCorrecta = letras[numeros % 23]

    if letra == letraCorrecta:
        messagebox.showinfo("Sistema 2SMR", f"Bienvenido al sistema {nombre_usuario} ✅")
    else:
        messagebox.showerror("Sistema 2SMR", f"DNI Incorrecto ❌. La letra correcta sería: {letraCorrecta}")

# Botón
boton = Button(ventana, text="Púlsame", command=Pulsar)
boton.grid(column=1, row=3)

# Imagen decorativa
imagen = PhotoImage(file="C:/Users/izaiamn854/Documents/Python/Prueba/dni.png")
fondo = Label(ventana, image=imagen).place(x=220, y=10)  # Descomenta si tienes la imagen

ventana.mainloop()