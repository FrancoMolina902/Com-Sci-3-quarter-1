
class Patient:

  def __init__(self, name, bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

  def get_bill_amount(self):
    return self.__bill_amount

  def set_bill_amount(self, bill_amount):
    self.__bill_amount = bill_amount

  def calculate_bill(self):
    return self.__bill_amount


class PhilHealthPatient(Patient):

  def calculate_bill(self):
    return self.get_bill_amount() * (1 - 0.20)


class SeniorPatient(Patient):

  def calculate_bill(self):
    return self.get_bill_amount() * (1 - 0.15)


def main():
  print("Hospital Billing System")
  print("---------------------------------")
  regular_patient = Patient("Juan Dela Cruz", 15000)
  philhealth_patient = PhilHealthPatient("Maria Santos", 15000)
  senior_patient = SeniorPatient("Pedro Reyes", 15000)

  patients = [regular_patient, philhealth_patient, senior_patient]

  
  for p in patients:
    print(f"Patient Name:  {p.get_name()}")
    print(f"Original Bill: ₱{p.get_bill_amount():,.2f}")
    print(f"Final Bill:    ₱{p.calculate_bill():,.2f}\n")


if __name__ == "__main__":
  main()
