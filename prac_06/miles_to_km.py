from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Miles_to_KmApp(App):

    def build(self):
        Window.size = (400, 200)
        self.title = "Miles to Km"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        result = value * 1.6
        self.root.ids.output_label.text = str(result)

    def plus_one(self,value):
        result = value + 1
        self.root.ids.input_number.text = str(result)

    def minus_one(self,value):
        result = value - 1
        self.root.ids.input_number.text = str(result)


Miles_to_KmApp().run()