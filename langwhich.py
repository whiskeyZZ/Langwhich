from turtle import color, width
import googletrans
from googletrans import Translator
import random
from tkinter import *
from random import shuffle
from save_stuff import Prop as prop
import time
import json


def choose_lang():
    keys = []
    languages = []
    for i in range(10):
        rnd = random.randint(0, len(lang_keys)-1)
        keys.append(lang_keys[rnd])
        languages.append(lang_names[rnd])
    
    translate_word(keys, languages)

def translate_word(keys, languages):
    words_to_translate = get_words()
    for x in range(10):
        lang_entry = []
        used_key = keys[x]
        new_trans = translator.translate(words_to_translate[x], dest=used_key)
        lang_entry.append(new_trans.text)
        lang_entry.append(languages[x])
        lang_entry.append(words_to_translate[x])
        prop.information_lang.append(lang_entry)
    start_level(0)

def get_words():
    with open("words.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    shuffle(lines)
    words_to_translate = []
    for i in range(10):
        words_to_translate.append(lines[i])
    return words_to_translate

def start_level(button_number):
    if prop.not_first_level and prop.correct_language == False:
        check_correct(button_number)

    elif prop.correct_language:
        check_guesses_word(button_number)
    
    if prop.jump == False and prop.level_counter < 10:
        prop.actual_lang = prop.information_lang[prop.level_counter][1]
        actual_word = prop.information_lang[prop.level_counter][0]
        actual_word_canvas.itemconfig(word, text=actual_word+ " ?")
        question_canvas.itemconfig(question, text="From which language is")
        button_langs = []
        shuffle(lang_names)
        button_langs.append(lang_names[0])
        button_langs.append(lang_names[1])
        button_langs.append(prop.actual_lang)
        shuffle(button_langs)
        prop.button_one_lang = button_langs[0]
        prop.button_two_lang = button_langs[1]
        prop.button_three_lang = button_langs[2]
        prop.level_counter += 1
        button_one.config(text=prop.button_one_lang)
        button_two.config(text=prop.button_two_lang)
        button_three.config(text=prop.button_three_lang)
        prop.not_first_level = True

    if prop.level_counter == 10:
        button_one.pack_forget()
        button_two.pack_forget()
        button_three.pack_forget()
        question_canvas.itemconfig(question, text="Your score")
        actual_word_canvas.itemconfig(word, text=str(prop.points))
        with open("highscore.json") as hs:
            highscore_dict = json.loads(hs.read())
            hs.close()
        highscr = highscore_dict["highscore"]
        actaul_hs = 0
        if highscr < prop.points:
            actaul_hs = prop.points
            highscore_dict["highscore"] = prop.points
            js = json.dumps(highscore_dict)
            f = open("highscore.json", "w")
            f.write(js)
        else:
            actaul_hs = highscr
        highscore_canvas = Canvas(root, bg=bg_color, width=800, height=100, highlightthickness=0)
        highscore_canvas.create_text(400, 50, text="Highscore", font=("Helvetica", 50), fill=text_color)
        actual_hs_canvas = Canvas(root, bg=bg_color, width=800, height=120, highlightthickness=0)
        actual_hs_canvas.create_text(400, 70, font=("Helvetica", 80, "bold"), fill="blue", text=str(actaul_hs))
        button_restart.config(text="Restart")
        button_restart.pack()

def guess_word():
    question_canvas.itemconfig(question, text="What means")
    words = []
    prop.actual_word = prop.information_lang[prop.level_counter-1][2]
    with open("words.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    shuffle(lines)
    words.append(prop.actual_word)
    words.append(lines[0])
    words.append(lines[1])
    shuffle(words)
    prop.button_one_word = words[0]
    prop.button_two_word = words[1]
    prop.button_three_word = words[2]
    button_one.config(text=prop.button_one_word)
    button_two.config(text=prop.button_two_word)
    button_three.config(text=prop.button_three_word)
    prop.jump = True

def check_guesses_word(button_number):
    if prop.button_one_word == prop.actual_word:
        button_one.config(foreground="#37d629", activeforeground="#37d629")
        if button_number == 1:
            prop.points += 1
    if prop.button_two_word == prop.actual_word:
        button_two.config(foreground="#37d629", activeforeground="#37d629")
        if button_number == 2:
            prop.points += 1
    if prop.button_three_word == prop.actual_word:
        button_three.config(foreground="#37d629", activeforeground="#37d629")
        if button_number == 3:
            prop.points += 1
    root.update()
    time.sleep(1)
    button_one.config(foreground="#226660", activeforeground="#226660")
    button_two.config(foreground="#226660", activeforeground="#226660")
    button_three.config(foreground="#226660", activeforeground="#226660")
    prop.jump = False
    prop.correct_language = False

def check_correct(button_number):
    prop.correct_language = False
    if prop.button_one_lang == prop.actual_lang:
        button_one.config(foreground="#37d629", activeforeground="#37d629")
        if button_number == 1:
            prop.points += 1
            prop.correct_language = True
    if prop.button_two_lang == prop.actual_lang:
        button_two.config(foreground="#37d629", activeforeground="#37d629")
        if button_number == 2:
            prop.points += 1
            prop.correct_language = True
    if prop.button_three_lang == prop.actual_lang:
        button_three.config(foreground="#37d629", activeforeground="#37d629")
        if button_number == 3:
            prop.points += 1
            prop.correct_language = True
    root.update()
    time.sleep(1)
    button_one.config(foreground="#226660", activeforeground="#226660")
    button_two.config(foreground="#226660", activeforeground="#226660")
    button_three.config(foreground="#226660", activeforeground="#226660")
    if prop.correct_language:
        guess_word()

def restart():
    button_restart.pack_forget()
    question_canvas.itemconfig(question, text="From which Language is")
    button_one.pack()
    button_two.pack()
    button_three.pack()
    prop.reset_prop(prop)
    choose_lang()


translator = Translator()

lang_dict = (googletrans.LANGUAGES)
lang_keys = list(lang_dict.keys())
lang_names = list(lang_dict.values())

bg_color = "#081413"
text_color = "#226660"


root = Tk()
root.title("Langwhich")
root.configure(bg=bg_color)
canvas = Canvas(root, width=1000, height=800)

question_canvas = Canvas(root, bg=bg_color, width=800, height=100, highlightthickness=0)
question = question_canvas.create_text(400, 50, text="From which Language is", font=("Helvetica", 50), fill=text_color)
question_canvas.pack()

actual_word_canvas = Canvas(root, bg=bg_color, width=800, height=120, highlightthickness=0)
word = actual_word_canvas.create_text(400, 70, font=("Helvetica", 80, "bold"), fill="blue")
actual_word_canvas.pack()

button_one = Button(root, command=lambda : start_level(1), background=bg_color, activebackground=bg_color, foreground=prop.text_color_one, activeforeground=prop.text_color_one, font=("Helvetica", 60), highlightthickness=0, bd=0)
button_one.pack()
button_two = Button(root, command=lambda : start_level(2), background=bg_color, activebackground=bg_color, foreground=prop.text_color_two, activeforeground=prop.text_color_two, font=("Helvetica", 60), highlightthickness=0, bd=0)
button_two.pack()
button_three = Button(root, command=lambda : start_level(3), background=bg_color, activebackground=bg_color, foreground=prop.text_color_three, activeforeground=prop.text_color_three, font=("Helvetica", 60), highlightthickness=0, bd=0)
button_three.pack()
button_restart = Button(root, command=lambda : restart(), background=bg_color, activebackground=bg_color, foreground=prop.text_color_three, activeforeground=prop.text_color_three, font=("Helvetica", 60), highlightthickness=0, bd=0)

choose_lang()
root.mainloop()