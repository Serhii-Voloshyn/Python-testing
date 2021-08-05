import unittest
from student import Student

class TestStudentMethods(unittest.TestCase):

    def setUp(self):
        """Setup 2 Student objects, which are used for testing"""
        self.student_a = Student('Oleg', 'Lepkiy', 'IP-11')
        self.student_b = Student('Petro', 'Saga', 'TC-11')

    def test_full_name(self):
        """Test if get_full_name has expected outup"""
        self.assertEqual(self.student_a.get_full_name(), 'Oleg Lepkiy')
        self.assertEqual(self.student_b.get_full_name(), 'Petro Saga')

    def test_graduating(self):
        """Test if graduate() always changes is_graduate to True"""
        self.student_a.graduate()
        self.student_b.graduate()

        self.assertTrue(self.student_a.is_graduated)
        self.assertTrue(self.student_b.is_graduated)

    @unittest.expectedFailure
    def test_email_generator(self):
        """Test if generate_email() has expected outup"""
        self.assertEqual(self.student_a.generate_email(), 'oleg.lepkiy@nulp.ua')
        self.assertEqual(self.student_a.generate_email(), 'petro.saga@nulp.ua')

if __name__ == '__main__':
    unittest.main()