import turtle
import tkinter as tk
import os
from tkinter import END, ttk
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import List


class App:
	def __init__(self) -> None:
		self.title_str = "Play Turtle"
		self.filename = None

		self.root = tk.Tk()
		self.root.title(self.title_str)
		if os.path.exists('turtle.png'):
			self.root.iconphoto(True, tk.PhotoImage(file="turtle.png"))

		self.menubar = tk.Menu(self.root, tearoff=False)
		self.root.config(menu=self.menubar)

		self.filemenu = tk.Menu(self.menubar, tearoff=False)
		self.filemenu.add_command(label="Open", command=self.open_file)
		self.filemenu.add_command(label="Save", command=self.save)
		self.filemenu.add_command(label="Save As", command=self.save_file)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.root.quit)

		self.helpmenu = tk.Menu(self.menubar, tearoff=False)
		self.helpmenu.add_command(label="Help")
		self.helpmenu.add_command(label="About")

		self.menubar.add_cascade(label="File", menu=self.filemenu)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)

		self.canvas = tk.Canvas(self.root)
		self.canvas.config(width=800, height=700)
		self.canvas.pack(side=tk.RIGHT)

		self.screen = turtle.TurtleScreen(self.canvas)
		self.screen.bgcolor("cyan")

		self.code = tk.Text(self.root, width=30, height=40)
		self.root.bind("<Control-o>", lambda e: self.open_file())
		self.root.bind("<Control-s>", lambda e: self.save())
		self.root.bind("<Control-S>", lambda e: self.save_file())
		self.root.bind("<Control-Return>", lambda e: self.run_code())
		self.code.bind("<KeyPress>", self.key_press)
		self.code.pack()

		self.bob = turtle.RawTurtle(self.screen, shape="turtle")

		self.run = ttk.Button(self.root, text="Run", command=self.run_code, width=30)
		self.run.pack()

		self.env = {
			"forward": lambda x: self.bob.fd(float(x)),
			"back": lambda x: self.bob.bk(float(x)),
			"right": lambda x: self.bob.rt(float(x)),
			"left": lambda x: self.bob.lt(float(x)),
			"speed": lambda x: self.bob.speed(float(x)),
			"width": lambda x: self.bob.width(float(x)),
			"shape": lambda x: self.bob.shape(x),
			"fd": lambda x: self.bob.fd(float(x)),
			"bk": lambda x: self.bob.bk(float(x)),
			"rt": lambda x: self.bob.rt(float(x)),
			"lt": lambda x: self.bob.lt(float(x)),
			"square": lambda x: self.square(float(x)),
			"circle": lambda x: self.circle(float(x)),
			"color": lambda x: self.color(x),
			"hide": lambda: self.bob.ht(),
			"show": lambda: self.bob.st(),
			"begin-fill": lambda: self.bob.begin_fill(),
			"end-fill": lambda: self.bob.end_fill(),
			"bgcolor": lambda x: self.screen.bgcolor(x),
		}

	def execute_command(self, command, arg):
		self.env.get(command)(arg)

	def set_var(self, env: dict, args):
		self.env.update({args[0]: args[1]})

	def color(self, color_str):
		self.bob.color(color_str)

	def circle(self, radius):
		self.bob.circle(radius)

	def square(self, length):
		for _ in range(4):
			self.bob.fd(length)
			self.bob.rt(90)

	def run_app(self):
		self.root.mainloop()

	def run_code(self):
		self.bob.reset()
		lines = self.code.get("1.0", END).strip().split("\n")
		for line in lines:
			func: List[str] = line.split()
			if len(func) == 0 or func[0].startswith("#"):
				continue
			elif line.startswith("!py "):
				line = line.split(" ")
				line.pop(0)
				line = " ".join(line)
				exec(line, globals(), locals())
				continue
			elif func[0] == "loop":
				times = func[1].strip("times")
				times = self.env.get(times, times)
				commands = " ".join(func[2:])
				commands = commands.split(";")
				for idx, _ in enumerate(commands):
					commands[idx] = commands.strip()
				for _ in range(int(times)):
					for command in commands:
						self.execute_command(command[0], command[1])
				continue
			elif func[0] == "set":
				self.set_var(self.env, func[1:])
				continue
			command = self.env.get(func[0])
			if command == None:
				showerror(
					f"{func[0]!r} Not Found", message=f"{func[0]!r} was not found"
				)
			else:
				try:
					command(self.env.get(func[1], func[1]))
				except IndexError:
					if func[0] in ("hide", "show", "begin-fill", "end-fill"):
						command()
					else:
						showerror(
							"Missing Argument",
							f"It appears that {func[0]!r} is missing a parameter",
						)

	def open_file(self):
		file = askopenfile(
			"r",
			filetypes=[("Play Turtle Files", "*.pty"), ("All Files", "*.*")],
			initialdir=".",
		)
		self.filename = file.name
		self.root.title(f"{self.title_str} - {self.filename}")
		code_ = file.read()
		file.close()
		self.code.delete("1.0", END)
		self.code.insert("1.0", code_)

	def save(self):
		if self.filename:
			with open(self.filename, "w") as file:
				file.write(self.code.get("1.0", END))
			self.root.title(f"{self.title_str} - {self.filename}")
		else:
			self.save_file()

	def save_file(self):
		save_to = asksaveasfile(
			mode="w",
			filetypes=[("Play Turtle Files", "*.pty"), ("All Files", "*.*")],
			defaultextension=".pty",
			initialdir=".",
		)
		self.filename = save_to.name
		self.root.title(f"{self.title_str} - {self.filename}")
		save_to.write(self.code.get("1.0", END))
		save_to.close()

	def key_press(self, event: tk.Event):
		if self.filename:
			self.root.title(f"{self.title_str} - {self.filename} *")
		else:
			self.root.title(f"{self.title_str} *")

def play():
	app = App()
	app.run_app()

if __name__ == "__main__":
	play()