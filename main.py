import time
import tkinter as tk
import sys
import re

INPUT_PATTERN = r"\d{2}:\d{2}"
on = True


def main():
    # The time is defined using command line arguments

    # only run if one command line argument is provided
    if len(sys.argv) == 1:
        seconds = 60*25  # Default: 25 minutes

    elif len(sys.argv) == 2:
        if re.match(INPUT_PATTERN, sys.argv[1].strip()):
            seconds = inputToSeconds(sys.argv[1].strip())

        else:
            print("ERROR: Argument must have the form `mm:ss`.")
            sys.exit()

    else:
        print("Wrong argument provided. It has to be in the form `mm:ss`.")
        sys.exit()

    class Application(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("pypomodoro")
            self.createWidgets()

        def createWidgets(self):
            textInfo = f"Great Work!\n{seconds//60:02d}:{seconds%60:02d}" + \
                       " minutes completed"
            self.infoFrame = tk.Frame(self)
            self.infoFrame.pack()
            self.titleFrame = tk.Label(self.infoFrame, text="PyPomodoro",
                                       font="Courier 20")
            self.titleFrame.pack()
            self.infoLabel = tk.Label(self.infoFrame, text=textInfo,
                                      font="Courier 16")
            self.infoLabel.pack(pady=5, padx=5)
            self.resetButton = tk.Button(
                self,
                text="Repeat another session of " +
                     f"{seconds//60:02d}:{seconds%60:02d} minutes",
                font="Courier 14",
                command=self.delayNext
            )
            self.resetButton.pack(fill="x")
            self.quitButton = tk.Button(
                self, text="Quit", font="Courier 14", command=self.quitAll
            )
            self.quitButton.pack(fill="x")

        def delayNext(self):
            # print("destroy")
            self.destroy()

        def quitAll(self):
            global on
            on = False
            # print("Closing app!")
            self.quit()

    while on:
        app = Application()
        # print("window created")

        # for i in range(delaySeconds, 0, -1):
        #     print(str(i))
        #     print("\033[A\033[A")
        #     # sys.stdout.write(str(i)+' ')
        #     # sys.stdout.flush()
        #     time.sleep(1)
        time.sleep(seconds)

        # print("sleep time over")
        app.mainloop()
    # time.sleep(5)


def inputToSeconds(x):
    """
    Assumes input in the form `mm:ss`, where m and s are decimal digits.
    Returns an integer representing the amount of seconds the input means.
    """
    minutes, seconds = x.split(":")
    return int(minutes) * 60 + int(seconds)


if __name__ == "__main__":
    main()
