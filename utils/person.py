class Person:
   def __init__(self, person_name, phone_number, item):
      self.person_name = person_name
      self.phone_number = phone_number
      self.item = item


# to replace class Person once function next_step is done
class New_Person:
   person_name = None
   phone_number = None
   item = None

   def __init__(self, person_name, phone_number, item):
      self.person_name = person_name
      self.phone_number = phone_number
      self.item = item