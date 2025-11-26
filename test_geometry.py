import unittest
import geometry_lib.rectangle as rectangle
import geometry_lib.circle as circle
import geometry_lib.square as square
import geometry_lib.triangle as triangle
import math

class RectangleTestCase(unittest.TestCase):
    def test_rect_zero_side(self): 
        area = rectangle.area(10, 0)
        perimeter = rectangle.perimeter(10, 0)
        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 20)
    def test_rect_square(self):
        area = rectangle.area(10, 10)
        perimeter = rectangle.perimeter(10,10)
        self.assertEqual(area, 100)
        self.assertEqual(perimeter, 40)
    def test_rect_different_sides(self):
        area = rectangle.area(8, 12)
        perimeter = rectangle.perimeter(8, 12)
        self.assertEqual(area, 96)
        self.assertEqual(perimeter, 40)

class SquareTestCase(unittest.TestCase):
    def test_square_zero_mult(self): 
        area = square.area(0)
        perimeter = square.perimeter(0)
        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 0)
    def test_square_mul(self):
        area = square.area(10)
        perimeter = square.perimeter(10)
        self.assertEqual(area, 100)
        self.assertEqual(perimeter, 40)

class CircleTestCase(unittest.TestCase):
    def test_circle_zero_radius(self):
        area = circle.area(0)
        perimeter = circle.perimeter(0)
        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 0)
    def test_circle_int_radius(self):
        area = circle.area(28)
        perimeter = circle.perimeter(28)
        self.assertAlmostEqual(area, 28*28*math.pi)
        self.assertAlmostEqual(perimeter, 56*math.pi)
    def test_circle_float_radius(self):
        area = circle.area(4.39)
        perimeter = circle.perimeter(4.39)
        self.assertAlmostEqual(area, 4.39*4.39*math.pi)
        self.assertAlmostEqual(perimeter, 8.78*math.pi)

class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_side(self):
        area = triangle.area(0, 7)
        perimeter = triangle.perimeter(0,7,7)
        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 14)
    def test_triangle_egyptian(self):
        area = triangle.area(5, 24/5)
        perimeter = triangle.perimeter(3,4,5)
        self.assertEqual(area, 12)
        self.assertEqual(perimeter, 12)
    def test_triangle_equilateral(self):
        area = triangle.area(6, 3*math.sqrt(3))
        perimeter = triangle.perimeter(6,6,6)
        self.assertAlmostEqual(area, 9*math.sqrt(3))
        self.assertEqual(perimeter, 18)

class MixedTestCase(unittest.TestCase):
    def test_rectsquare_equality(self):  
        rect = rectangle.area(10, 10)
        sqr = square.area(10)
        self.assertEqual(rect, sqr)
    def test_recttriangle_equality(self):
        rect = rectangle.area(9, 7)
        tri = triangle.area(7, 9)
        self.assertEqual(2*tri, rect)

