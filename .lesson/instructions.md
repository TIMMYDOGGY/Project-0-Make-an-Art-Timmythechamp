# Instructions  

## Project description: Make an Art

Use turtle graphics to make some art.

Write your code in `main.py`.

I will laser cut or 3d print your final draft.

Requirements:
* [ ] Two colors: Black (etching color) and White (background color)
    * Optionally, you can also add red lines for places you want to be cut
* [ ] 1 picture that you draw with turtle graphics (or other Python graphics modules)
* [ ] At least 2 variables
    * [ ] When you change the variable, the picture changes accordingly
    * [ ] Your variable can take a range of values.
    * [ ] In the comments, you specify what values the variable can take.
* [ ] At least 2 for loops
    * [ ] At least one of the for loops uses the loop variable to do something slightly different each time it loops through. Here's an example:

      ```python
      # draw a spiral
      # `arm_legnth` is the loop variable
      for arm_length in range(20):
        # the length of the spiral arm is different each iteration
        turtle.forward(arm_length*5) 
        turtle.right(90)
      ```
* [ ] At least 2 functions
  * [ ] Each function is called at least 2 times in your code
  * [ ] At least one function has a parameter
      * [ ] At least two different arguments are supplied to that function


## Project milestones

All project milestones are due **before class** on the day they are due.

* September 14 - Proposal
* September 21 - Rough draft
* (in class Sep 21) - Colleague consultation
* October 2 - Presentations
* October 4 - Final draft

### Proposal

In the file `readme.md`, write a description and/or make a sketch of the drawing you want to try to make.

Answer these questions:

1. Roughly, what will your drawing look like
2. What are two variables you could use so that when you change each variable, the drawing changes?
3. Where is there repetition in your drawing?
4. What are the main parts of your drawing? Are there clear sections or objects?
5. How could you use a loop variable of a for loop? Is there somewhere in your drawing where something is repeated, but it's slightly different each time? Maybe the same object is repeated in different places, or maybe a similar object is repeated but with different sizes?

### Rough draft

The rough draft will be graded just like the final draft will be. It's an opportunity to see if there are any things you are missing or ways to improve it.

### Colleague consultation

You will check your colleague's code to
* see if the requirements of the assignment are being met
* help debug any problems, and
* brainstorm ways to improve the project.

### Presentations

You may use slides if you want, or just show us the code in replit and talk about it.

* 3 minute presentation
  * show your drawing
  * show your code
  * talk about your process (anything particularly interesting, difficult, or cool?)
* 1 minute for questions

## Turtle library reference

Change the variables in **bold** to what you want them to be for your picture.

| Function | Definition |
| --- | --- |
|  turtle.forward(**distance**) | Moves the turtle forward. The number of pixels it goes is **distance**
| turtle.backward(**distance**) | Moves the turtle backward. The number of pixels it goes is **distance**
| turtle.right(**angle**) | Turns the turtle **angle** degrees clockwise
| turtle.left(**angle**) | Turns the turtle **angle** degrees counterclockwise
| turtle.up() | Picks up the turtle’s tail (stops drawing)
| turtle.down() | Puts down the turtle’s tail (starts drawing again)
| turtle.pencolor(**color name**) | Changes the color of the turtle’s tail to **color name**
| turtle.heading() | Returns the current heading (as an angle from the starting heading)
| turtle.position() | Returns the current position (as x,y coordinates)
| turtle.goto(**x**, **y**) | Moves the turtle to position **x**, **y**
| turtle.dot() | Leaves a dot as the current position

You can also explore the [official docs](https://docs.python.org/3/library/turtle.html) for even more.  
