from gui.app_gui import GuiApp

class Main:

    def __init__(self):
        self.gui = GuiApp()

    def compute_program(self):
        self.gui.create_main_gui()

if __name__ == "__main__":
    main = Main()
    main.compute_program()


