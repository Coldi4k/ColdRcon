import tkinter as tk
import json
import subprocess
import os

# Paths for profiles file
home_path = os.path.expanduser('~')
data_folder_path = os.path.join(home_path, '.ColdRcon-data')
profiles_file_path = os.path.join(data_folder_path, 'profiles.json')

# Ensure the .ColdRcon-data directory exists
os.makedirs(data_folder_path, exist_ok=True)

# Check if profiles file exists and load profiles data
profiles_data = {'server_ip': '', 'server_port': '', 'password': ''}
if os.path.exists(profiles_file_path):
    with open(profiles_file_path, 'r') as profiles_file:
        profiles_data = json.load(profiles_file)

# Function to save profiles data
def save_profiles():
    profiles_data['server_ip'] = ip_entry.get()
    profiles_data['server_port'] = port_entry.get()
    profiles_data['password'] = password_entry.get()
    with open(profiles_file_path, 'w') as profiles_file:
        json.dump(profiles_data, profiles_file)

# Function to load the last profile
def load_last_profile():
    ip_entry.delete(0, tk.END)
    ip_entry.insert(0, profiles_data['server_ip'])
    port_entry.delete(0, tk.END)
    port_entry.insert(0, profiles_data['server_port'])
    password_entry.delete(0, tk.END)
    password_entry.insert(0, profiles_data['password'])

# Function to handle disconnect action
def disconnect_action():
    command_entry.pack_forget()
    send_button.pack_forget()
    console_label.pack_forget()
    disconnect_button.pack_forget()
    ip_label.pack()
    spacesl1.pack()
    ip_entry.pack()
    spacese1.pack()
    port_label.pack()
    spacesl2.pack()
    port_entry.pack()
    spacese2.pack()
    password_label.pack()
    spacesl3.pack()
    password_entry.pack()
    spaces.pack()
    connect_button.pack()
    spaces2.pack()
    save_profiles_button.pack()
    spaces3.pack()
    load_profile_button.pack()

# Function to setup connection
def setup_connection():
    try:
        server_ip = ip_entry.get()
        server_port = port_entry.get()
        password = password_entry.get()
        ip_label.pack_forget()
        spacesl1.pack_forget()
        ip_entry.pack_forget()
        spacese1.pack_forget()
        port_label.pack_forget()
        spacesl2.pack_forget()
        port_entry.pack_forget()
        spacese2.pack_forget()
        password_label.pack_forget()
        spacesl3.pack_forget()
        password_entry.pack_forget()
        spacese3.pack_forget()
        spaces.pack_forget()
        connect_button.pack_forget()
        spaces2.pack_forget()
        save_profiles_button.pack_forget()
        spaces3.pack_forget()
        load_profile_button.pack_forget()
        command_entry.pack()
        send_button.pack()
        console_label.pack()
        root.server_ip = server_ip
        root.server_port = server_port
        root.password = password
        disconnect_button.pack()
    except Exception as e:
        console_label.config(text=f'Error setting up connection: {e}')

# Function to send command
def send_command():
    try:
        command = command_entry.get()
        full_command = f'{mcrcon_path} -H {root.server_ip} -P {root.server_port} -p {root.password} "{command}"'
        result = subprocess.check_output(full_command, shell=True, text=True)
        console_label.config(text=f'Command executed: {command}\nResponse: {result}')
    except Exception as e:
        console_label.config(text=f'Error executing command: {e}')

# Main GUI setup
root = tk.Tk()
root.title('ColdRcon')
root.geometry('1000x500')
root.iconbitmap('icon.ico')
root.configure(bg='#313335')

# UI Elements
ip_label = tk.Label(root, text='Server IP:', font=('Helvetica', 14), fg='white', bg='#313335')
spacesl1 = tk.Button(root, bg='#313335', border=0, state='disabled')
spacesl1.pack_forget()
ip_entry = tk.Entry(root, font=('Helvetica', 14), bg='#F9FBE7', fg='black', borderwidth=2, relief='solid')
spacese1 = tk.Button(root, bg='#313335', border=0, state='disabled')
spacese1.pack_forget()
port_label = tk.Label(root, text='Rcon Port:', font=('Helvetica', 14), fg='white', bg='#313335')
spacesl2 = tk.Button(root, bg='#313335', border=0, state='disabled')
spacesl2.pack_forget()
port_entry = tk.Entry(root, font=('Helvetica', 14), bg='#F9FBE7', fg='black', borderwidth=2, relief='solid')
spacese2 = tk.Button(root, bg='#313335', border=0, state='disabled')
spacese2.pack_forget()
password_label = tk.Label(root, text='Rcon Password:', font=('Helvetica', 14), fg='white', bg='#313335')
spacesl3 = tk.Button(root, bg='#313335', border=0, state='disabled')
spacesl3.pack_forget()
password_entry = tk.Entry(root, font=('Helvetica', 14), bg='#F9FBE7', fg='black', borderwidth=2, relief='solid')
spacese3 = tk.Button(root, bg='#313335', border=0, state='disabled')
spacese3.pack_forget()
spaces = tk.Button(root, bg='#313335', border=0, state='disabled')
spaces.pack_forget()
connect_button = tk.Button(root, text='Connect', command=setup_connection, bg='#7345e5', fg='white', font=('Helvetica', 14))
ip_label.pack(pady=10)
ip_entry.pack(pady=10)
port_label.pack(pady=10)
port_entry.pack(pady=10)
password_label.pack(pady=10)
password_entry.pack(pady=10)
connect_button.pack(pady=10)
command_entry = tk.Entry(root, font=('Helvetica', 14), bg='#F9FBE7', fg='black', borderwidth=2, relief='solid')
command_entry.pack_forget()
send_button = tk.Button(root, text='Send', command=send_command, bg='#7345e5', fg='white', font=('Helvetica', 14))
send_button.pack_forget()
console_label = tk.Label(root, text='', font=('Helvetica', 16), fg='white', bg='#313335')
console_label.pack_forget()
disconnect_button = tk.Button(root, text='Disconnect', command=disconnect_action, bg='#FF5733', fg='white', font=('Helvetica', 14))
disconnect_button.pack_forget()
spaces2 = tk.Button(root, bg='#313335', border=0, state='disabled')
spaces2.pack_forget()
save_profiles_button = tk.Button(root, text='Save Profiles', command=save_profiles, bg='#7345e5', fg='white', font=('Helvetica', 14))
save_profiles_button.pack(pady=10)
spaces3 = tk.Button(root, bg='#313335', border=0, state='disabled')
spaces3.pack_forget()
load_profile_button = tk.Button(root, text='Load Last Profile', command=load_last_profile, bg='#FF5733', fg='white', font=('Helvetica', 14))
load_profile_button.pack(pady=10)
mcrcon_path = 'RconCore.exe'

# Start GUI loop
root.mainloop()
