# Creating the necessary function to reduce the list
def reduce_polygon(polygon_list):
    """Reduces the ammount of points to draw a polygon to only the points needed.
    
    Args:
        polygon_list: A list of tuples containing x and y coordinates of the points that form the original polygon.

    Returns:
        A reduced list of tuples that use only the needed points to draw that same polygon.
    """

    # Starting the index variable
    i = 0

    while i <= len(polygon_list):
        try:

            # Checking if the x or y coordinate of index + 2 is the same as in the index position and index + 1 position
            # If it is, it means that we are using more than 2 points to draw a line, and that isn't necessary
            if (polygon_list[i + 2][0] == polygon_list[i][0] and polygon_list[i + 2][0] == polygon_list[i + 1][0]) \
            or (polygon_list[i + 2][1] == polygon_list[i][1] and polygon_list[i + 2][1] == polygon_list[i + 1][1]):

                # Removing the unnecessary point from the list
                polygon_list.remove(polygon_list[i + 1])
            else:
                pass
            i = i + 1
        
        # End the function when the index + 2 doesn't exist anymore
        except IndexError:
            break

    return polygon_list

# Driver code
if __name__ == "__main__":
    # Using the given example as a list of coordinates
    example_list = [(1,1), (1,2), (1,3), (2,3), (2,4), (3,4), (3,3), (3,2), (2,2), (2,1), (1,1)]

    # Calling the function to check
    results = reduce_polygon(example_list)
    print(results)