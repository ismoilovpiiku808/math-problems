def calculate_area(shape, dimensions):
    if shape == "circle":
        radius = float(dimensions[0])
        area = 3.1415 * (radius ** 2)
    elif shape == "rectangle":
        length = float(dimensions[0])
        width = float(dimensions[1])
        area = length * width
    elif shape == "triangle":
        base = float(dimensions[0])
        height = float(dimensions[2])
        area = 0.5 * base * height
    else:
        raise ValueError("Invalid shape: {}".format(shape))
    
    return area

dimensions = [1.0, 2.0]  # Example dimensions for a rectangle
area = calculate_area("rectangle", dimensions)
print(area)  # Output will be the calculated area of the rectangle
