from unittest import TestCase, main
import circle
import square
import triangle

class TestGeometry(TestCase):
    def test_circle_area(self):
        # arrange
        radius = 5
        # act
        result = circle.area(radius)
        # assert
        self.assertEqual(result, 78.53981633974483)

    def test_circle_perimiter(self):
        radius = 17
        result = circle.perimeter(radius)
        self.assertEqual(result, 106.81415022205297)

    def test_square_area(self):
        side = 12
        result = square.area(side)
        self.assertEqual(result, 144)

    def test_square_perimiter(self):
        side = 11
        result = square.perimeter(side)
        self.assertEqual(result, 44)
    
    def test_triangle_area(self):
        sides = [3, 4, 5]
        result = triangle.area(*sides)
        self.assertEqual(result, 6)

    def test_triangle_perimiter(self):
        sides = [5, 9, 1]
        result = triangle.perimeter(*sides)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    main()