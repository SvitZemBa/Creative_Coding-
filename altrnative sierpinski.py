import turtle as tu

def draw_circle(diameter):
    """Draw a single circle with the given diameter."""
    tu.pendown()
    tu.circle(diameter / 2)
    tu.penup()

def draw_flower(diameter, depth, petals=5):
    """Recursive function to draw a flower-like structure with evenly arranged petals."""
    if depth == 0:
        draw_circle(diameter)  # Draw the smallest circle
    else:
        # Draw the central circle
        draw_circle(diameter)
        
        # Calculate the angle between petals
        angle = 360 / petals
        
        # Reduce the diameter and depth for recursive petals
        diameter *= 0.5
        depth -= 1
        
        # Draw petals around the current circle
        for _ in range(petals):
            tu.penup()
            tu.forward(diameter * 1.5)  # Move outward for the next petal
            draw_flower(diameter, depth, petals)  # Recursive call
            tu.penup()
            tu.backward(diameter * 1.5)  # Return to the center
            tu.right(angle)  # Rotate for the next petal

def draw_flower_grid(start_diameter, depth, petals, grid_size):
    """Draw a grid of flowers."""
    spacing = start_diameter * 2  # Space between flower centers
    for row in range(grid_size):
        for col in range(grid_size):
            # Move to the starting position for each flower
            x = col * spacing - (grid_size * spacing) / 2
            y = row * spacing - (grid_size * spacing) / 2
            tu.penup()
            tu.goto(x, y)
            tu.pendown()
            # Draw the flower
            draw_flower(start_diameter, depth, petals)

# Set up the turtle
tu.speed(0)  # Fastest drawing speed
tu.hideturtle()

# Draw the grid of flowers
draw_flower_grid(start_diameter=100, depth=2, petals=5, grid_size=4)

tu.exitonclick()

