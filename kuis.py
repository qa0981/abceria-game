from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.animation import Animation
from random import shuffle

class ImageButton(ButtonBehavior, Image):
    correct = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

questions = [
    {
        "sound": "image/voice_ alfabet/3.mp3",
        "correct_answer": "A",
        "choices": [
            {"image": "image/huruf/tebak_huruf/letter-c.png", "correct": True},
            {"image": "image/huruf/tebak_huruf/letter-a.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-k.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-m.png", "correct": False},
        ],
    },
    {
        "sound": "image/voice_ alfabet/7.mp3",
        "correct_answer": "B",
        "choices": [
            {"image": "image/huruf/tebak_huruf/letter-t.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-g.png", "correct": True},
            {"image": "image/huruf/tebak_huruf/letter-f.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/y.png", "correct": False},
        ],
    },
    {
        "sound": "image/voice_ alfabet/12.mp3",
        "correct_answer": "C",
        "choices": [
            {"image": "image/huruf/tebak_huruf/letter-j.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-h.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-o.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-l.png", "correct": True},
        ],
    },
    {
        "sound": "image/voice_ alfabet/20.mp3",
        "correct_answer": "D",
        "choices": [
            {"image": "image/huruf/tebak_huruf/letter-t.png", "correct": True},
            {"image": "image/huruf/tebak_huruf/letter-m.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-o.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-q.png", "correct": False},
        ],
    },
    {
        "sound": "image/voice_ alfabet/5.mp3",
        "correct_answer": "E",
        "choices": [
            {"image": "image/huruf/tebak_huruf/letter-f.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-e.png", "correct": True},
            {"image": "image/huruf/tebak_huruf/letter-h.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-u.png", "correct": False},
        ],
    },
]

class TebakHurufScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.questions = questions[:]
        self.current_question_index = 0
        self.correct_answer = None
        self.sound = None

        self.layout = BoxLayout(orientation="vertical", spacing=20, padding=20, size_hint=(1, 1))
        self.layout.add_widget(Label(text="Listen to the sound and choose the correct answer!", font_size=24, size_hint=(1, 0.2)))

        self.play_sound_button = ImageButton(
            source="image/voice4.png",
            size_hint=(0.6, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            on_press=self.play_sound
        )
        self.layout.add_widget(self.play_sound_button)

        self.choices_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint=(0.7, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.choice_buttons = []
        for _ in range(4):
            btn = ImageButton(size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5}, allow_stretch=True)
            btn.bind(on_press=self.check_answer)
            self.choice_buttons.append(btn)
            self.choices_layout.add_widget(btn)

        self.layout.add_widget(self.choices_layout)
        self.add_widget(self.layout)

        self.load_next_question()

    def load_next_question(self):

        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.sound = SoundLoader.load(question["sound"])
            self.correct_answer = question["correct_answer"]

            choices = question["choices"]
            shuffle(choices)
            for i, btn in enumerate(self.choice_buttons):
                btn.source = choices[i]["image"]
                btn.correct = choices[i]["correct"]

            self.layout.children[0].text = f"Question {self.current_question_index + 1} of {len(self.questions)}"
        else:
            self.layout.children[0].text = "Quiz Completed! 🎉"
            self.play_sound_button.disabled = True
            for btn in self.choice_buttons:
                btn.disabled = True

    def play_sound(self, instance):
        if self.sound:
            self.sound.play()

    def check_answer(self, instance):

        if instance.correct:
            self.show_popup("Correct!", "You selected the right answer!")
            self.play_correct_sound()
        else:
            self.wrong_answer_animation(instance)
            self.layout.children[0].text = "Try Again! 😢"

    def show_popup(self, title, message):

        popup = Popup(
            title=title,
            content=Label(text=message, halign="center", valign="middle"),
            size_hint=(0.6, 0.4)
        )
        popup.bind(on_dismiss=self.next_question)
        popup.open()

    def next_question(self, instance):
 
        self.current_question_index += 1
        self.load_next_question()

    def play_correct_sound(self):

        correct_sound = SoundLoader.load("music/correct.mp3")
        if correct_sound:
            correct_sound.play()

    def wrong_answer_animation(self, btn):
        animation = (
            Animation(x=btn.x + 15, duration=0.1) +
            Animation(x=btn.x - 15, duration=0.1) +
            Animation(x=btn.x, duration=0.1)
        )
        animation.start(btn)

        wrong_sound = SoundLoader.load("music/wrong.mp3")
        if wrong_sound:
            wrong_sound.play()

    def go_back(self, instance=None):
        self.manager.current = "game"
        self.play_sound("music/pop-button.mp3")
