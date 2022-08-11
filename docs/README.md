Play Turtle provides a way for children to learn programming by moving a turtle on the screen

It provides a subset of commands found in Python's Turtle module to abstract away complicated programming ideas.

<details>
<summary>Table of Contents</summary>

* [Installation](#installation)
* [Commands](#play-turtle-commands)

</details>

## Installation

There are multiple ways to install Play Turtle

With pip

```sh
$ pip install playturtle
# Provides the play-turtle command
```

Clone the repo and run locally

```sh
$ git clone https://github.com/mordy-python/PlayTurtle
$ cd PlayTurtle
$ python playturtle.py
# Can also install with `pip install .`
# Will provide the `play-turtle` command 
```

## Play Turtle Commands

* <a href="#forward">`Forward`</a>
* <a href="#back">`Back`</a>
* <a href="#right">`Right`</a>
* <a href="#left">`Left`</a>
* <a href="#speed">`Speed`</a>
* <a href="#width">`Width`</a>
* <a href="#shape">`Shape`</a>
* <a href="#square">`Square`</a>
* <a href="#circle">`Circle`</a>
* <a href="#color">`Color`</a>
* <a href="#hide">`Hide`</a>
* <a href="#show">`Show`</a>
* <a href="#begin-fill">`Begin fill`</a>
* <a href="#end-fill">`End fill`</a>
* <a href="#bgcolor">`Bgcolor`</a>

### Forward

* Syntax
  * Command: `forward`
  * Parameters: `distance`
* What it does
  * The `forward` command moves the turtle on the screen, drawing a line behind it.
  * The `distance` parameter tells the turtle how far to move.

### Back

* Syntax
  * Command: `back`
  * Parameters: `distance`
* What it does
  * The `back` command moves the turtle backward on the screen, drawing a line in front of it.
  * The `distance` parameter tells the turtle how far to move.

### Right

* Syntax
  * Command: `right`
  * Parameters: `degrees`
* What it does
  * The `right` command turns the turtle right.
  * The `degrees` parameter tells the turtle how many degrees to rotate.

### Left

* Syntax
  * Command: `left`
  * Parameters: `degrees`
* What it does
  * The `left` command turns the turtle left.
  * The `degrees` parameter tells the turtle how many degrees to rotate.

### Speed

* Syntax
  * Command: `speed`
  * Parameters: `new-speed`
* What it does
  * The `speed` command sets the turtles drawing speed.
  * The `new-speed` parameter tells the turtle how fast it should move.

### Width

* Syntax
  * Command: `width`
  * Parameters: `new-width`
* What it does
  * The `width` command sets the turtles width (in pixels).
  * The `new-width` parameter specifies what the new width of the turtle should be.

### Shape

* Syntax
  * Command: `shape`
  * Parameters: `new-shape`
* What it does
  * The `shape` command changes the turtle's shape.
  * The `new-shape` parameter specifies what shape should be displayed.
    > Note: The `new-shape` parameter can only be on of the following: arrow, circle, turtle, square, triangle, classic

### Square

* Syntax
  * Command: `square`
  * Parameters: `side-length`
* What it does
  * The `square` command draws a square on the screen
  * The `side-length` parameter determines how long the sides of the square will be

### Circle

* Syntax
  * Command: `circle`
  * Parameters: `radius`
* What it does
  * The `circle` command draws a circle on the screen
  * The `radius` parameter determines how big the circle will be

### Color

* Syntax
  * Command: `color`
  * Parameters: `new-color`
* What it does
  * The `color` command changes the color of the turtle and of the lines it draws
  * The `new-color` parameter specifies what color to change to
    > See a list of all named colors [here](https://trinket.io/docs/colors)

### Hide

* Syntax
  * Command: `hide`
  * Paramters: none
* What it does
  * The `hide` command hides the turtle. It will still draw, it just won't be visible

### Show

* Syntax
  * Command: `show`
  * Paramters: none
* What it does
  * The `show` command shows the turtle if it's hidden. If it's already visible, it does nothing

### Begin Fill

* Syntax
  * Command: `begin-fill`
  * Paramters: none
* What it does
  * The `begin-fill` command will start the fill process using the current `color`. However, nothing will be filled until `end-fill` is called.

### End Fill

* Syntax
  * Command: `end-fill`
  * Paramters: none
* What it does
  * The `end-fill` command will fill any shapes drawn in between the `begin-fill` command and itself. If there was no `begin-fill` command, `end-fill` will do nothing.

### Bgcolor

* Syntax
  * Command: `bgcolor`
  * Paramters: `new-color`
* What it does
  * The `bgcolor` command changes the background color of the canvas
  * The `new-color` paramter specifies what color it should change to
    > See a list of all named colors [here](https://trinket.io/docs/colors)
