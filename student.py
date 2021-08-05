class Student(object):
    def __init__(self, name, last_name, course, is_graduated = False):
        """Constructr
        name - string, student name
        last_name - string, student last_name
        cource - string, format: IP-11 (utf-8)
        is_graduated - booleam, is student graduated"""
        self.name = name
        self.last_name = last_name
        self.cource = course
        self.is_graduated = is_graduated

    def get_full_name(self):
        """Return single string, which contain name and last name"""
        return self.name + ' ' + self.last_name

    def generate_email(self):
        """Return single string, generated email for student"""
        return self.name.lower() + '.' + self.last_name.lower() + '@nulp.ua'

    def graduate(self):
        """Sets attribute is_graduate = True"""
        self.is_graduated = True
