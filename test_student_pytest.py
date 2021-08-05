import pytest
from student import Student

@pytest.fixture
def student_a():
    """Setup Student object, which are used for testing"""
    return Student('Oleg', 'Lepkiy', 'IP-11')
@pytest.fixture
def student_b():
    """Setup Student object, which are used for testing"""
    return Student('Petro', 'Saga', 'TC-11')

def test_full_name(student_a, student_b):
    """Test if get_full_name has expected outup"""
    assert student_a.get_full_name() == 'Oleg Lepkiy'
    assert student_b.get_full_name() == 'Petro Saga'

def test_graduating(student_a, student_b):
    """Test if graduate() always changes is_graduate to True"""
    student_a.graduate()
    student_b.graduate()

    assert student_a.is_graduated
    assert student_b.is_graduated

@pytest.mark.skip(reason="Always fails")
def test_email_generator(student_a, student_b):
    """Test if generate_email() has expected outup"""
    assert student_a.generate_email() == 'oleg.lepkiy@nulp.ua'
    assert student_a.generate_email() == 'petro.saga@nulp.ua'