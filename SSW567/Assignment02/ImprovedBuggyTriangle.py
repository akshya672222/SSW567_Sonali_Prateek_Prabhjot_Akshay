import unittest

def classifyTriangle(a, b, c):
    try:
        a, b, c = sorted([int(a), int(b), int(c)])

        if not (0 < a <= 200 or 0 < b <= 200 or 0 < c <= 200):
            return "Invalid Input1"

        x, y, z = a + b, b + c, c + a
        if not (x > c and y > a and z > b):
            return "Invalid Input2"

        p, q, r = a*a, b*b, c*c

        if a == b == c:
            return "Equilateral"
        elif r == p + q:
            return "Right"
        elif a == b or b == c or c == b:
            return "Isosceles"
        else:
            return "Scalene"
    except ValueError as e:
        return "Invalid Input"


# tests for method
class checkTriangleTests ( unittest.TestCase ):
    def testToRun1(self):
        self.assertEqual ( classifyTriangle ( 5 , 3 , 5 ) , "Isosceles" )

    def testToRun2(self):
        self.assertEqual ( classifyTriangle ( 5 , 5 , 5 ) , "Equilateral" )

    def testToRun3(self):
        self.assertEqual ( classifyTriangle ( 6, 4, 5 ) , "Scalene" )

    def testToRun4(self):
        self.assertEqual ( classifyTriangle ( 4, 5, 3 ) , "Right" )

    def testToRun5(self):
        self.assertEqual ( classifyTriangle ( "a" , 3 , 5 ) , "Invalid Input" )

    def testToRun6(self):
        self.assertEqual ( classifyTriangle ( 200, 5, 3 ) , "Invalid Input" )

    def testToRun7(self):
        self.assertEqual ( classifyTriangle ( 4, -1, 3 ) , "Invalid Input" )

    def testToRun8(self):
        self.assertEqual ( classifyTriangle ( 10, 15, 10 ) , "Isosceles" )

    def testToRun9(self):
        self.assertEqual ( classifyTriangle ( 10, 10, 40 ) , "Invalid Input" )

    def testToRun10(self):
        self.assertEqual ( classifyTriangle ( 4, 4, 2 ) , "Isosceles" )


def main():
    unittest.main ( )


if __name__ == '__main__':
    main ( )
