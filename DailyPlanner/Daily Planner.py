import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from datetime import datetime

class DailyPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Planner") 
        self.root.iconbitmap('Icon.ico')
        self.root.state('zoomed')

        # Styling
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Comic Sans MS", 14), foreground="#333")
        self.style.configure("TButton", font=("Comic Sans MS", 12))
        self.style.configure("TEntry", font=("Comic Sans MS", 12))
        
        # Left Frame for Todo List and Notes
        self.left_frame = ttk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.left_frame.grid_propagate(False)  # Prevent auto-sizing

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)

        self.label_todo = ttk.Label(self.left_frame, text="TODO LIST", font=("Comic Sans MS", 14, "bold"))
        self.date_label = tk.Label(self.left_frame, text="", font=("Comic Sans MS", 12))
        self.label_todo.pack()
        self.date_label.pack(anchor='nw')

        self.task_listbox = tk.Listbox(self.left_frame, background="#d6e4cb", foreground="#787d63", selectbackground="#d6e4cb", selectforeground="#000", activestyle="none", font=("Comic Sans MS", 12), width=30, bd=1, relief=tk.SOLID)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        self.add_task_frame = ttk.Frame(self.left_frame,border=1)
        self.add_task_frame.pack(fill=tk.X, pady=5)

        self.add_task_entry = ttk.Entry(self.add_task_frame, font=("Comic Sans MS", 12))
        self.add_task_entry.pack(fill=tk.BOTH, expand=True)

        self.button_frame = ttk.Frame(self.left_frame)
        self.button_frame.pack(fill=tk.X, pady=5)

        self.add_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.pack(side=tk.LEFT,padx=500)

        self.complete_button = ttk.Button(self.button_frame, text="Mark Complete", command=self.mark_complete, style="TButton")
        self.complete_button.pack(side=tk.LEFT)

        self.label_notes = ttk.Label(self.left_frame, text="NOTES", font=("Comic Sans MS", 14, "bold"))
        self.label_notes.pack(pady = 5)

        self.notes_text = tk.Text(self.left_frame, wrap=tk.WORD, font=("Comic Sans MS", 12), height=10, width=30, relief=tk.SOLID, borderwidth=0, bg="#f8f2e2", fg="#787d63",bd=1)
        self.notes_text.pack(fill=tk.BOTH, expand=True)

        self.save_button = ttk.Button(self.left_frame, text="Save", command=self.save_data, style="TButton")
        self.save_button.pack(pady=10, padx=500, side=tk.LEFT)  # Adjust padx to center the button

        self.reset_button = ttk.Button(self.left_frame, text="Reset", command=self.reset_data, style="TButton")
        self.reset_button.pack(pady=10, side=tk.LEFT)  # Adjust padx to center the button

        # Right Frame for Time Stamps and Inputs
        self.right_frame = ttk.Frame(root)
        self.right_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.label_time = ttk.Label(self.right_frame, text="SCHEDULES", font=("Comic Sans MS", 13, "bold"))
        self.label_time.pack(pady = 5)

        self.time_entries = []

        for hour in range(6, 24):
            time_str = f"{hour:02d}:00 {'AM' if hour < 12 else 'PM'}"
            time_label = ttk.Label(self.right_frame, text=time_str, font=("Comic Sans MS", 10, "bold"))
            time_label.pack(anchor=tk.W)

            time_entry = ttk.Entry(self.right_frame, font=("Comic Sans MS", 12), style="TEntry")
            time_entry.pack(fill=tk.BOTH, expand=True)
            self.time_entries.append(time_entry)

        # Load saved data
        self.load_saved_data()

        self.update_date()

    def add_task(self):
        task = '-> ' + self.add_task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.add_task_entry.delete(0, tk.END)

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task_text = self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            if "~" in task_text:
                self.task_listbox.insert(tk.END, '-> '+ task_text[2:-2])
                self.task_listbox.itemconfig(tk.END, {'fg': '#999'})
            else:
                self.task_listbox.insert(tk.END,f"~~{task_text[3::]}~~")
                self.task_listbox.itemconfig(tk.END, {'fg': '#787d63'})

    def load_saved_data(self):
        try:
            with open("daily_planner_data.txt", "r") as file:
                data = file.read()
                sections = data.split("===SEPARATOR===")

                if len(sections) >= 3:
                    task_data = sections[0].strip().split("\n")
                    time_data = sections[1].strip().split("\n")
                    notes_data = sections[2].strip()

                    for task in task_data:
                        self.task_listbox.insert(tk.END, task)

                    for i, time_entry in enumerate(self.time_entries):
                        if i < len(time_data):
                            time_entry.insert(0, time_data[i])

                    self.notes_text.delete(1.0, tk.END)
                    self.notes_text.insert(tk.END, notes_data)

        except FileNotFoundError:
            pass

    def save_data(self):
        tasks = "\n".join(self.task_listbox.get(0, tk.END))
        times = "\n".join([entry.get() for entry in self.time_entries])
        notes = self.notes_text.get(1.0, tk.END)

        with open("daily_planner_data.txt", "w") as file:
            file.write(f"{tasks}\n===SEPARATOR===\n{times}\n===SEPARATOR===\n{notes}")

    def reset_data(self):
        self.task_listbox.delete(0, tk.END)
        for time_entry in self.time_entries:
            time_entry.delete(0, tk.END)
        self.notes_text.delete(1.0, tk.END)

    def update_date(self):
        current_date = datetime.now().strftime("%d %B %Y, %A")
        self.date_label.config(text=current_date)

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyPlannerApp(root)
    root.mainloop()
