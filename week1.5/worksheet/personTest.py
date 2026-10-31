from datetime import date
from person import Person

p = Person("Alan John Smith", date(2005, 6, 15))

print(p.initials())
print(p.is_birthday())