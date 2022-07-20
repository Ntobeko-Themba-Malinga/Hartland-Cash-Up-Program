import tkinter as tk
from tkinter import messagebox
from win32printing import Printer
from datetime import date


def print_function():
    day = date_entry.get()

    try:
        food = float(food_entry.get())
        bar = float(total_entry.get()) - food
        total = food + bar

        speed_point = float(speed_point_entry.get())

        patty_cash = float(patty_cash_entry.get())
        cash = float(cash_entry.get()) - patty_cash  
        
        card = float(card_entry.get())
        card_tips = float(card_tips_entry.get())
        card_car_wash = float(car_wash_entry.get())
        total_card = card + card_tips + card_car_wash

        other = float(other_entry.get())
        
        total_sales = patty_cash + cash + card + other
    except Exception as e:
        food = float(0)
        bar = float(0) - food
        total = food + bar

        speed_point = float(0)

        patty_cash = float(0)
        cash = float(0) - patty_cash  
        
        card = float(0)
        card_tips = float(0)
        card_car_wash = float(0)
        total_card = card + card_tips + card_car_wash

        other = float(0)
        
        total_sales = patty_cash + cash + card + other

    if int(other) == 0:
        if card_tips > 0 and int(card_car_wash) == 0:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\n     +R{card_tips:0,.2f}tips\nTotal sales: R{total_sales:0,.2f}"
        elif int(card_tips) == 0 and card_car_wash > 0:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\n     +R{card_car_wash:0,.2f}carwash\nTotal sales: R{total_sales:0,.2f}"
        elif card_tips > 0 and card_car_wash > 0:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\n     +R{card_tips:0,.2f}tips\n     +R{card_car_wash:0,.2f}carwash\nTotal sales: R{total_sales:0,.2f}"
        else:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\nTotal sales: R{total_sales:0,.2f}"
    else:
        if card_tips > 0 and int(card_car_wash) == 0:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\n     +R{card_tips:0,.2f}tips\nOther: R{other:0,.2f}\nTotal sales: R{total_sales:0,.2f}"
        elif int(card_tips) == 0 and card_car_wash > 0:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\n     +R{card_car_wash:0,.2f}carwash\nOther: R{other:0,.2f}\nTotal sales: R{total_sales:0,.2f}"
        elif card_tips > 0 and card_car_wash > 0:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\n     +R{card_tips:0,.2f}tips\n     +R{card_car_wash:0,.2f}carwash\nOther: R{other:0,.2f}\nTotal sales: R{total_sales:0,.2f}"
        else:
            cash_up = f"\t{day}\n\nFood: R{food:0,.2f}\nBar: R{bar:0,.2f}\nTotal: R{total:0,.2f}\n\n" \
                    +f"Petty cash: R{patty_cash:0,.2f}\nCash: R{cash:0,.2f}\nCard: R{card:0,.2f}\nOther: R{other:0,.2f}\nTotal sales: R{total_sales:0,.2f}"

    printer_name = printer_name_entry.get()
    font_size = int(font_size_entry.get())

    font = {
        "height": font_size
    }

    if total_card == speed_point:
        if total_sales == total:
            with Printer(linegap=1) as printer:
                printer.printer_name = printer_name
                printer.text(cash_up, font_config=font)
        else:
            messagebox.showerror(
                title="Cash Up Error",
                message="Machine total and total sales don't match."
            )
    else:
        messagebox.showerror(
            title="Cash Up Error",
            message="Machine card and speed point don't match."
        )


FONT = font=('Calibri', 18)
PAD_Y = 4
PAD_X = 10

window = tk.Tk()
window.title("HARTLAND OASE")

frame1 = tk.Frame(window, pady=10)
frame1.pack()

# Date
date_label = tk.Label(
    master=frame1,
    text="DATE:",
    font=FONT
)
date_label.grid(row=0, column=0)
date_entry = tk.Entry(
    master=frame1,
    font=FONT,
)
date_entry.grid(row=0, column=1, pady=PAD_Y, padx=PAD_X)
date_entry.insert(0, date.today().strftime("%d/%m/%Y"))

