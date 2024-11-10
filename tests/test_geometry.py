from unittest import TestCase, main
import circle
import square
import triangle

class TestGeometry(TestCase):
    def test_circle_area(self):
        self.assertEqual(circle.area(5), 78.53981633974483)

    def test_circle_perimiter(self):
        self.assertEqual(circle.perimeter(17), 106.81415022205297)

    def test_square_area(self):
        self.assertEqual(square.area(12), 144)

    def test_square_perimiter(self):
        self.assertEqual(square.perimeter(11), 44)
    
    def test_triangle_area(self):
        self.assertEqual(triangle.area(3, 4, 5), 6)

    def test_triangle_perimiter(self):
        self.assertEqual(triangle.perimeter(5, 9, 1), 15)

if __name__ == '__main__':
    main()