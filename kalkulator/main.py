import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class Frame1(ctk.CTkFrame):
    def __init__(self, master, log_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.log_callback = log_callback

        input_frame = ctk.CTkFrame(self)
        input_frame.pack(side=ctk.TOP, pady=5)

        self.entry_data = ctk.CTkEntry(input_frame)
        self.entry_data.pack(side=ctk.LEFT)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(side=ctk.TOP, pady=5)

        buttons = [
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("0", "0"),
            ("+", "+"),
            ("-", "-"),
            ("*", "*"),
            ("/", "/"),
            ("(", "("),
            (")", ")"),
            (".", "."),
            ("=", self.evaluate)
        ]

        for label, value in buttons:
            button = ctk.CTkButton(button_frame, text=label, command=lambda v=value: self.update_entry(v))
            button.pack(side=ctk.LEFT, padx=5)

        self.eval_button = ctk.CTkButton(input_frame, text="Submit", command=self.evaluate)
        self.eval_button.pack(side=ctk.LEFT, padx=5)

        return_frame = ctk.CTkFrame(self)
        return_frame.pack(side=ctk.TOP, pady=5)

        return_label = ctk.CTkLabel(return_frame, text="Return:")
        return_label.pack(side=ctk.LEFT)

        self.result_label = ctk.CTkLabel(return_frame, text="", width=300, height=1)
        self.result_label.pack(side=ctk.LEFT)

    def update_entry(self, value):
        current_value = self.entry_data.get()
        self.entry_data.delete(0, "end")
        self.entry_data.insert("end", current_value + value)

    def evaluate(self):
        data = self.entry_data.get()

        try:
            result = eval(data)
            self.result_label.configure(text=str(result))

            self.log_callback("Result: " + str(result))
        except Exception as e:
            self.result_label.configure(text="Error: " + str(e))



class Frame2(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create a list to hold log frames
        self.log_frames = []

    def add_log(self, log):
        # Create a frame to contain the log label
        log_frame = ctk.CTkFrame(self, fg_color="#161621", border_color="dark-blue")
        log_frame.pack(side=ctk.TOP, fill="both", padx=10, pady=5)

        # Create and add the log label to the frame
        log_label = ctk.CTkLabel(log_frame, text=log)
        log_label.pack(side=ctk.LEFT)

        # Append the log frame to the list of log frames
        self.log_frames.append(log_frame)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Kalkulator"
        self.geometry("800x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        # Create an array to hold Frame1 instances
        self.frame1_array = []

        # Create Frame2 instance
        self.frame2 = Frame2(master=self)
        self.frame2.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Create and append Frame1 instances to the array
        for i in range(3):  # For example, create 3 Frame1 instances
            frame1_instance = Frame1(master=self, log_callback=self.frame2.add_log)
            frame1_instance.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
            self.frame1_array.append(frame1_instance)


app = App()
app.title = "Kalkulator"
app.mainloop()