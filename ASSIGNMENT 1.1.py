
# LOWER TRIANGLE 
def lower_triangle(n):
    print("Lower Triangular Pattern:\n")
    for i in range(1, n + 1):
        print("* " * i)
    print("\n")  

# UPPER TRIANGLE
def upper_triangle(n):
    print("Upper Triangular Pattern:\n")
    for i in range(n, 0, -1):
        print("* " * i)
    print("\n")  


# CENTERED TRIANGLE
def pyramid_pattern(n):
    print("Centered Pyramid Pattern:\n")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print("\n")  

# Main execution Program
if __name__ == "__main__":
    rows = 5  
    lower_triangle(rows)
    upper_triangle(rows)
    pyramid_pattern(rows)
