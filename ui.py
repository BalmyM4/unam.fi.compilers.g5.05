import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter import ttk

# ------------------------------------------------------------------------- #
# ---------------------------- Utility functions -------------------------- #
# ------------------------------------------------------------------------- #


# Open a file and display its content in the text area.
def open_file():
    
    # Get the file path
    file_path = filedialog.askopenfilename( filetypes=[("Text files", "*.txt")] )


    # If a file is selected, open it and display its contents
    if file_path:

        # Open the file and read its contents
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()

        # Clear the text area
        text_area.delete("1.0", tk.END)

        # Insert the file content into the text area
        text_area.insert(tk.END, file_content)



# Get text from the text area
def get_text():

    text = text_area.get("1.0", tk.END).strip()

    return text



# Analyze data
def analyze_text():
    
    # Get the text from the text area
    input_data = get_text()

    # If the text is empty, display an error message
    if not input_data:
        pass
    else:
        # Analyze the text
        result = """Texto analizado"""

        # Display the result
        result_area.insert(tk.END, result)



# Save the result into a file
def save_file():

    # Get the file path
    file_path = filedialog.asksaveasfilename( defaultextension=".txt", filetypes=[("Text files", "*.txt"),("All files", "*.*") ] )

    # If a file is selected, open it and display its contents
    if file_path:

        # Get the text from the text area
        result = result_area.get("1.0", tk.END).strip()

        # Save the text into the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(result)


# Clear the text area
def clear_text_area():
    text_area.delete("1.0", tk.END)


# Clear the result area
def clear_result_area():
    result_area.delete("1.0", tk.END)



# ------------------------------------------------------------------------- #
# ---------------------------------- Main --------------------------------- #
# ------------------------------------------------------------------------- #


# Create main window
root = tk.Tk()

# Set the title
root.title("Lexical Analyzer")

# Set the window size
root.geometry("700x900")


# Set the background color
root.config(bg="#24292e")


# ------------------------------------------------------------------------- #
# ---------------------------------- Head --------------------------------- #
# ------------------------------------------------------------------------- #

# Create a small frame for decoration
#decorative_frame1 = tk.Frame(root, height=5, bg="#36a3f7")
#decorative_frame1.pack(fill="x", pady=5)


# Function to move the window
def move_window(event):
    # Get the new window position
    root.geometry(f'+{event.x_root}+{event.y_root}')


# Remove the default title bar
root.overrideredirect(True)


# Create a frame for the custom title bar
title_bar = tk.Frame(root, bg="#1d2125", relief="raised", bd=0, height=30)
title_bar.pack(fill="x", side="top")


# Add a title to the title bar frame
title_label = tk.Label(title_bar, text="Lexical Analyzer", fg="white", bg="#1d2125", font=("Haettenschweiler", 18))
title_label.pack(side="left", padx=10)


# Load the image for the close button
close_image = tk.PhotoImage(file="resources/img/close.png")

# Create a button to close the window
close_button = tk.Button(title_bar, image=close_image, bg="#1d2125", bd=0, command=root.quit)
close_button.pack(side="right", padx=10)
close_button.config(activebackground="#1d2125", activeforeground="white")


# Make the title bar draggable
title_bar.bind("<B1-Motion>", move_window) # Detect movement with the left mouse button




# Create a small frame for decoration
decorative_frame2 = tk.Frame(root, height=5, bg="#814f05")
decorative_frame2.pack(fill="x", pady=5)



# ------------------------------------------------------------------------- #
# ---------------------------------- Body --------------------------------- #
# ------------------------------------------------------------------------- #


# Main frame
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, fill="both")
frame.config(bg="#24292e")



# ------------------------------------------------------------------------- #
# ------------------------------- Text area ------------------------------- #
# ------------------------------------------------------------------------- #


# Text area with scroll
text_area = scrolledtext.ScrolledText(frame, width=50, height=10, font=("Consolas", 14))
text_area.pack(pady=5, fill="both", expand=True)
text_area.config(bg="#444d56", fg="#ffffff")


# Button to select file
btn_open = tk.Button(frame, text="Open file", command=open_file)
btn_open.pack(pady=5, fill="x")
btn_open.config( font=("Arial Rounded MT Bold", 14, "bold"), 
                 relief="flat", 
                 bg="#0366d6", 
                 fg="#ffffff", 
                 activebackground="#24292e", 
                 activeforeground="#ffffff")


# Create a frame to hold the 'Analyze' and 'Clear' buttons
buttons_text_area_frame = tk.Frame(frame)
buttons_text_area_frame.pack(pady=5, fill="x")
buttons_text_area_frame.config(bg="#24292e")


# Configure the grid columns to expand
buttons_text_area_frame.grid_columnconfigure(0, weight=1)
buttons_text_area_frame.grid_columnconfigure(1, weight=1)


# Button to analyze
btn_analyze = tk.Button(buttons_text_area_frame, text="Analyze", command=analyze_text)
btn_analyze.grid(row=0, column=0, pady=5, sticky="ew", padx=5)
btn_analyze.config( font=("Arial Rounded MT Bold", 14, "bold"), 
                 relief="flat", 
                 bg="#23764f", 
                 fg="#ffffff", 
                 activebackground="#24292e", 
                 activeforeground="#ffffff")


# Button to clear the content
btn_clear_text = tk.Button(buttons_text_area_frame, text="Clear", command=clear_text_area)
btn_clear_text.grid(row=0, column=1, pady=5, sticky="ew", padx=5)
btn_clear_text.config( font=("Arial Rounded MT Bold", 14, "bold"), 
                 relief="flat", 
                 bg="#762344", 
                 fg="#ffffff", 
                 activebackground="#24292e", 
                 activeforeground="#ffffff")


# ------------------------------------------------------------------------- #
# ------------------------------ Result area ------------------------------ #
# ------------------------------------------------------------------------- #


# Scrollable text area
result_area = scrolledtext.ScrolledText(frame, width=50, height=10, font=("Consolas", 14))
result_area.pack(pady=5, fill="both", expand=True)
result_area.config(bg="#444d56", fg="#ffffff")


# Create a frame to hold the 'Save file' and 'Clear' buttons
buttons_result_area_frame = tk.Frame(frame)
buttons_result_area_frame.pack(pady=5, fill="x")
buttons_result_area_frame.config(bg="#24292e")


# Configure the grid columns to expand
buttons_result_area_frame.grid_columnconfigure(0, weight=1)
buttons_result_area_frame.grid_columnconfigure(1, weight=1)


# Button to save file
btn_save = tk.Button(buttons_result_area_frame, text="Save file", command=save_file)
btn_save.grid(row=0, column=0, pady=5, sticky="ew", padx=5)
btn_save.config( font=("Arial Rounded MT Bold", 14, "bold"), 
                 relief="flat", 
                 bg="#0366d6", 
                 fg="#ffffff", 
                 activebackground="#24292e", 
                 activeforeground="#ffffff")


# Button to clear content
btn_clear_result = tk.Button(buttons_result_area_frame, text="Clear", command=clear_result_area)
btn_clear_result.grid(row=0, column=1, pady=5, sticky="ew", padx=5)
btn_clear_result.config( font=("Arial Rounded MT Bold", 14, "bold"), 
                 relief="flat", 
                 bg="#762344", 
                 fg="#ffffff", 
                 activebackground="#24292e", 
                 activeforeground="#ffffff")



# ------------------------------------------------------------------------- #
# ------------------------------- Main loop ------------------------------- #
# ------------------------------------------------------------------------- #


root.mainloop()
