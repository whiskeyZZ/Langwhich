from turtle import color, width
import googletrans
from googletrans import Translator
import random
from tkinter import *
from random import shuffle
import save_stuff


def choose_lang():
    keys = []
    languages = []
    for i in range(5):
        rnd = random.randint(0, len(lang_keys)-1)
        keys.append(lang_keys[rnd])
        languages.append(lang_names[rnd])
    
    translate_word(keys, languages)

def translate_word(keys, languages):
    words_to_translate = get_words()
    for x in range(5):
        lang_entry = []
        used_key = keys[x]
        new_trans = translator.translate(words_to_translate[x], dest=used_key)
        lang_entry.append(new_trans.text)
        lang_entry.append(languages[x])
        lang_entry.append(words_to_translate[x])
        information_lang.append(lang_entry)
    start_level()

def get_words():
    with open("words.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    shuffle(lines)
    words_to_translate = []
    for i in range(5):
        words_to_translate.append(lines[i])
    return words_to_translate

def start_level():
    actual_lang = information_lang[save_stuff.Prop.get_counter(save_stuff.Prop)][1]
    actual_word = information_lang[save_stuff.Prop.get_counter(save_stuff.Prop)][0]
    actual_word_canvas.itemconfig(word, text=actual_word+ " ?")
    button_langs = []
    shuffle(lang_names)
    button_langs.append(lang_names[0])
    button_langs.append(lang_names[1])
    button_langs.append(actual_lang)
    shuffle(button_langs)
    save_stuff.Prop.set_one_lang(save_stuff.Prop , button_langs[0])
    save_stuff.Prop.set_two_lang(save_stuff.Prop, button_langs[1])
    save_stuff.Prop.set_three_lang(save_stuff.Prop, button_langs[2])
    save_stuff.Prop.add_to_counter(save_stuff.Prop)
    button_one.config(text=save_stuff.Prop.get_one_lang(save_stuff.Prop))
    button_two.config(text=save_stuff.Prop.get_two_lang(save_stuff.Prop))
    button_three.config(text=save_stuff.Prop.get_three_lang(save_stuff.Prop))
    print(save_stuff.Prop.get_counter(save_stuff.Prop))


translator = Translator()

lang_dict = (googletrans.LANGUAGES)
lang_keys = list(lang_dict.keys())
lang_names = list(lang_dict.values())
actual_lang = ""
actual_level = 0
information_lang = []

bg_color = "#081413"
text_color = "#226660"

root = Tk()
root.title("Langwhich")
root.configure(bg=bg_color)
canvas = Canvas(root, width=1000, height=800)

question_canvas = Canvas(root, bg=bg_color, width=800, height=100, highlightthickness=0)
question_canvas.create_text(400, 50, text="From which Language is", font=("Helvetica", 50), fill=text_color)
question_canvas.pack()

actual_word_canvas = Canvas(root, bg=bg_color, width=800, height=120, highlightthickness=0)
word = actual_word_canvas.create_text(400, 70, font=("Helvetica", 80, "bold"), fill="blue")
actual_word_canvas.pack()

button_one = Button(root, command=lambda : start_level(), background=bg_color, activebackground=bg_color, foreground=text_color, activeforeground=text_color, font=("Helvetica", 60), highlightthickness=0, bd=0)
button_one.pack()
button_two = Button(root, command=lambda : start_level(), background=bg_color, activebackground=bg_color, foreground=text_color, activeforeground=text_color, font=("Helvetica", 60), highlightthickness=0, bd=0)
button_two.pack()
button_three = Button(root, command=lambda : start_level(), background=bg_color, activebackground=bg_color, foreground=text_color, activeforeground=text_color, font=("Helvetica", 60), highlightthickness=0, bd=0)
button_three.pack()

choose_lang()
root.mainloop()
