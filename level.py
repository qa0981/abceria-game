class LevelSelectionScreen(Screen):
    coin_count = StringProperty("100")
    username = StringProperty("Username")

    def on_enter(self):
        self.start_animations()

    def start_animations(self):
        obj1 = self.ids.animated1
        anim1 = Animation(pos_hint={"x": 0.9, "y": 0.3}, duration=2) + Animation(pos_hint={"x": 0.8, "y": 0.6}, duration=2)
        anim1.repeat = True
        anim1.start(obj1)

        obj2 = self.ids.animated2
        anim2 = Animation(size=(220, 220), duration=1.5) + Animation(size=(180, 180), duration=1.5)
        anim2.repeat = True
        anim2.start(obj2)

        obj3 = self.ids.animated3
        anim3 = Animation(pos_hint={"x": 0.1, "y": 0.5}, duration=3) + Animation(pos_hint={"x": 0.2, "y": 0.7}, duration=3)
        anim3.repeat = True
        anim3.start(obj3)

        obj4 = self.ids.animated4
        anim4 = Animation(opacity=0.2, duration=1) + Animation(opacity=1, duration=1)
        anim4.repeat = True
        anim4.start(obj4)

    def wobble_arrow(self, widget):
        wobble = (
            Animation(pos_hint={"x": 0.015, "y": 0.02}, duration=0.1) +
            Animation(pos_hint={"x": 0.025, "y": 0.02}, duration=0.1) +
            Animation(pos_hint={"x": 0.02, "y": 0.02}, duration=0.1)
        )
        wobble.repeat = False
        wobble.start(widget)

    def go_to_menu(self):
        print("Returning to start menu")
        self.manager.current = "game"

    def select_level(self, level):
        print(f"Level {level} selected!")


<Image>:
    allow_stretch: True

<LevelSelectionScreen>:
    coin_count: "100"
    username: "Player"

    FloatLayout:
        canvas.before:
            Rectangle:
                source: "image/bg_next.png"
                size: self.size
                pos: self.pos

        Image:
            source: "image/title/1.png"
            size_hint: None, None
            size: 800, 200
            pos_hint: {"center_x": 0.5, "top": 0.85}

        Image:
            id: animated1
            source: "image/huruf/p.png"
            size_hint: None, None
            size: 180, 180
            pos_hint: {"x": 0.2, "y": 0.9}  # Initial position

        Image:
            id: animated2
            source: "image/huruf/d.png"
            size_hint: None, None
            size: 300, 300
            pos_hint: {"x": 0.1, "y": 0.1}

        Image:
            id: animated3
            source: "image/huruf/open-book.png"
            size_hint: None, None
            size: 180, 180
            pos_hint: {"x": 0.1, "y": 0.4}

        Image:
            id: animated4
            source: "image/huruf/book.png"
            size_hint: None, None
            size: 150, 150
            pos_hint: {"x": 0.9, "y": 0.1}
            opacity: 1

        FloatLayout:
            size_hint: None, None
            size: 150, 50
            pos_hint: {"x": 0.02, "top": 0.98}
            canvas.before:
                Color:
                    rgba: (217 / 255, 162 / 255, 67 / 255, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [25]

            Image:
                source: "buttons/koin.png"
                size_hint: None, None
                size: 40, 40
                pos_hint: {"x": 0.05, "center_y": 0.5}
                allow_stretch: True

            Label:
                text: root.coin_count
                font_size: 54
                font_name: "fonts/SplashBakery.otf"
                color: (255 / 255, 222 / 255, 169 / 255, 1)
                size_hint: None, None
                size: 110, 50
                pos_hint: {"x": 0.5, "center_y": 0.5}
                halign: "left"
                valign: "middle"
                text_size: self.size

        FloatLayout:
            size_hint: None, None
            size: 300, 50
            pos_hint: {"right": 0.98, "top": 0.98}
            canvas.before:
                Color:
                    rgba: (217 / 255, 162 / 255, 67 / 255, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [25]

            Image:
                source: "buttons/tameng.png"
                size_hint: None, None
                size: 40, 40
                pos_hint: {"x": 0.05, "center_y": 0.5}
                allow_stretch: True

            Label:
                text: root.username
                font_size: 54
                font_name: "fonts/SplashBakery.otf"
                color: (255 / 255, 222 / 255, 169 / 255, 1)
                size_hint: None, None
                size: 200, 50
                pos_hint: {"x": 0.3, "center_y": 0.5}
                halign: "left"
                valign: "middle"
                text_size: self.size

        MagicImage:
            source: "buttons/arrow_left.png"
            size_hint: None, None
            size: 100, 100
            pos_hint: {"x": 0.02, "y": 0.02}
            on_release: self.wobble_and_navigate(root.go_to_menu)

        FloatLayout:
            size_hint: None, None
            size: 900, 450
            pos_hint: {"center_x": 0.46, "center_y": 0.35}

            GridLayout:
                cols: 3
                spacing: 30
                size_hint: None, None
                size: 900, 180
                pos_hint: {"center_x": 0.5, "top": 1}

                ClickableImage:
                    source: "buttons/button_level/1.png"
                    size_hint: None, None
                    size: 320, 200
                    on_release: root.select_level(1)

                ClickableImage:
                    source: "buttons/button_level/2.png"
                    size_hint: None, None
                    size: 320, 200
                    on_release: root.select_level(2)

                ClickableImage:
                    source: "buttons/button_level/3.png"
                    size_hint: None, None
                    size: 320, 200
                    on_release: root.select_level(3)