# Total
total_label = tk.Label(
    master=frame1,
    text="TOTAL:",
    font=FONT
)
total_label.grid(row=1, column=0)
total_entry = tk.Entry(
    master=frame1,
    font=FONT
)
total_entry.grid(row=1, column=1, pady=PAD_Y, padx=PAD_X)
total_entry.insert(0, '0')

# Food
food_label = tk.Label(
    master=frame1,
    text="FOOD:",
    font=FONT
)
food_label.grid(row=2, column=0)
food_entry = tk.Entry(
    master=frame1,
    font=FONT
)
food_entry.grid(row=2, column=1, pady=PAD_Y, padx=PAD_X)
food_entry.insert(0, '0')

# Patty cash
patty_cash_label = tk.Label(
    master=frame1,
    text="PATTY CASH:",
    font=FONT
)
patty_cash_label.grid(row=3, column=0)
patty_cash_entry = tk.Entry(
    master=frame1,
    font=FONT
)
patty_cash_entry.grid(row=3, column=1, pady=PAD_Y, padx=PAD_X)
patty_cash_entry.insert(0, '0')

# Cash
cash_label = tk.Label(
    master=frame1,
    text="CASH:",
    font=FONT
)
cash_label.grid(row=4, column=0)
cash_entry = tk.Entry(
    master=frame1,
    font=FONT
)
cash_entry.grid(row=4, column=1, pady=PAD_Y, padx=PAD_X)
cash_entry.insert(0, '0')

# Speed point
speed_point_label = tk.Label(
    master=frame1,
    text="SPEED POINT:",
    font=FONT
)
speed_point_label.grid(row=5, column=0)
speed_point_entry = tk.Entry(
    master=frame1,
    font=FONT
)
speed_point_entry.grid(row=5, column=1, pady=PAD_Y, padx=PAD_X)
speed_point_entry.insert(0, '0')

# Card
card_label = tk.Label(
    master=frame1,
    text="CARD:",
    font=FONT
)
card_label.grid(row=6, column=0)
card_entry = tk.Entry(
    master=frame1,
    font=FONT
)
card_entry.grid(row=6, column=1, pady=PAD_Y, padx=PAD_X)
card_entry.insert(0, '0')

# Card tips
card_tips_label = tk.Label(
    master=frame1,
    text="CARD TIPS:",
    font=FONT
)
card_tips_label.grid(row=7, column=0)
card_tips_entry = tk.Entry(
    master=frame1,
    font=FONT
)
card_tips_entry.grid(row=7, column=1, pady=PAD_Y, padx=PAD_X)
card_tips_entry.insert(0, '0')

# Car wash
car_wash_label = tk.Label(
    master=frame1,
    text="CAR WASH:",
    font=FONT
)
car_wash_label.grid(row=8, column=0)
car_wash_entry = tk.Entry(
    master=frame1,
    font=FONT
)
car_wash_entry.grid(row=8, column=1, pady=PAD_Y, padx=PAD_X)
car_wash_entry.insert(0, '0')

# Other
other_label = tk.Label(
    master=frame1,
    text="OTHER:",
    font=FONT
)
other_label.grid(row=9, column=0)
other_entry = tk.Entry(
    master=frame1,
    font=FONT
)
other_entry.grid(row=9, column=1, pady=PAD_Y, padx=PAD_X)
other_entry.insert(0, '0')

# printer
printer_name_label = tk.Label(
    master=frame1,
    text="PRINTER NAME:"
)
printer_name_label.grid(row=10, column=0)
printer_name_entry = tk.Entry(
    master=frame1,
    font=("Calibri", 12)
)
printer_name_entry.grid(row=10, column=1, pady=PAD_Y, padx=PAD_X)
printer_name_entry.insert(0, 'RONGTA 80mm Series Printer')

# Font size
font_size_label = tk.Label(
    master=frame1,
    text='FONT SIZE'
)
font_size_label.grid(row=11, column=0)
font_size_entry = tk.Entry(
    master=frame1,
    font=("Calibri", 12)
)
font_size_entry.grid(row=11, column=1)
font_size_entry.insert(0, '18')


# print button
print_button = tk.Button(
    master=frame1,
    text='PRINT',
    font=FONT,
    command=print_function
)
print_button.grid(row=12, column=0, columnspan=2, pady=10)



window.mainloop()
