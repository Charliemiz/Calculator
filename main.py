from gui import *


def main():
    window = Tk()
    window.title('Calculator')
    window.resizable(False, False)

    Calculator(window)
    window.mainloop()


if __name__ == '__main__':
    main()
