from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp


class TestApp(App):
    def build(self):
        self.title = 'Test App'
        root = BoxLayout(orientation='vertical', padding=dp(24), spacing=dp(16))
        self.label = Label(
            text='سلام!\nاین یک تست سادهٔ Kivy است.',
            font_size='20sp',
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))
        btn = Button(text='تست موفق', size_hint_y=None, height=dp(52), font_size='18sp')
        btn.bind(on_release=self.on_press)
        root.add_widget(self.label)
        root.add_widget(btn)
        return root

    def on_press(self, *_):
        self.label.text = 'دکمه با موفقیت لمس شد ✅'


if name == '__main__':
    TestApp().run()
