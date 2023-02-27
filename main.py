import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.score = 0
        self.cpu_score = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.show_score = tk.Text(root, height=1, width=50)
        self.show_score.pack()

        self.text = tk.Text(root, height=10, width=50)
        self.text.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="right")

        self.new = tk.Button(self, text="New Game", fg="blue")
        self.new["command"] = self.clear
        self.new.pack(side="right")

        self.rock = tk.Button(self)
        self.rock["text"] = "Rock"
        self.rock["command"] = self.say_rock
        self.rock.pack(side="bottom")

        self.paper = tk.Button(self)
        self.paper["text"] = "Paper"
        self.paper["command"] = self.say_paper
        self.paper.pack(side="left")

        self.scissors = tk.Button(self)
        self.scissors["text"] = "Scissors"
        self.scissors["command"] = self.say_scissors
        self.scissors.pack(side="left")

        self.show_score.config(state=tk.DISABLED)
        self.text.config(state=tk.DISABLED)

    def say_rock(self):
      self.user = "ROCK"
      self.text.config(state=tk.NORMAL)
      self.text.insert(tk.END, "You picked rock! \n")
      self.text.config(state=tk.DISABLED)
      self.rock["state"] = tk.DISABLED
      self.paper["state"] = tk.DISABLED
      self.scissors["state"] = tk.DISABLED
      self.random()

    def say_paper(self):
      self.user = "PAPER"
      self.text.config(state=tk.NORMAL)
      self.text.insert(tk.END, "You picked paper! \n")
      self.text.config(state=tk.DISABLED)
      self.rock["state"] = tk.DISABLED
      self.paper["state"] = tk.DISABLED
      self.scissors["state"] = tk.DISABLED
      self.random()

    def say_scissors(self):
      self.user = "SCISSORS"
      self.text.config(state=tk.NORMAL)
      self.text.insert(tk.END, "You picked scissors! \n")
      self.text.config(state=tk.DISABLED)
      self.rock["state"] = tk.DISABLED
      self.paper["state"] = tk.DISABLED
      self.scissors["state"] = tk.DISABLED
      self.random()

    def clear(self):
      self.text.config(state=tk.NORMAL)
      self.text.delete('1.0', tk.END)
      self.rock["state"] = tk.NORMAL
      self.paper["state"] = tk.NORMAL
      self.scissors["state"] = tk.NORMAL

    def random(self):
      self.num = random.randint(1, 3)

      if self.num == 1:
        self.cpu_move = "ROCK"
      elif self.num == 2:
        self.cpu_move = "PAPER"
      elif self.num == 3:
        self.cpu_move = "SCISSORS"

      self.text.config(state=tk.NORMAL)
      self.text.insert(tk.END, "CPU picked...\n")
      self.text.insert(tk.END, f"{self.cpu_move}!\n")

      if self.cpu_move == self.user:
        self.text.insert(tk.END, f"You and CPU picked {self.user}!\nIt's a DRAW")
      elif self.cpu_move == "SCISSORS" and self.user == "ROCK":
        self.text.insert(tk.END, f"You picked {self.user} and CPU picked {self.cpu_move}!\nUser WINS! ")
        self.score += 1
      elif self.cpu_move == "ROCK" and self.user == "PAPER":
        self.text.insert(tk.END, f"You picked {self.user} and CPU picked {self.cpu_move}!\nUser WINS! ")
        self.score += 1
      elif self.cpu_move == "PAPER" and self.user == "SCISSORS":
        self.text.insert(tk.END, f"You picked {self.user} and CPU picked {self.cpu_move}!\nUser WINS! ")
        self.score += 1
      elif self.cpu_move == "SCISSORS" and self.user == "PAPER":
        self.text.insert(tk.END, f"You picked {self.user} and CPU picked {self.cpu_move}!\nUser LOSES! ")
        self.cpu_score += 1
      elif self.cpu_move == "ROCK" and self.user == "SCISSORS":
        self.text.insert(tk.END, f"You picked {self.user} and CPU picked {self.cpu_move}!\nUser LOSES! ")
        self.cpu_score += 1
      elif self.cpu_move == "PAPER" and self.user == "ROCK":
        self.text.insert(tk.END, f"You picked {self.user} and CPU picked {self.cpu_move}!\nUser LOSES! ")
        self.cpu_score += 1
      
      self.text.config(state=tk.DISABLED)
      self.update_score()
        
    def update_score(self):
      self.show_score.config(state=tk.NORMAL)
      self.show_score.delete('1.0', tk.END)
      self.show_score.insert(tk.END, f"User: {self.score} CPU: {self.cpu_score}")
      self.show_score.config(state=tk.DISABLED)

root = tk.Tk()
root.title('Rock Paper Scissors by Calvin Liew')
app = Application(master=root)
app.mainloop()
