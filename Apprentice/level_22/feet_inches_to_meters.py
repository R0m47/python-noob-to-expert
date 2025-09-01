from tkinter import *


def feet_to_meters():
    feet = feet_input.get()
    m = float(feet) * 0.3048
    return m


def inches_to_meters():
    inches = inches_input.get()
    m = float(inches) * 0.0254
    return m


def final_result():
    final_result = feet_to_meters() + inches_to_meters()
    meter_result_label.config(text=f"{round(final_result,2)}")


window = Tk()
window.title("Feet Inches to Meters Converter")
window.config(padx=20, pady=20)
feet_input = Entry(width=7)
feet_input.grid(column=1, row=0)
feet_label = Label(text="Feets")
feet_label.grid(column=2, row=0)
inches_input = Entry(width=7)
inches_input.grid(column=1, row=1)
inches_label = Label(text="Inches")
inches_label.grid(column=2, row=1)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=2)
meter_result_label = Label(text=0)
meter_result_label.grid(column=1, row=2)
meter_label = Label(text="m")
meter_label.grid(column=2, row=2)
calculate_button = Button(text="Calculate", command=final_result)
calculate_button.grid(column=1, row=3)
window.mainloop()
