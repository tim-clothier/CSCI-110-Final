def print_traingular_numbers(n) :
    i = 1
    while i <= n :
        tri = calculate_triangular_number(i)
        i += 1
        print(str(int(tri)) + "\n")


def calculate_triangular_number(nth) :
    tri = (nth * (nth + 1)) / 2
    return tri

print_traingular_numbers(int(input("Enter the nth triangular number to calculate up to:")))