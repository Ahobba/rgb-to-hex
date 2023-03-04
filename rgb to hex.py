import pyperclip
import tkinter as tk

def rgb_to_hex(r, g, b):
    """Converte um valor RGB em um código hexadecimal."""
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def copy_to_clipboard(value):
    """Copia o valor para a área de transferência."""
    pyperclip.copy(value)

    # Atualiza o valor exibido na interface
    color_label.config(text=f"Copied: {value}")

# Cria uma janela
window = tk.Tk()
window.title("RGB to Hex Converter")

# Adiciona um campo de entrada para os valores RGB
r_entry = tk.Entry(window)
g_entry = tk.Entry(window)
b_entry = tk.Entry(window)
r_entry.pack(side=tk.LEFT)
g_entry.pack(side=tk.LEFT)
b_entry.pack(side=tk.LEFT)

# Adiciona um botão de conversão
convert_button = tk.Button(window, text="Convert", command=lambda: convert_and_display())
convert_button.pack(side=tk.LEFT)

# Adiciona um rótulo para exibir a cor copiada
color_label = tk.Label(window, text="")
color_label.pack(side=tk.LEFT, padx=10)

# Adiciona um quadrado para exibir a cor
color_frame = tk.Frame(window, width=50, height=50, bg="#000000")
color_frame.pack(side=tk.LEFT, padx=10)

def convert_and_display():
    # Obtém os valores RGB a partir dos campos de entrada
    r = int(r_entry.get())
    g = int(g_entry.get())
    b = int(b_entry.get())

    # Converte a cor para código hexadecimal
    color_hex = rgb_to_hex(r, g, b)

    # Copia o resultado para a área de transferência
    copy_to_clipboard(color_hex)

    # Atualiza a cor exibida no quadrado
    color_frame.config(bg=color_hex)

# Inicia a interface gráfica
window.mainloop()


p = input()
