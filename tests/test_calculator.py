from unittest import TestCase, main
from calculate import calc


class TestCalculator(TestCase):
    def test_correct_figure_func_value(self):
        figure = "circle"
        func = "area"
        radius = 1
        answer = calc(figure, func, [radius])
        self.assertEqual(answer, 3.141592653589793)

    def test_correct_figure_func_wrong_value(self):
        figure = "square"
        func = "perimeter"
        side = "abc"
        with self.assertRaises(AssertionError):
            calc(figure, func, [side])

    def test_correct_figure_wrong_func_value(self):
        figure = "square"
        func = "is_triangle"
        side = "some words"
        with self.assertRaises(AssertionError):
            calc(figure, func, [side])

    def test_wrong_figure_func_value(self):
        figure = "figure"
        func = "get_vectors"
        side = "some words"
        with self.assertRaises(AssertionError):
            calc(figure, func, [side])

    def test_string_values(self):
        figure = "triangle"
        func = "area"
        sides = ["1", "2", "3"]
        with self.assertRaises(AssertionError):
            calc(figure, func, sides)

    def test_over_values(self):
        figure = "square"
        func = "area"
        sides = [1, 2, 3]
        with self.assertRaises(TypeError):
            calc(figure, func, sides)

    def test_over_parameters(self):
        figure = "square"
        func = "area"
        sides = [1]
        with self.assertRaises(TypeError):
            calc(figure, func, sides, True)


if __name__ == "__main__":
    main()
