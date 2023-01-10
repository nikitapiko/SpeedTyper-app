from tkinter import *
import random
from random_texts import random_texts

ONE_MIN = 10
THREE_MIN = 180
FIVE_MIN = 300


def wpm(text, time):
    print(time)
    total_typed_keys = len(text)
    print(total_typed_keys)
    # gross WPM
    gross_wpm = round((total_typed_keys/5)/(time/60), 1)
    print(total_typed_keys/5)
    print(gross_wpm)
    wpm_label.config(text=f"Your SpeedTyper Speed: {gross_wpm} words per minute")

    # check for mistakes
def accuracy(correct_text1, typed_text1):
    error_count = 0
    correct_list = correct_text1.split(" ")
    typed_list = typed_text1.split(" ")
    error_words = []
    print(correct_list)
    print(typed_list)

    for word in typed_list:
        if word not in correct_list:
            error_count += 1
            error_words.append(word)

    typed_text_length = len(typed_text1)
    net_correct_chars = typed_text_length - (error_count * 5)
    accuracy_ratio = round(net_correct_chars/typed_text_length, 2) * 100

    accuracy_label.config(text=f"Accuracy: {accuracy_ratio}% \nErrors: {error_count}\n")
    print(f"{accuracy_ratio}%")
    print(error_count)
    print(error_words)
    # print(correct_text)
    # print(typed_text)


def error_detection(correct_text2, typed_text2):
    error_count = 0
    print(correct_text2)
    print(typed_text2)
    for char in range(len(typed_text2) - 1):
        if typed_text2[char] == correct_text2[char]:
            print('correct')
        else:
            print('false')
            typed_text2.
            print("removed")


def start_timer(event):
    global timer_started
    if not timer_started:
        timer_started = True
        timer_label.config(text=ONE_MIN)
        timer()

def timer():
    global current_text_to_analyze
    current_time = int(timer_label.cget("text"))
    print(current_time)
    current_time -= 1
    timer_label.config(text=str(current_time))

    if current_time > 0:
        window.after(1000, timer)
    else:
        typed_text = entry.get()
        wpm(typed_text, ONE_MIN)
        correct_text = text_field.get("1.0", END)
        accuracy(correct_text1=correct_text, typed_text1=typed_text)
        error_detection(correct_text2=correct_text, typed_text2=typed_text)




window = Tk()
window.title("SpeedTyper")
window.config(pady=50, padx=50)
window.wm_attributes("-topmost", 1)

# logo = PhotoImage(file="SpeedTyperLogo.png")
# canvas = Canvas(height=300, width=300)
# canvas.create_image(100, 100, image=logo)
# canvas.grid(column=1, row=0)

text_field = Text(width=50, height=7, font=("Arial", 18))
text_field.insert(index=END, chars=random.choice(random_texts))

# text_field.insert(te"Random Text to type")

# text entry field
entry = Entry(window, width=38, font=("Arial", 21))
entry.grid(column=1, row=5)

# timer
timer_label = Label(window)
timer_started = False
wpm_label = Label()
wpm_label.grid(column=1, row=3)

accuracy_label = Label()
accuracy_label.grid(column=1, row=4)


text_field.grid(column=1, row=1)
timer_label.grid(column=1, row=2)


entry.bind("<Key>", start_timer)



current_text_to_analyze = ""



window.mainloop()