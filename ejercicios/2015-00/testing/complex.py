import unittest
from rectangle import Rectangle
from rectangle import overlap

class RectangleTestCase(unittest.TestCase):
    def setUp(self):
        self.rec = Rectangle()
        self.rec_b = Rectangle()

    def test_default_size(self):
        self.assertEqual(self.rec.size(), (10,10),
                         'incorrect default size')

    def test_resize(self):
        self.rec.resize(100,150)
        self.assertEqual(self.rec.size(), (100,150),
                         'wrong size after resize')
    def test_overlap_symmetry(self):
        self.rec.recenter(0,0)
        self.rec.resize(10,10)
        self.rec_b.recenter(5,4)
        self.rec_b.resize(10,10)
        self.assertEqual(overlap(self.rec, self.rec_b), 
                         overlap(self.rec_b, self.rec), 
                        'wrong overlap symmetry')
