from logger_file import log

class Person:
    def __init__(self, person_id=None, first_name=None, last_name=None, email=None):
        self._person_id = person_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value

    def __str__(self):
        return f'<Person {self.first_name}>'

if __name__ == '__main__':
    me = Person(1, 'Josue', 'Canaviri', 'josue@gmailcom')
    log.debug(me)

    # Simular un insert
    john = Person(first_name='John', last_name='Doe', email='john@gmail.com')
    log.debug(john)

    # Simular un delete
    susan = Person(person_id=1)
    log.debug(susan)
