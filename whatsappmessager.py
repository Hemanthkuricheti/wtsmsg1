import tkinter as tk
import pywhatkit

def send_whatsapp_message():
    mobile_number = mobile_entry.get()
    message = message_entry.get()
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    
    pywhatkit.sendwhatmsg(mobile_number, message, hours, minutes)

# Create the main window
root = tk.Tk()
root.title("WhatsApp Message Sender")

# Labels
mobile_label = tk.Label(root, text="Mobile Number:")
message_label = tk.Label(root, text="Message:")
time_label = tk.Label(root, text="Send Time (HH:MM):")

# Entry fields
mobile_entry = tk.Entry(root)
message_entry = tk.Entry(root)
hours_entry = tk.Entry(root)
minutes_entry = tk.Entry(root)

# Send Button
send_button = tk.Button(root, text="Send Message", command=send_whatsapp_message)

# Layout using grid
mobile_label.grid(row=0, column=0)
message_label.grid(row=1, column=0)
time_label.grid(row=2, column=0)
mobile_entry.grid(row=0, column=1)
message_entry.grid(row=1, column=1)
hours_entry.grid(row=2, column=1)
minutes_entry.grid(row=2, column=2)
send_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
