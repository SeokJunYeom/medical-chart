from tkinter import *


class PatientFrame:

    def __init__(self, frame=None):
        self.frame = frame
        self.frame.place(x=480, y=80, height=145, width=455)

        self.name_label = Label(self.frame)
        self.name_label.place(relx=0.04, y=10, height=17, width=74)
        self.name_label.configure(text='이름')

        self.age_label = Label(self.frame)
        self.age_label.place(relx=0.04, y=37, height=17, width=74)
        self.age_label.configure(text='나이')

        self.sex_label = Label(self.frame)
        self.sex_label.place(relx=0.04, y=64, height=17, width=74)
        self.sex_label.configure(text='성별')

        self.address_label = Label(self.frame)
        self.address_label.place(relx=0.04, y=91, height=17, width=74)
        self.address_label.configure(text='주소')

        self.contact_label = Label(self.frame)
        self.contact_label.place(relx=0.04, y=118, height=17, width=74)
        self.contact_label.configure(text='연락처')

        self.name_entry_text = StringVar()
        self.name_entry = Entry(self.frame, textvariable=self.name_entry_text)
        self.name_entry.place(x=110, y=10, height=17, width=244)
        self.name_entry.configure(background='#bdbdbd')

        self.age_entry_text = StringVar()
        self.age_entry = Entry(self.frame, textvariable=self.age_entry_text)
        self.age_entry.place(x=110, y=37, height=17, width=244)
        self.age_entry.configure(background='#bdbdbd')

        self.sex_entry_text = StringVar()
        self.sex_entry = Entry(self.frame, textvariable=self.sex_entry_text)
        self.sex_entry.place(x=110, y=64, height=17, width=244)
        self.sex_entry.configure(background='#bdbdbd')

        self.address_entry_text = StringVar()
        self.address_entry = Entry(self.frame, textvariable=self.address_entry_text)
        self.address_entry.place(x=110, y=91, height=17, width=244)
        self.address_entry.configure(background='#bdbdbd')

        self.contact_entry_text = StringVar()
        self.contact_entry = Entry(self.frame, textvariable=self.contact_entry_text)
        self.contact_entry.place(x=110, y=118, height=17, width=244)
        self.contact_entry.configure(background='#bdbdbd')

    def get_contents(self):

        return {
            'name': self.name_entry.get(),
            'age': self.age_entry.get(),
            'sex': self.sex_entry.get(),
            'address': self.address_entry.get(),
            'contact': self.contact_entry.get(),
        }

    def set_contents(self, name, age, sex, address, contact):
        self.name_entry_text.set(name)
        self.age_entry_text.set(age)
        self.sex_entry_text.set(sex)
        self.address_entry_text.set(address)
        self.contact_entry_text.set(contact)

class ChartFrame:

    def __init__(self, frame=None):
        self.frame = frame
        self.frame.place(x=480, y=254, height=225, width=455)

        self.num_label = Label(self.frame)
        self.num_label.place(relx=0.02, y=22, height=17, width=74)
        self.num_label.configure(text='차트번호')

        self.date_label = Label(self.frame)
        self.date_label.place(relx=0.02, y=55, height=17, width=74)
        self.date_label.configure(text='내원일')

        self.symptom_label = Label(self.frame)
        self.symptom_label.place(relx=0.02, y=88, height=17, width=74)
        self.symptom_label.configure(text='호소증상')

        self.evaluation_label = Label(self.frame)
        self.evaluation_label.place(relx=0.02, y=121, height=17, width=74)
        self.evaluation_label.configure(text='환자평가')

        self.diagnosis_label = Label(self.frame)
        self.diagnosis_label.place(relx=0.02, y=154, height=17, width=74)
        self.diagnosis_label.configure(text='진단')

        self.plan_label = Label(self.frame)
        self.plan_label.place(relx=0.02, y=187, height=17, width=74)
        self.plan_label.configure(text='치료및계획')

        self.num_entry_text = StringVar()
        self.num_entry = Entry(self.frame, textvariable=self.num_entry_text)
        self.num_entry.place(x=110, y=22, height=17, width=244)
        self.num_entry.configure(background='#bdbdbd')

        self.date_entry_text = StringVar()
        self.date_entry = Entry(self.frame, textvariable=self.date_entry_text)
        self.date_entry.place(x=110, y=55, height=17, width=244)
        self.date_entry.configure(background='#bdbdbd')

        self.symptom_entry_text = StringVar()
        self.symptom_entry = Entry(self.frame, textvariable=self.symptom_entry_text)
        self.symptom_entry.place(x=110, y=88, height=17, width=244)
        self.symptom_entry.configure(background='#bdbdbd')

        self.evaluation_entry_text = StringVar()
        self.evaluation_entry = Entry(self.frame, textvariable=self.evaluation_entry_text)
        self.evaluation_entry.place(x=110, y=121, height=17, width=244)
        self.evaluation_entry.configure(background='#bdbdbd')

        self.diagnosis_entry_text = StringVar()
        self.diagnosis_entry = Entry(self.frame, textvariable=self.diagnosis_entry_text)
        self.diagnosis_entry.place(x=110, y=154, height=17, width=244)
        self.diagnosis_entry.configure(background='#bdbdbd')

        self.plan_entry_text = StringVar()
        self.plan_entry = Entry(self.frame, textvariable=self.plan_entry_text)
        self.plan_entry.place(x=110, y=187, height=17, width=244)
        self.plan_entry.configure(background='#bdbdbd')

    def get_contents(self):

        return {
            'num': self.num_entry.get(),
            'date': self.date_entry.get(),
            'symptom': self.symptom_entry.get(),
            'evaluation': self.evaluation_entry.get(),
            'diagnosis': self.diagnosis_entry.get(),
            'plan': self.plan_entry.get(),
        }

    def set_contents(self, num, date, symptom, evaluation, diagnosis, plan):
        self.num_entry_text.set(num)
        self.date_entry_text.set(date)
        self.symptom_entry_text.set(symptom)
        self.evaluation_entry_text.set(evaluation)
        self.diagnosis_entry_text.set(diagnosis)
        self.plan_entry_text.set(plan)
