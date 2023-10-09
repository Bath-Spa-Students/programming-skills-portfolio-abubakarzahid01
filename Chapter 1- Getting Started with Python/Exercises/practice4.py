#4:Compute the area of triangle
def area_of_triangle(base, height):
    """
    this function computes the area of a triangle given its base and height.
    """
    return 0.5 * base * height 
# Example usage of the function 
base_value = 5
height_value = 10
triangle_area = area_of_triangle(base_value, height_value)
# Output the computed area 
print("The area of the triangle is", triangle_area)