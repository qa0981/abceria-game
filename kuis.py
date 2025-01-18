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
            {"image": "image/huruf/tebak_huruf/letter-c.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-a.png", "correct": True},
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
        "correct_answer": "B",
        "choices": [
            {"image": "image/huruf/tebak_huruf/letter-j.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-h.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-o.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-l.png", "correct": True},
        ],
    },
    {
        "sound": "image/voice_ alfabet/20.mp3",
        "correct_answer": "B",
        "choices": [
            {"image": "image/huruf/tebak_huruf/letter-t.png", "correct": True},
            {"image": "image/huruf/tebak_huruf/letter-m.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-o.png", "correct": False},
            {"image": "image/huruf/tebak_huruf/letter-q.png", "correct": False},
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

        # Main layout
        self.layout = BoxLayout(orientation="vertical", spacing=20, padding=20)

        # Label for instructions
        self.instruction_label = Label(
            text="Listen to the sound and choose the correct answer!",
            font_size=24,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.instruction_label)

        # Button to play sound
        self.play_sound_button = Button(
            text="Play Sound",
            size_hint=(1, 0.2),
            on_press=self.play_sound
        )
        self.layout.add_widget(self.play_sound_button)

        self.choices_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, 0.6))
        self.choice_buttons = []
        for _ in range(4):
            btn = ImageButton(
                size_hint=(None, None),
                size=(100, 100),
                allow_stretch=True
            )
            btn.bind(on_press=self.check_answer)
            self.choice_buttons.append(btn)
            self.choices_layout.add_widget(btn)

        self.layout.add_widget(self.choices_layout)
        self.add_widget(self.layout)

        # Load the first question immediately
        self.load_next_question()

    def load_questions(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.load_next_question()

    def load_next_question(self):
        """
        Load the next question from the list.
        """
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.sound = SoundLoader.load(question["sound"])
            self.correct_answer = question["correct_answer"]

            # Shuffle choices
            choices = question["choices"]
            shuffle(choices)
            for i, btn in enumerate(self.choice_buttons):
                btn.source = choices[i]["image"]
                btn.correct = choices[i]["correct"]

            self.instruction_label.text = f"Question {self.current_question_index + 1} of {len(self.questions)}"
        else:
            # End of the quiz
            self.instruction_label.text = "Quiz Completed! 🎉"
            self.play_sound_button.disabled = True
            for btn in self.choice_buttons:
                btn.disabled = True

    def play_sound(self, instance):
        """
        Play the sound for the current question.
        """
        if self.sound:
            self.sound.play()

    def check_answer(self, instance):
        """
        Validate the chosen answer.
        """
        print(f"Checking answer: {'Correct' if instance.correct else 'Incorrect'}")
        if instance.correct:
            self.show_popup("Correct!", "You selected the right answer!")
        else:
            self.wrong_answer_animation(instance)
            self.instruction_label.text = "Try Again! 😢"

        # Move to the next question after a short delay
        self.current_question_index += 1
        self.load_next_question()

    def show_popup(self, title, message):
        """
        Display a pop-up when the answer is correct.
        """
        print(f"Displaying popup: {title}")
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.6, 0.4)
        )
        popup.open()

    def wrong_answer_animation(self, btn):
        """
        Trigger animation (wiggle) and sound for the wrong answer.
        """
        print("Starting wrong answer animation")
        animation = Animation(x=btn.x + 10, duration=0.1) + Animation(x=btn.x - 10, duration=0.1)
        animation.start(btn)

        # Play wrong answer sound
        wrong_sound = SoundLoader.load("music/wrong.mp3")  # You can set your own wrong sound here
        if wrong_sound:
            wrong_sound.play()