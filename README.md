# Play Turtle

Play Turtle provides a way for children to learn programming by moving a turtle on the screen

It provides a subset of commands found in Python's Turtle module to abstract away complicated programming ideas.

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
* <a href="#hide">`Hide `</a>
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

* Syntax: `square side-length`
* Draws a `square` where each side is `side-length` pixels long

### Circle

* Syntax: `circle radius`
* Draws a `circle` that has a radius of `radius`. Keep in mind, the radius is half the diameter of the circle.

### Color

* Syntax: `color new-color`
* Changes the color of the turtle, and the color of all the lines drawn on the screen to the `new-color`. `new-color` can be a hex code, or one of the named colors supported by turtle.
    * See a list of all named colors [here](https://trinket.io/docs/colors)

### Hide

* Syntax: `hide`
* Hides the turtle. The turtle will continue to draw on the canvas, it just won't be visible

### Show

* Syntax: `show`
* Shows the turtle, if it's hidden. If it's already visible, does nothing.

###  Begin Fill

* Syntax: `begin-fill`
* Will fill any shapes drawn with the turtles current color as soon as `end-fill` is called.

### End Fill

* Syntax: `end-fill`
* Fills all shapes drawn in between itself and the `begin-fill` command with the turtles current color.

### Bgcolor

* Syntax: `bgcolor new-color`
* Changes the background color of the canvas. `new-color` can be a hex code, or one of the named colors supported by turtle.
    * See a list of all named colors [here](https://trinket.io/docs/colors)