# Play Turtle

Play Turtle provides a way for children to learn programming by moving a turtle on the screen

It provides a subset of commands found in Python's Turtle module to abstract away complicated programming ideas.

## Play Turtle Commands

* <a href="#forward">`Forward`</a>
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
    * Parameters: `amount`
* What it does
    * The `forward` command moves the turtle on the screen, drawing a line behind it.
    * The `amount` parameter tells the turtle how far to move

### Back

* Syntax: `back amount`
* Shortcuts: `bk amount`
* The `back` command draws a line `amount` pixels in the opposite direction the turtle is currently facing

### Right

* Syntax: `right degrees`
* Shortcuts: `rt degrees`
* The `right` command rotates the turtle `degrees` degrees to the right

### Left

* Syntax: `left degrees`
* Shortcuts: `lt degrees`
* The `left` command rotates the turtle `degrees` degress to the left

### Speed

* Syntax: `speed new-speed`
* The `speed` command changes the turtles speed. If `new-speed` is `0`, then there will be no animation, everything is drawn before being rendered. If `new-speed` is between `1` and `10`, then, the higher the number, the faster the turtle moves.

### Width

* Syntax: `width new-width`
* The `width` command changes the thickness of the line drawn by the turtle to `new-width` pixels.

### Shape

* Syntax: `shape turtle-shape`
* The `shape` command chnages the shape of the turtle displayed on screen. `turtle-shape` must be one of `arrow`, `turtle`, `circle`, `square`, `triangle`, or `classic`.

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