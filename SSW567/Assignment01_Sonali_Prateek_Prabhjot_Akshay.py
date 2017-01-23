import unittest


def classifyTriangle(a , b , c):
    if a > 0 and b > 0 and c > 0:
        a , b , c = sorted ( [ a , b , c ] )
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            else:
                if c * c == a * a + b * b:
                    return "Right"
                elif (a == b) or (a == c) or (b == c):
                    return "Isosceles"
                else:
                    return "Scalene"
        else:
            return "False"


# tests for method
class checkTriangleTests ( unittest.TestCase ):
    def testOne(self):
        self.assertEqual ( classifyTriangle ( 5 , 5 , 5 ) , "Equilateral" )
        # fail unless :- assertEquals

    def testTwo(self):
        self.assertNotEqual ( classifyTriangle ( 5 , 5 , 5 ) , "Right" )
        # fail if :- assertNotEquals

    def testThree(self):
        self.assertEqual ( classifyTriangle ( 5 , 3 , 4 ) , "Right" )
        # fail unless :- assertEquals

    def testFour(self):
        self.assertEqual ( classifyTriangle ( 2 , 3 , 2 ) , "Isosceles" )
        # fail unless :- assertEquals

    def testFive(self):
        self.assertNotEqual ( classifyTriangle ( 5 , 8 , 9 ) , "Equilateral" )
        # fail unless :- assertNotEquals

    def testSix(self):
        self.assertEqual ( classifyTriangle ( 5 , 8 , 9 ) , "Scalene" )
        # fail unless :- assertEquals


def main():
    unittest.main ( )


if __name__ == '__main__':
    main ( )
