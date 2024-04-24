# author: @Aksel
# todo: få commitment issues

#
# Bruker en custom versjon av TKinter for GUI
# denne gir en mer "modern" stil
#
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

#
# Lager "framen" hvor selve kalkuleringene skal skje
#
class Frame1(ctk.CTkFrame):
    #
    # dette er default config for en class med dette librariet
    #
    def __init__(self, master, log_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.log_callback = log_callback

        input_frame = ctk.CTkFrame(self)
        input_frame.pack(side=ctk.TOP, pady=5)

        self.entry_data = ctk.CTkEntry(input_frame)
        self.entry_data.pack(side=ctk.LEFT)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(side=ctk.TOP, pady=5)

        #
        # dette er hvordan jeg skal generere knappene
        # vennligst ikke spør meg om hva dette er :D
        # tune in til min presse konferanse på skolen på fredag om hva dette er
        #
        buttons = [
            ("1", "1"), ("2", "2"), ("3", "3"),
            ("4", "4"), ("5", "5"), ("6", "6"),
            ("7", "7"), ("8", "8"), ("9", "9"),
            ("+", "+"), ("-", "-"), ("*", "*"),
            ("0", "0"), (".", "."), ("/", "/"),
            ("Clear", self.clear_entry)
        ]

        #
        # Legger buttins array inn i en button grid på ~5x3
        # for hvert label og value i buttons så vil den lage en ny button og endre column når den når 3 og deretter
        # fortsette på en ny row
        #

        row_count = 0
        column_count = 0
        for label, value in buttons:
            button = ctk.CTkButton(button_frame, text=label, command=lambda v=value: self.on_button_click(v))
            button.grid(row=row_count, column=column_count, padx=5, pady=5)
            column_count += 1
            if column_count == 3:
                column_count = 0
                row_count += 1

        self.eval_button = ctk.CTkButton(input_frame, text="Submit", command=self.evaluate)
        self.eval_button.pack(side=ctk.LEFT, padx=5)

        return_frame = ctk.CTkFrame(self)
        return_frame.pack(side=ctk.TOP, pady=5)

        return_label = ctk.CTkLabel(return_frame, text="Return:")
        return_label.pack(side=ctk.LEFT)

        self.result_label = ctk.CTkLabel(return_frame, text="", width=300, height=1)
        self.result_label.pack(side=ctk.LEFT)

    #
    # denne funksjonen blir brukt med clear_entry() for å slette ting on click
    #
    def on_button_click(self, value):
        if value == "Clear":
            self.clear_entry()
        else:
            self.update_entry(value)

    def update_entry(self, value):
        current_value = self.entry_data.get()
        self.entry_data.delete(0, "end")
        self.entry_data.insert("end", current_value + value)

    #
    # simpel slette funksjon for et entry i input label
    #
    def clear_entry(self):
        self.entry_data.delete(0, "end")

    #
    # Hoved funksjonen for koden
    # denne tar å gjør all matten i koden
    # vil ta input som en string og sal da gi den videre til Frame2
    #
    def evaluate(self):
        data = self.entry_data.get()

        try:
            result = eval(data)
            self.result_label.configure(text=str(result))

            self.log_callback("Result: " + str(result))
        except Exception as e:
            self.result_label.configure(text="Error: " + str(e))

#
# Dette er resultat Framen, den skal være scrollbar og gi deg tilgang til å se tidligere inputs
#
class Frame2(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.log_frames = []

    def add_log(self, log):
        log_frame = ctk.CTkFrame(self, fg_color="#161621", border_color="dark-blue")
        log_frame.pack(side=ctk.TOP, fill="both", padx=10, pady=5)

        log_label = ctk.CTkLabel(log_frame, text=log)
        log_label.pack(side=ctk.LEFT)

        self.log_frames.append(log_frame)


#
# Main class
# Her ligger alt default configs og fungerer isj som et entry point
# dette er som en config for applikasjonen og gir essensiell info på programmet
#
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Kalkulator"
        self.geometry("800x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.frame1_array = []

        self.frame2 = Frame2(master=self)
        self.frame2.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        #
        # for loop for å lage selve log labels
        #
        # lager en for hver instance av en frame2.add_logg funksjon som kjører
        #
        # så hver gang den kjører så vil frame1_instance lage en frame
        # så vi den få en grid og deretter bli appendet til
        #

        for i in range(3):
            frame1_instance = Frame1(master=self, log_callback=self.frame2.add_log)
            frame1_instance.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
            self.frame1_array.append(frame1_instance)

#
# dettan er hvor koden kjører fra
# app.mainloop sier bare hva som skjer om koden når dit igjen så den vil gå slik
##############################################################################
#
#                          app -> app.mainloop() -|
#                            |-return to root  <-|
#
###############################################################################
#

app = App()
app.title = "Kalkulator"
app.mainloop()