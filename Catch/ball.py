import tkinter
from random import choice, randint

ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
ball_number = []# список номеров шариков
ball_coordinate = [] # список координат шариков

def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    По клику мышкой нужно удалять тот объект, на который мышка указывает.
    А также засчитываеть его в очки пользователя.
    """
    global label, score
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)
    number=obj[0]
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        score+=1
        label['text']=score
        create_random_ball()


def move_all_balls(event):
    """ передвигает все шарики на чуть-чуть
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
 создаёт шарик в случайном месте игрового холста canvas,
 при этом шарик не выходит за границы холста!
    """
    global ball_coordinate, ball_number
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())
     #рисуем шарик и запоминаем его номер в num_oval
    num_oval = canvas.create_oval(x, y, x+R, y+R, width=0, fill=random_color())
    ball_coordinate.append([x,y])# запоминаем координаты нового шарика
    ball_number.append(num_oval)# запоминаем номер нового шарика

def random_color():
    """
 :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)

def init_ball_catch_game():
    """
 Создаём необходимое для игры количество шариков, по которым нужно будет кликать.
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas, score, label

    root = tkinter.Tk()
    label_text = tkinter.Label(root, text = 'Набранные очки')
    label_text.pack()
    score = 0
    label = tkinter.Label(root, text=score)#привязка к переменной
    label.pack()
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите поиграть ещё!")