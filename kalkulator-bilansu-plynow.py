import customtkinter as ctk

FONT = "Arial"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Kalkulator Bilansu Płynów")
app.geometry("500x500")
app.resizable(False, False)

def calculate_fluid_balance():
    if fluid_balance_menu.get() == "Wybierz typ bilansu":
        result_label.configure(text="Proszę wybrać typ bilansu płynów.")
        return
    
    if not all(entry.get().isdigit() for entry in [
        flow_rate_entry, iv_fluids_entry, oral_fluids_entry, urine_entry, vomit_entry]):
        
        result_label.configure(text="Proszę wprowadzić prawidłowe\nwartości liczbowe.")
        return
    
    hours_dictionary = {"6h": 6, "12h": 12, "24h": 24}

    result = int(flow_rate_entry.get()) * hours_dictionary[fluid_balance_menu.get()]
    result += int(iv_fluids_entry.get()) + int(oral_fluids_entry.get())
    result -= int(urine_entry.get()) + int(vomit_entry.get())
    
    if result < 0: result = 0

    result_label.configure(text=f"Pozostało do oddania {result} ml.")
    
    

fluid_balance_menu = ctk.CTkOptionMenu(
    app,
    values=["Wybierz typ bilansu", "6h", "12h", "24h"],
    font=(FONT, 20),
    width=400
)
fluid_balance_menu.pack(pady=20)

flow_rate_entry = ctk.CTkEntry(
    app,
    placeholder_text="Podaj szybkość przepływu kroplówki (ml/h)",
    font=(FONT, 20),
    width=400
)
flow_rate_entry.pack(pady=10)

iv_fluids_entry = ctk.CTkEntry(
    app,
    placeholder_text="Dodatkowe płyny dożylne (ml)",
    font=(FONT, 20),
    width=400
)
iv_fluids_entry.pack(pady=10)

oral_fluids_entry = ctk.CTkEntry(
    app,
    placeholder_text="Płyny doustne (ml)",
    font=(FONT, 20),
    width=400
)
oral_fluids_entry.pack(pady=10)

urine_entry = ctk.CTkEntry(
    app,
    placeholder_text="Mocz (ml)",
    font=(FONT, 20),
    width=400
)
urine_entry.pack(pady=10)

vomit_entry = ctk.CTkEntry(
    app,
    placeholder_text="Wymioty (ml)",
    font=(FONT, 20),
    width=400
)
vomit_entry.pack(pady=10)

calculate_button = ctk.CTkButton(
    app,
    text="Oblicz bilans płynów",
    font=(FONT, 24),
    width=400,
    command=calculate_fluid_balance
)
calculate_button.pack(pady=20)

result_label = ctk.CTkLabel(
    app,
    text="Podaj dane i oblicz\naby zobaczyć wynik",
    font=(FONT, 26),
    width=400
)
result_label.pack(pady=10)

app.mainloop()
