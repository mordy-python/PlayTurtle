from tkinter import messagebox
import turtle
import tkinter as tk
from tkinter import END, TOP, ttk
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfile, asksaveasfile

def open_file():
	file = askopenfile('r', filetypes =[('Python Files', '*.py')], initialdir=".")
	root.title(f"Play Turtle - {file.name}")
	code_ = file.read()
	file.close()
	code.delete('1.0', END)
	code.insert('1.0', code_)

def save_file():
	save_to = asksaveasfile(mode='w', filetypes =[('Python Files', '*.py')])
	root.title(f"Play Turtle - {save_to.name}")
	save_to.write(code.get('1.0', END))
	save_to.close()

env = {
	"forward": lambda x: bob.fd(float(x)),
	"back": lambda x: bob.bk(float(x)),
	"right": lambda x: bob.rt(float(x)),
	"left": lambda x: bob.lt(float(x)),
	"speed": lambda x: bob.speed(float(x)),
	"width": lambda x: bob.width(float(x)),
	"shape": lambda x: bob.shape(x),
	"fd": lambda x: bob.fd(float(x)),
	"bk": lambda x: bob.bk(float(x)),
	"rt": lambda x: bob.rt(float(x)),
	"lt": lambda x: bob.lt(float(x)),
	"square": lambda x: square(float(x)),
	"circle": lambda x: circle(float(x)),
	"color": lambda x: color(x),
	"hide": lambda: bob.ht(),
	"show": lambda: bob.st(),
	"begin-fill": lambda: bob.begin_fill(),
	"end-fill": lambda: bob.end_fill(),
	"bgcolor": lambda x: screen.bgcolor(x),
}


def execute_command(command, arg):
	env.get(command)(arg)


def set_var(env: dict, args):
	env.update({args[0]: args[1]})


def run_code():
	bob.reset()
	lines = code.get("1.0", END).strip().split("\n")
	for line in lines:
		func = line.split()
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
			times = env.get(times, times)
			commands = " ".join(func[2:])
			commands = commands.split(";")
			for idx, _ in enumerate(commands):
				commands[idx] = commands[idx].strip().split()
			for _ in range(int(times)):
				for command in commands:
					execute_command(command[0], command[1])
			continue
		elif func[0] == "set":
			set_var(env, func[1:])
			continue
		command = env.get(func[0])
		if command == None:
			showerror(f"{func[0]} Not Found", message=f"{func[0]!r} was not found")
		else:
			try:
				try:
					command(func[1])
				except ValueError:
					command(env.get(func[1]))
			except IndexError:
				if func[0] in ("hide", "show", "begin-fill", "end-fill"):
					command()
				else:
					showerror(
						"Missing Argument",
						f"It appears that an argument is missing in {func[0]!r}",
					)


def square(size):
	for _ in range(4):
		bob.fd(size)
		bob.rt(90)


def circle(size):
	bob.circle(size)


def color(color_str):
	bob.color(color_str)


root = tk.Tk()
root.title("Play Turtle")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="turtle.png"))

menubar = tk.Menu(root, tearoff=False)
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menubar, tearoff=False)
helpmenu.add_command(label="Help")
helpmenu.add_command(label="About")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)


canvas = tk.Canvas(root)
canvas.config(width=800, height=700)
canvas.pack(side=tk.RIGHT)

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("cyan")

code = tk.Text(root, width=30, height=40)
code.pack()

bob = turtle.RawTurtle(screen, shape="turtle")

run = ttk.Button(root, text="Run", command=run_code, width=30)
run.pack()

root.mainloop()
