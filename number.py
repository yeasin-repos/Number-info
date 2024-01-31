import tkinter as tk
from tkinter import ttk, messagebox
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_phone_info():
    input_number = phone_number_entry.get()

    try:
        parsed_number = phonenumbers.parse(input_number)
        time_zones = timezone.time_zones_for_number(parsed_number)
        carrier_name = carrier.name_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "en")

        info_text = f"Phone Number: {parsed_number}\n"
        info_text += f"Time Zones: {', '.join(time_zones)}\n"
        info_text += f"Carrier: {carrier_name}\n"
        info_text += f"Region: {region}"

        result_text.config(text=info_text)

    except phonenumbers.NumberParseException:
        messagebox.showerror("Error", "Invalid phone number format")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Phone Number Info")
root.configure(bg="#282c34")

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), foreground="#9966CC",background="#282c34")
style.configure("TButton", font=("Helvetica", 12), foreground="#9966CC", background='#282c34')

# Create and set up the GUI components
phone_label = ttk.Label(root, text="Enter your phone number (with country code):")
phone_number_entry = ttk.Entry(root, font=("Helvetica", 12))
get_info_button = ttk.Button(root, text="Get Info", command=get_phone_info)
result_text = ttk.Label(root, text="", justify="left", font=("Helvetica", 12), foreground="#9966CC")

# Place the components on the window
phone_label.pack(pady=10)
phone_number_entry.pack(pady=10)
get_info_button.pack(pady=10)
result_text.pack(pady=10)

# Start the main loop
root.mainloop()
