import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        rn = Runner(name='John')
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn = Runner(name='John1')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):
        runner1 = Runner(name='John2')
        runner2 = Runner(name='John3')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
