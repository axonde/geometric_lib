def area(a, b, c):
    '''
    Return area of a triangle by three sides

        Args:
            a (int): first side
            b (int): second side
            c (int): third side

        Return value:
            area (float): area of the given triangle
    '''

    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5


def perimeter(a, b, c):
    '''
    Return triangle perimiter by given sides.

        Args:
            a (int): first side
            b (int): second side
            c (int): third side

        Return value:
            perimeter (int): perimiter of the given triangle
    '''

    return a + b + c
