"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Veronica Gawarecki.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate them. """
    run_test_draw_L()
    run_test_draw_wall_on_right()


def run_test_draw_L():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = 'Draw an L of circles.  Two tests'
    window = rg.RoseWindow(width, height, title)

    window.continue_on_mouse_click('Click to run Test 1.')

    # ------------------------------------------------------------------
    starting_point = rg.Point(50, 50)
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # First L.
    # ------------------------------------------------------------------
    radius = 10
    starting_circle = rg.Circle(starting_point, radius)
    green_circle = starting_circle.clone()
    green_circle.fill_color = 'green'

    draw_L(window, green_circle, 10, 5)
    window.continue_on_mouse_click('Click to run Test 2.')

    # ------------------------------------------------------------------
    # Second L.
    # ------------------------------------------------------------------
    starting_circle.move_by(250, 100)
    blue_circle = starting_circle.clone()
    blue_circle.fill_color = 'blue'

    window.continue_on_mouse_click('Click to run Test 2.')
    draw_L(window, blue_circle, 6, 15)

    window.close_on_mouse_click()


def draw_L(window, circle, r, c):
    """
    See   L.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an 'L' of circles on the given rg.RoseWindow.
      The 'column' part of the L should have r rows and 3 columns.
        (That is, it is r 'tall' and 3 'thick'.)
      The 'shared corner' part of the L should be 3 x 3.
      The 'row' part of the L should have c columns and 3 rows.
        (That is, it is c 'long' and 3 'thick'.)

      The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
      - The fill_color that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type r: int
      :type c: int
    and m and n are small, positive integers.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    circle.attach_to(window)
    for k in range(r+3):
        circle.attach_to(window)
        circle1=rg.Circle(rg.Point(circle.center.x,circle.center.y+(circle.radius)*2*(k)),circle.radius)
        circle1.fill_color=circle.fill_color

        circle1.attach_to(window)
        window.render(.1
                      )
        for j in range(3):
            circle2=rg.Circle(rg.Point(circle.center.x+(circle.radius)*2*(j),circle1.center.y),circle.radius)
            circle2.fill_color=circle.fill_color
            circle2.attach_to(window)
            window.render(.1)
    tempcircle=rg.Circle(rg.Point(circle.center.x+6*circle.radius,circle.center.y+2*r*circle.radius),circle.radius)

    for k in range (3):
        circle3=rg.Circle(rg.Point(tempcircle.center.x,tempcircle.center.y+circle.radius*2*k),circle.radius)
        circle3.fill_color=circle.fill_color
        circle3.attach_to(window)
        window.render(.1)
        for j in range(c):
            circle4=rg.Circle(rg.Point(circle3.center.x+circle.radius*2*j,circle3.center.y),circle.radius)
            circle4.fill_color=circle.fill_color
            circle4.attach_to(window)
            window.render(.1)


def run_test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    window.continue_on_mouse_click('Click to run Test 1.')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), rg.Point(250 + 30, 30 + 20))
    draw_wall_on_right(rectangle1, 8, window)

    window.continue_on_mouse_click('Click to run Test 2.')
    rectangle2 = rg.Rectangle(rg.Point(470, 40), rg.Point(470 + 50, 40 + 50))
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    point1=rectangle.get_upper_right_corner()
    point2=rectangle.get_lower_left_corner()
    dx=rectangle.get_width()
    dy=rectangle.get_height()

    for k in range(n):
        newrec=rg.Rectangle(rg.Point(point1.x,point1.y+dy*k),rg.Point(point2.x,point2.y+dy*k))
        newrec.attach_to(window)
        for j in range(k):
            point3=newrec.get_lower_left_corner()
            point4=newrec.get_upper_right_corner()
            newrec2=rg.Rectangle(rg.Point(point3.x-dx*(j+1),point3.y),rg.Point(point4.x-dx*(j+1),point4.y))
            newrec2.attach_to(window)
            window.render(.1)


    window.render()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
