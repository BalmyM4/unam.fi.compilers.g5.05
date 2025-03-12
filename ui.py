import tkinter as tk
from tkinter import filedialog, scrolledtext



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

# Set the icon
root.iconbitmap("img/icon.ico")


# Main frame
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, fill="both")



# ------------------------------------------------------------------------- #
# ------------------------------- Text area ------------------------------- #
# ------------------------------------------------------------------------- #


# Text area with scroll
text_area = scrolledtext.ScrolledText(frame, width=50, height=10)
text_area.pack(pady=5, fill="both", expand=True)


# Button to select file
btn_open = tk.Button(frame, text="Open file", command=open_file)
btn_open.pack(pady=5, fill="x")


# Create a frame to hold the 'Analyze' and 'Clear' buttons
buttons_text_area_frame = tk.Frame(frame)
buttons_text_area_frame.pack(pady=5, fill="x")


# Configure the grid columns to expand
buttons_text_area_frame.grid_columnconfigure(0, weight=1)
buttons_text_area_frame.grid_columnconfigure(1, weight=1)


# Button to analyze
btn_analyze = tk.Button(buttons_text_area_frame, text="Analyze", command=analyze_text)
btn_analyze.grid(row=0, column=0, pady=5, sticky="ew", padx=5)


# Button to clear the content
btn_clear_text = tk.Button(buttons_text_area_frame, text="Clear", command=clear_text_area)
btn_clear_text.grid(row=0, column=1, pady=5, sticky="ew", padx=5)



# ------------------------------------------------------------------------- #
# ------------------------------ Result area ------------------------------ #
# ------------------------------------------------------------------------- #


# Scrollable text area
result_area = scrolledtext.ScrolledText(frame, width=50, height=10)
result_area.pack(pady=5, fill="both", expand=True)


# Create a frame to hold the 'Save file' and 'Clear' buttons
buttons_result_area_frame = tk.Frame(frame)
buttons_result_area_frame.pack(pady=5, fill="x")


# Configure the grid columns to expand
buttons_result_area_frame.grid_columnconfigure(0, weight=1)
buttons_result_area_frame.grid_columnconfigure(1, weight=1)


# Button to save file
btn_save = tk.Button(buttons_result_area_frame, text="Save file", command=save_file)
btn_save.grid(row=0, column=0, pady=5, sticky="ew", padx=5)


# Button to clear content
btn_clear_result = tk.Button(buttons_result_area_frame, text="Clear", command=clear_result_area)
btn_clear_result.grid(row=0, column=1, pady=5, sticky="ew", padx=5)



# ------------------------------------------------------------------------- #
# ------------------------------- Main loop ------------------------------- #
# ------------------------------------------------------------------------- #


# Ejecutar la ventana
root.mainloop()
