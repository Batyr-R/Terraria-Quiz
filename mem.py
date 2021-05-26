from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel,QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
question_list = []
question_list.append(Question('В каком году создали игру Террария?','2011','2010','2009','2012'))
question_list.append(Question('Сколько жизней у Герцега Рыброна?','50000','40000','30000','60000'))
question_list.append(Question('Сколько урона у Стражника Данжа?','9999','2000','3000','6000'))
question_list.append(Question('Кто самый последний босс?','Лунный Лорд','Герцег Рыброн','Императрица Света','Культист-Лунатик'))
question_list.append(Question('Что тебе дают при первом заходе в мир террарии?','медную кирку , топор , меч','медный молот , топор , кирку','медную лопату , топор , кирку','другое'))
question_list.append(Question('Багрянец и искажение бывают в одном мире?','в секретном сиде','не бывают','бывает','другое'))
question_list.append(Question('После какого босса тебе дают (скрыто) молот ☭','стены плоти','лунотрона','пожирателя миров','глаза ктулху'))
question_list.append(Question('Как поселить гоблина-торговца в дом?','найти его в пещере и потом сделать ему дом сверху','просто сделать ему дом и он сам поселиться','сделать дом из гоблиновых блоков','удалить игру'))
question_list.append(Question('Сколько Жизней у Луного Лорда?','120000','100000','110000','130000'))
question_list.append(Question('Сколько всего есть башен?','4','3','5','6'))
question_list.append(Question('Самые сильные крылья?','Крылья Герцега Рыброна','Спектральные кралья','Демонические крылья','Ангельские крылья'))
question_list.append(Question('Сколько Боссов в Террарие?','30','12','36','24'))
question_list.append(Question('Какой фрагмент у призывателя?','Звездной пыли','Солнца','Вихря','Туманности'))
question_list.append(Question('Сколько есть руд каторых можно получить при разрушении алтарей','3','6','5','4'))


app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Test')

# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году создали игру Террария')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('2009')
rbtn_2 = QRadioButton('2010')
rbtn_3 = QRadioButton('2011')
rbtn_4 = QRadioButton('2012')

RadioGroup = QButtonGroup()# объеденяем для снятия флажка с переключателей.
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_result():
    RadioGroupBox.hide()
    
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_questions():
    
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answer=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_questions()
def show__correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        show__correct("Правильно!")
        window.score+=1
        print('Статиска\n-Всего вопросов:',window.total,'\n-Правильных ответов:',window.score)
        print("Рейтинг:",(window.score/window.total*100),"%")
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show__correct("Неверно!")
            print("Рейтинг:",(window.score/window.total*100),"%")
def next_qustion():
    window.total +=1
    print('Статиска\n-Всего вопросов:',window.total,'\n-Правильных ответов:',window.score)
    cur_question=randint(0,len(question_list)-1)
    q=question_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text()=='Ответить':
        check_answer()
    else:
        next_qustion()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score=0
window.total=0
window.resize(400, 300)

btn_OK.clicked.connect(click_OK)

next_qustion()
window.show()
app.exec()