from kivy.app import App
from kivy.core.window import Window


class WindowFileDropExampleApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        print("**" * 20)
        print("THIS IS THE FILE PATH: ", file_path)
        print("**" * 20)
        return


if __name__ == "__main__":
    WindowFileDropExampleApp().run()
