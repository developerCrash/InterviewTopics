def generate_lists(start, end):
    numbers = list(range(start, end + 1))
    squares = list(map(lambda x: x ** 2, numbers))
    cubes = list(map(lambda x: x ** 3, numbers))

    return numbers, squares, cubes

if __name__ == &quot;__main__&quot;:
    start_num = 1  # Start number
    end_num = 5    # End number

    numbers_list, squares_list, cubes_list = generate_lists(start_num, end_num)

    # Print the lists
    print(&quot;Numbers:&quot;, numbers_list)
    print(&quot;Squares:&quot;, squares_list)
    print(&quot;Cubes:&quot;, cubes_list)
