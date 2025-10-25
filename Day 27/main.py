from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = miles_input.get()
    calcute = float(new_text)*1.60934
    zero_label.config(text=calcute)




window = Tk()

window.title("miles to kilometer converter")
window.config(padx=100,pady=100)
window.minsize(width=100, height=100)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)
print(miles_input.get())

miles_label = Label(text="miles")
miles_label.grid(column=2,row=0)

is_equal_to_label = Label(text="is equal to label")
is_equal_to_label.grid(column=0,row=1)

zero_label = Label(text="0")
zero_label.grid(column=1,row=1)

km_label = Label(text="km")
km_label.grid(column=2,row=1)






Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()
