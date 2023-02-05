from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
help_window_flag=False
about_window_flag=False
root=tk.Tk()
root.title("Блокнот")
root.geometry("700x700+800+50")
root.minsize(200,100)
root.maxsize(1920,1080)
main_menu = Menu(root)
view_colors = {
    "dark": {"text_bg": "black", "text_fg": "yellow", "cursor": "white", "select_bg": "#8D917A"},
    "light": {"text_bg": "white", "text_fg": "black", "cursor": "#A5A5A5", "select_bg": "#FAEEDD"},
    "night": {"text_bg": "grey", "text_fg": "purple","cursor": "white","select_bg": "#000e57"},
    "happy": {"text_bg": "lime", "text_fg": "red","cursor": "red","select_bg": "#02027F"},
    "uno": {"text_bg": "yellow", "text_fg": "red","cursor": "blue","select_bg": "#00ff33"}}
fonts = {
    "Arial":
        {"font":"Arial 14 bold"},
    "CSMS":{"font": ("Comic Sans MS", 15, "bold")},
    "TNR": {"font": ("Times New Roman", 15, "bold")},
    "SCP": {"font": ("Source Code Pro", 15, "bold")},
    "MSSS": {"font": ("MS Sans Serif", 15, "bold")},
    "C": {"font": ("Consolas", 15, "bold")}}
def chenge_theme(theme):
    f_text["bg"] = view_colors[theme]["text_bg"]
    f_text["fg"] = view_colors[theme]["text_fg"]
    f_text["insertbackground"] = view_colors[theme]["cursor"]
    f_text["selectbackground"] = view_colors[theme]["select_bg"]


def chenge_fonts(fontss):
    f_text["font"] = fonts[fontss]["font"]


def exit_func():
    root.destroy()
def file_new():
    text_save=str(text.get(1.0,tk.END))
    if text_save!="\n":
        root_asksave=tk.Tk()
        root_asksave.geometry("300x100+500+300")
        root_asksave.resizable(False,False)
        root_asksave.title("Помощь")
        global help_window_flag
        if help_window_flag==False:
            def new_text():
                text.delete('1.0',tk.END)
                root_asksave.destroy()
            def close_asksave():
                root_asksave.destroy()
        def new_save():
            root_asksave.destroy()
            file_save()
            text.delete('1.0',tk.END)
        save_label=tk.Label(root_asksave,text="СОХРАНИТЬ ФАЙЛ")
        save_label.pack()
        yes_button=tk.Button(root_asksave,text="Да",command=file_save)
        yes_button.pack()
        no_button=tk.Button(root_asksave,text="Нет",command=new_text)
        no_button.pack()
        back_button=tk.Button(root_asksave,text="Отмена",command=close_asksave)
        back_button.pack()
def help_window():
    global help_window_flag
    if help_window_flag==False:
        root_help=tk.Tk()
        root_help.geometry("350x70+500+300")
        root_help.resizable(False,False)
        root_help.title("Помощь")
        help_Label=tk.Label(root_help,text="Ссылка для инструкции\nhttps://journal.top-academy.ru/ru/main/dashboard/page/index")
        help_Label.pack()
        help_window_flag=True
        def close_root_help():
            root_help.destroy()
            global help_window_flag
            help_window_flag=False
        help.button=tk.Button(root_help,text="Закрыть",command=close_root_help)
        help.button.pack()
def file_save():
    file_name=tk.filedialog.asksaveasfilename(initialdir="/",title="Сохранить как",filetype=(("Текстовые документы","*.txt"),("Все файлы","*.*")))
    if file_name:
        with open(file_name+".txt","w") as f:
            text_save=str(text.get(1.0,tk.END))
            f.write(text_save)
            
def about_help():
    global about_window_flag
    if about_window_flag==False:
        root_about=tk.Tk()
        root_about.geometry("300x70+500+300")
        root_about.resizable(False,False)
        root_about.title("Создатели")
        about_Label=tk.Label(root_about,text="Создатели Райан Гослинг и Михаил Калюжный\nв Академии ТОП")
        about_Label.pack()
        about_window_flag=True
        def about_root_help():
            root_about.destroy()
            global about_window_flag
            about_window_flag=False
        help.button=tk.Button(root_about,text="Закрыть",command=about_root_help)
        help.button.pack()

def file_open():
    file_name=tk.filedialog.askopenfilename(initialdir="/",title="Открыть файл",filetype=(("Текстовые документы","*.txt"),("Все файлы","*.*")))
    if file_name:
        with open(file_name,"r") as f:
            text_open=f.read()
            text.insert(1.0,text_open)
            
def the_creator():
    global about_window_flag
    if about_window_flag==False:
        root_about=tk.Tk()
        root_about.geometry("500x120+500+300")
        root_about.resizable(False,False)
        root_about.title("The words of the creator")
        about_Label=tk.Label(root_about,text="Для начала мы создали окно на котором можно писать текст,\nсоздали меню с новыйм листом,\nоткрытие сохранённого текста,\ncохроняем текст,\nи выход из блокнота ")
        about_Label.pack()
        about_window_flag=True
        def about_root_help():
            root_about.destroy()
            global about_window_flag
            about_window_flag=False
        help.button=tk.Button(root_about,text="Закрыть" ,command=about_root_help)
        help.button.pack()


main_menu=tk.Menu(root)
root.config(menu=main_menu)
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="Новый лист",command=file_new)
file_menu.add_command(label="Открыть текст",command=file_open)
file_menu.add_command(label="Сохранить текст",command=file_save)
file_menu.add_command(label="Выйти",command=exit_func)
main_menu.add_cascade(label="Файл",menu=file_menu)

help_menu=tk.Menu(main_menu,tearoff=0)
help_menu.add_command(label="Помощь",command=help_window)
help_menu.add_command(label="Автор",command=about_help)
main_menu.add_cascade(label="Помощь",menu=help_menu)

themes_menu=tk.Menu(main_menu,tearoff=0)
themes_menu.add_command(label="Слова автора",command=the_creator)
main_menu.add_cascade(label="Процесс производства",menu=themes_menu)

view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label="Тёмная", command=lambda: chenge_theme("dark"))
view_menu_sub.add_command(label="Светлая", command=lambda: chenge_theme("light"))
view_menu_sub.add_command(label="Ночная", command=lambda: chenge_theme("night"))
view_menu_sub.add_command(label="Весёлая", command=lambda: chenge_theme("happy"))
view_menu_sub.add_command(label="UNO", command=lambda: chenge_theme("uno"))
view_menu.add_cascade(label="Тема", menu=view_menu_sub)

font_menu_sub.add_command(label="Arial", command=lambda: chenge_fonts("Arial"))
font_menu_sub.add_command(label="Comic Sans MS", command=lambda: chenge_fonts("CSMS"))
font_menu_sub.add_command(label="Times New Roman", command=lambda: chenge_fonts("TNR"))
font_menu_sub.add_command(label="Source Code Pro", command=lambda: chenge_fonts("SCP"))
font_menu_sub.add_command(label="Consolas", command=lambda: chenge_fonts("C"))
font_menu_sub.add_command(label="MS Sans Serif", command=lambda: chenge_fonts("MSSS"))
view_menu.add_cascade(label="Шрифт...", menu=font_menu_sub)
root.config(menu=view_menu)

main_menu.add_cascade(label="Вид", menu=view_menu)
root.config(menu=main_menu)



f_text=tk.Text(root)
f_text.pack(expand=tk.YES,fill=tk.BOTH)
root.mainloop()