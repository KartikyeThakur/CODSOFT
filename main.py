from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.result = TextInput(font_size=50, readonly=True, halign='right', multiline=False, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        self.add_widget(self.result)

        buttons = [
            ['AC', '+/-', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, font_size=32, background_normal='', background_color=self.get_button_color(label), size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)

    def get_button_color(self, label):
        if label in ['÷', '×', '-', '+', '=']:
            return (1, 0.6, 0, 1)  # Orange
        elif label in ['AC', '+/-', '%']:
            return (0.5, 0.5, 0.5, 1)  # Gray
        else:
            return (0.3, 0.3, 0.3, 1)  # Dark Gray

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'AC':
            self.result.text = ''
        elif button_text == '=':
            try:
                self.result.text = str(eval(self.result.text.replace('×', '*').replace('÷', '/')))
            except Exception:
                self.result.text = 'Error'
        elif button_text == '+/-':
            if current:
                if current[0] == '-':
                    self.result.text = current[1:]
                else:
                    self.result.text = '-' + current
        elif button_text == '%':
            try:
                self.result.text = str(float(self.result.text) / 100)
            except Exception:
                self.result.text = 'Error'
        else:
            if current and (current[-1] in '+-×÷' and button_text in '+-×÷'):
                self.result.text = current[:-1] + button_text
            else:
                self.result.text += button_text

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()
