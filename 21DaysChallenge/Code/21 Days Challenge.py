import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import *
from tkinter.ttk import *
import requests
import json
from PIL import ImageTk, Image

class HabitTrackerApp:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Habit Tracker")
        self.root.iconbitmap("Icon.ico")
        self.root.geometry("400x500")  # Set window size
        self.root.resizable(False,False)

        self.img = ImageTk.PhotoImage(Image.open("Icon2.png"))

        # Create a notebook for multiple checklists
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill="both")

        # Style
        self.s = Style()
        self.s.configure('My.TFrame', background='#f2f2f1')

        # Welcome screen
        self.welcome_frame = ttk.Frame(self.notebook, style='My.TFrame')
        self.notebook.add(self.welcome_frame, text="Welcome")

        welcome_label = tk.Label(
            self.welcome_frame,
            text="21 Days Challenge\nGet ready to build positive habits.\n\n",
            font=("Comic Sans MS", 18),
            pady=60,
            padx=30,
            bg="#313131",
            fg="white"
        )
        welcome_label.place(relx=0.5, rely=0.2, anchor="center")

        quote_label = tk.Label(
            self.welcome_frame,
            text=": QUOTE :\n"+self.fetch_quote(),
            font=("Comic Sans MS", 12),
            wraplength=400,
            pady=50,
            padx=40,
            bg="#f2f2f1",
            fg="#1c1c1e"
        )
        quote_label.place(relx = 0.5, rely = 0.5, anchor = "center")

        img_label=Label(self.welcome_frame, image = self.img)
        img_label.place(relx=0.5, rely=1.2, anchor="center")

        # Hamburger menu
        self.hamburger_menu = tk.Menu(self.root)
        self.root.config(menu=self.hamburger_menu)

        self.file_menu = tk.Menu(self.hamburger_menu, tearoff=0)
        self.hamburger_menu.add_cascade(label="Menu", menu=self.file_menu)
        self.file_menu.add_command(label="Add Checklist", command=self.add_checklist)
        
        # Load saved progress (after welcome screen creation)
        self.load_progress()

        # Run the Tkinter event loop
        self.root.mainloop()

    def mark_day(self, day, checklist_index):
        self.completed_days[checklist_index][day] = not self.completed_days[checklist_index][day]
        self.update_checkbox(day, checklist_index)

    def update_checkbox(self, day, checklist_index):
        self.checkbox_vars[checklist_index][day].set(self.completed_days[checklist_index][day])

    def save_progress(self, checklist_index):
        # Save the progress to a JSON file
        data = {"completed_days": self.completed_days, "checklist_names": self.checklist_names}
        with open("habit_data.json", "w") as json_file:
            json.dump(data, json_file)
        messagebox.showinfo("Save Progress", "Progress saved successfully!")

    def load_progress(self):
        try:
            # Load data from the JSON file
            with open("habit_data.json", "r") as json_file:
                data = json.load(json_file)

            # Check if "completed_days" key exists in the data
            if "completed_days" in data:
                self.completed_days = data["completed_days"]
                self.checkbox_vars = [[tk.BooleanVar() for _ in range(21)] for _ in range(len(self.completed_days))]

                # Load checklist names
                self.checklist_names = data.get("checklist_names", [])

                # Create checklists from loaded progress
                for i, completed_days_data in enumerate(self.completed_days):
                    checklist_name = self.checklist_names[i] if i < len(self.checklist_names) else f"Checklist {i + 1}"
                    self.create_checklist(checklist_name, i)
        except (json.JSONDecodeError, FileNotFoundError):
            self.completed_days = []
            self.checkbox_vars = []
            self.checklist_names = []

    def fetch_quote(self):
        try:
            response = requests.get("https://api.quotable.io/random")
            data = response.json()
            return data["content"]
        except requests.RequestException as e:
            print(f"Error fetching quote: {e}")
            return "Progress May Be Slow,\nBut Quitting Won't Speed It Up.\nStay The Course, And You'll Achieve Your Goals!\n"

    def add_checklist(self):
        new_checklist_name = simpledialog.askstring("Add Checklist", "Enter the name for the new checklist:")
        if new_checklist_name:
            self.completed_days.append([False] * 21)
            self.checkbox_vars.append([tk.BooleanVar() for _ in range(21)])
            self.checklist_names.append(new_checklist_name)
            self.create_checklist(new_checklist_name, len(self.completed_days) - 1)
            self.save_progress(len(self.completed_days) - 1)  # Save progress for the new checklist

    def create_checklist(self, checklist_name, checklist_index):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=checklist_name)

        heading_label = tk.Label(
            frame,
            text=checklist_name,
            font=("Comic Sans MS", 16),
            pady=10,
            bg="#b7b7a4",  # Blue background color
            fg="#000",   # White text color
            borderwidth=2, 
            relief="solid"
        )
        heading_label.grid(row=0, column=0, columnspan=6, rowspan=2, sticky="nsew")

        for row in range(6):
            for col in range(4):
                day = row * 4 + col
                if day < 21:
                    checkbox_var = self.checkbox_vars[checklist_index][day]

                    checkbox = tk.Checkbutton(
                        frame,
                        text=f"Day {day + 1}",
                        variable=checkbox_var,
                        command=lambda d=day, ci=checklist_index: self.mark_day(d, ci),
                        font=("Comic Sans MS", 14),
                        bg="#ecf0f1",  # Light gray background color
                        fg="#6b705c",  # Dark gray text color
                        relief="flat",
                    )
                    checkbox.grid(row=row + 2, column=col, padx=5, pady=5, sticky="nsew")

                    # Update the checkbox state based on the completion status
                    self.update_checkbox(day, checklist_index)

        # Save progress button with a styled appearance
        save_button = tk.Button(
            frame,
            text="Save Progress",
            command=lambda ci=checklist_index: self.save_progress(ci),
            font=("Comic Sans MS", 14, "bold"),
            #bg="#2ecc71",  # Green background color
            fg="#6b705c",    # White text color
            relief="flat",
        )
        save_button.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")

        # Delete checklist button with a styled appearance
        delete_button = tk.Button(
            frame,
            text="Delete Checklist",
            command=lambda ci=checklist_index: self.delete_checklist(ci),
            font=("Comic Sans MS", 14, "bold"),
            #bg="#e74c3c",  # Red background color
            fg="#cb997e",    # White text color
            relief="flat",
        )
        delete_button.grid(row=8, column=2, columnspan=3, pady=5, sticky="nsew")

        # Configure row and column weights
        for i in range(7):
            frame.grid_rowconfigure(i + 1, weight=1)
            frame.grid_columnconfigure(i, weight=1)

    def delete_checklist(self, checklist_index):
        # Ask for confirmation before deleting the checklist
        answer = messagebox.askyesno("Delete Checklist", "Are you sure you want to delete this checklist?")
        if answer:
            self.notebook.forget(self.notebook.index("current"))
            self.completed_days.pop(checklist_index)
            self.checkbox_vars.pop(checklist_index)
            self.checklist_names.pop(checklist_index)
            self.save_all_progress()  # Save progress for all checklists

    def save_all_progress(self):
        # Save the progress for all checklists to a JSON file
        data = {"completed_days": self.completed_days, "checklist_names": self.checklist_names}
        with open("habit_data.json", "w") as json_file:
            json.dump(data, json_file)
        messagebox.showinfo("Save Progress", "Progress saved successfully!")

# Instantiate the application
habit_tracker_app = HabitTrackerApp()
