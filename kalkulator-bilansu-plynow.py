import customtkinter as ctk
import json
import os
import sys

FONT = "Arial"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ===== i18n =====
def resource_path(path):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, path)

def load_lang(code):
    with open(resource_path(f"{code}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

LANG_MAP = {
    "Polski": "pl-PL",
    "English": "en-US",
    "Українська": "uk-UA"
}

current_lang = "pl-PL"
T = load_lang(current_lang)

# ===== App =====
app = ctk.CTk()
app.geometry("475x525")
app.resizable(False, False)

# ===== Logic =====
def calculate_fluid_balance():
    if fluid_balance_menu.get() == T["choose_balance"]:
        result_label.configure(text=T["error_choose"])
        return

    if not all(entry.get().isdigit() for entry in [
        flow_rate_entry, iv_fluids_entry, oral_fluids_entry, urine_entry, vomit_entry
    ]):
        result_label.configure(text=T["error_number"])
        return

    hours_dictionary = {"6h": 6, "12h": 12, "24h": 24}

    result = int(flow_rate_entry.get()) * hours_dictionary[fluid_balance_menu.get()]
    result += int(iv_fluids_entry.get()) + int(oral_fluids_entry.get())
    result -= int(urine_entry.get()) + int(vomit_entry.get())

    if result < 0:
        result = 0

    result_label.configure(text=T["result"].format(value=result))

def apply_language():
    global T
    T = load_lang(current_lang)

    app.title(T["title"])
    fluid_balance_menu.configure(values=[T["choose_balance"], "6h", "12h", "24h"])
    fluid_balance_menu.set(T["choose_balance"])

    flow_rate_entry.configure(placeholder_text=T["flow_rate"])
    iv_fluids_entry.configure(placeholder_text=T["iv_fluids"])
    oral_fluids_entry.configure(placeholder_text=T["oral_fluids"])
    urine_entry.configure(placeholder_text=T["urine"])
    vomit_entry.configure(placeholder_text=T["vomit"])

    calculate_button.configure(text=T["calculate"])
    result_label.configure(text=T["result_default"])

def change_language(choice):
    global current_lang
    current_lang = LANG_MAP[choice]
    apply_language()

# ===== GUI =====
fluid_balance_menu = ctk.CTkOptionMenu(
    app,
    values=[],
    font=(FONT, 20),
    width=400
)
fluid_balance_menu.pack(pady=20)

flow_rate_entry = ctk.CTkEntry(app, font=(FONT, 20), width=400)
flow_rate_entry.pack(pady=10)

iv_fluids_entry = ctk.CTkEntry(app, font=(FONT, 20), width=400)
iv_fluids_entry.pack(pady=10)

oral_fluids_entry = ctk.CTkEntry(app, font=(FONT, 20), width=400)
oral_fluids_entry.pack(pady=10)

urine_entry = ctk.CTkEntry(app, font=(FONT, 20), width=400)
urine_entry.pack(pady=10)

vomit_entry = ctk.CTkEntry(app, font=(FONT, 20), width=400)
vomit_entry.pack(pady=10)

calculate_button = ctk.CTkButton(
    app,
    font=(FONT, 24),
    width=400,
    command=calculate_fluid_balance
)
calculate_button.pack(pady=20)

result_label = ctk.CTkLabel(
    app,
    font=(FONT, 26),
    width=400
)
result_label.pack(pady=10)

language_menu = ctk.CTkOptionMenu(
    app,
    values=list(LANG_MAP.keys()),
    font=(FONT, 18),
    width=150,
    command=change_language
)
language_menu.pack(padx=10, pady=10, side="bottom", anchor="w")
language_menu.set("Polski")

apply_language()
app.mainloop()
