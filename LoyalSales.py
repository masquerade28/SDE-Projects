import customtkinter as ctk

class LoyalSales:
    def __init__(self,root):
        self.root = root
        self.root.title("Loyal Sales")
        self.root.geometry("1000x650")
        self.root.iconbitmap("Icon.ico")
        self.root.resizable(0, 0)

        self.main_title = ctk.CTkLabel(self.root, text="Loyal Sales", font=ctk.CTkFont(family="Comic Sans MS", size=40, weight="bold"))
        self.main_title.pack()

        self.left_frame = ctk.CTkFrame(root, border_width=2)
        self.left_frame.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.BOTH, expand=True)

        self.right_frame = ctk.CTkFrame(root, border_width=2)
        self.right_frame.pack(side=ctk.RIGHT, padx=10, pady=10, fill=ctk.BOTH, expand=True)

        self.machineprice_label = ctk.CTkLabel(self.left_frame, text="Machine Price", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.machineprice_label.place(relx=0.05, rely=0.1)
        self.machineprice_entry = ctk.CTkEntry(self.left_frame,placeholder_text="Machine Price ($)", width=225)
        self.machineprice_entry.place(relx=0.5, rely=0.1)

        self.shipmentprice_label = ctk.CTkLabel(self.left_frame, text="Shipment Price", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.shipmentprice_label.place(relx=0.05, rely=0.2)
        self.shipmentprice_entry = ctk.CTkEntry(self.left_frame,placeholder_text="Shipment Price ($)", width=225)
        self.shipmentprice_entry.place(relx=0.5, rely=0.2)

        self.dollarprice_label = ctk.CTkLabel(self.left_frame, text="Dollar Price (Rs.)", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.dollarprice_label.place(relx=0.05, rely=0.3)
        self.dollarprice_entry = ctk.CTkEntry(self.left_frame,placeholder_text="Dollar Price", width=225)
        self.dollarprice_entry.place(relx=0.5, rely=0.3)

        self.customduty_label = ctk.CTkLabel(self.left_frame, text="Custom Duty", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.customduty_label.place(relx=0.05, rely=0.4)
        self.customduty_entry = ctk.CTkEntry(self.left_frame,placeholder_text="Custom Duty (%)", width=225)
        self.customduty_entry.place(relx=0.5, rely=0.4)

        self.tiwariji_label = ctk.CTkLabel(self.left_frame, text="Extra Expenses", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.tiwariji_label.place(relx=0.05, rely=0.5)
        self.tiwariji_entry = ctk.CTkEntry(self.left_frame,placeholder_text="Extra Expenses (Rs.)", width=225)
        self.tiwariji_entry.place(relx=0.5, rely=0.5)

        self.profit_label = ctk.CTkLabel(self.left_frame, text="Profit", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.profit_label.place(relx=0.05, rely=0.6)
        self.profit_entry = ctk.CTkEntry(self.left_frame,placeholder_text="Profit (Rs.)", width=225)
        self.profit_entry.place(relx=0.5, rely=0.6)

        self.gst_label = ctk.CTkLabel(self.left_frame, text="GST", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.gst_label.place(relx=0.05, rely=0.7)
        self.gst_entry = ctk.CTkEntry(self.left_frame,placeholder_text="18%", width=225)
        self.gst_entry.place(relx=0.5, rely=0.7)
        self.gst_entry.configure(state="disabled")

        self.generate_button = ctk.CTkButton(self.left_frame, text="Generate Bill",command= self.bill, font=ctk.CTkFont(family="Comic Sans MS", size=15), hover_color="#801000", fg_color="#3bb143")
        self.generate_button.place(relx=0.1, rely=0.85)

        self.clear_button = ctk.CTkButton(self.left_frame, text="Clear",command= self.clear, font=ctk.CTkFont(family="Comic Sans MS", size=15), hover_color="#3bb143", fg_color="#800000")
        self.clear_button.place(relx=0.6, rely=0.85)

        self.billarea_title = ctk.CTkLabel(self.right_frame, text="=========== Bill Area ===========", font=ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold"))
        self.billarea_title.place(relx=0.02, rely=0.05)

    def bill(self):
        a = float(self.machineprice_entry.get())
        b = float(self.shipmentprice_entry.get())
        c = a + b
        d = float(self.dollarprice_entry.get())
        e = d * c
        f = float(self.customduty_entry.get())
        g = (e * f)/100
        s = g + e
        x = float(self.tiwariji_entry.get())
        x1 = x + s
        p = float(self.profit_entry.get())
        p1 = p + x1
        price = (p1 * 18)/100
        price1 = price + p1

        label1 = ctk.CTkLabel(self.right_frame, text="=============================", font=ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold"))
        label1.place(relx=0.05, rely=0.1)

        self.machineprice = ctk.CTkLabel(self.right_frame, text=f"Machine Price : $ {a}", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.machineprice.place(relx=0.05, rely=0.2)

        self.shipmentprice = ctk.CTkLabel(self.right_frame, text=f"Shipment Price : $ {b}", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.shipmentprice.place(relx=0.05, rely=0.3)

        self.dollar = ctk.CTkLabel(self.right_frame, text=f"Dollar Price : Rs. {d}", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.dollar.place(relx=0.05, rely=0.4)

        self.customduty = ctk.CTkLabel(self.right_frame, text=f"Custom Duty : {f} %", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.customduty.place(relx=0.05, rely=0.5)

        self.tiwariji = ctk.CTkLabel(self.right_frame, text=f"Extra Expenses : Rs. {x}", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.tiwariji.place(relx=0.05, rely=0.6)

        self.profit = ctk.CTkLabel(self.right_frame, text=f"Profit : Rs. {p}", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.profit.place(relx=0.05, rely=0.7)

        label2 = ctk.CTkLabel(self.right_frame, text="=============================", font=ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold"))
        label2.place(relx=0.05, rely=0.8)

        self.finalprice = ctk.CTkLabel(self.right_frame, text=f"Final Price : Rs. {price1}", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
        self.finalprice.place(relx=0.05, rely=0.9)

    def clear(self):
        for widget in self.right_frame.winfo_children():
            if widget == self.billarea_title:
                continue
            else:
                widget.destroy()

        self.machineprice_entry.delete(0, ctk.END)
        self.shipmentprice_entry.delete(0, ctk.END)
        self.dollarprice_entry.delete(0, ctk.END)
        self.customduty_entry.delete(0, ctk.END)
        self.tiwariji_entry.delete(0, ctk.END)
        self.profit_entry.delete(0, ctk.END)
        

if __name__ == "__main__":
    root = ctk.CTk()
    app = LoyalSales(root)
    root.mainloop()