class Patient:

    def __init__(self, name='', age='', sex='', address='', contact=''):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address
        self.contact = contact

    def serialize(self):

        return {
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'address': self.address,
            'contact': self.contact
        }

class Chart:

    def __init__(self, num='', date='', symptom='', evaluation='', diagnosis='', plan=''):
        self.num = num
        self.date = date
        self.symptom = symptom
        self.evaluation = evaluation
        self.diagnosis = diagnosis
        self.plan = plan

    def serialize(self):

        return {
            'num': self.num,
            'date': self.date,
            'symptom': self.symptom,
            'evaluation': self.evaluation,
            'diagnosis': self.diagnosis,
            'plan': self.plan
        }