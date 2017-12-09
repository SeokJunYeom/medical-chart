from tkinter import *
from decimal import Decimal

from subframe import PatientFrame, ChartFrame
from structure import Patient, Chart


class MainFrame:

    def __init__(self):
        self.top = Tk()
        self.top.title('의료정보학 8조')
        self.top.geometry('950x500+0+0')
        self.top.resizable(0, 0)

        self.data_tree = [{
            'patient': Patient(),
            'chart': [Chart()] * 10,
        }] * 10

        self.patient_pointer = 0
        self.chart_pointer = 0

        self.patient_buttons = list()

        for i in range(10):
            relx = float(Decimal('0.01') + Decimal(i)/Decimal('10.2'))

            patient = Button(self.top)
            patient.place(relx=relx, rely=0.02, height=44, width=91)
            patient.configure(text=('환자' + str(i + 1)))
            patient.configure(background='#4eaf69')
            patient.configure(activebackground='#4eaf69')
            patient.configure(command=self.select_button(outer=self, data='patient', index=i))

            self.patient_buttons.append(patient)

        self.search_entry = Entry(self.top)
        self.search_entry.place(x=12, y=80, height=27, width=224)
        self.search_entry.configure(background='#bdbdbd')
        self.search_entry.configure(width=224)

        self.search_button = Button(self.top)
        self.search_button.place(relx=0.26, rely=0.155, height=28, width=56)
        self.search_button.configure(background='#4eaf69')
        self.search_button.configure(activebackground='#d9d9d9')
        self.search_button.configure(text='검색')
        self.search_button.configure(command=self.search_patient)

        self.chart_buttons = list()

        for i in range(10):
            rely = float(Decimal('0.48') + Decimal(i)*Decimal('0.05'))

            chart = Button(self.top)
            chart.place(relx=0.41, rely=rely, height=24, width=67)
            chart.configure(text=('내원일' + str(i + 1)))
            chart.configure(background='#4eaf69')
            chart.configure(activebackground='#4eaf69')
            chart.configure(command=self.select_button(outer=self, data='chart', index=i))

            self.chart_buttons.append(chart)

        self.patient = PatientFrame(Frame(self.top))
        self.chart = ChartFrame(Frame(self.top))

        self.patient_submit_button = Button(self.top)
        self.patient_submit_button.place(relx=0.907, rely=0.36, height=34, width=47)
        self.patient_submit_button.configure(activebackground='#d5d5d5')
        self.patient_submit_button.configure(background='#d5d5d5')
        self.patient_submit_button.configure(text='등록')
        self.patient_submit_button.configure(command=self.submit_patient)

        self.chart_submit_button = Button(self.top)
        self.chart_submit_button.place(relx=0.907, rely=0.87, height=34, width=47)
        self.chart_submit_button.configure(activebackground='#d5d5d5')
        self.chart_submit_button.configure(background='#d5d5d5')
        self.chart_submit_button.configure(text='등록')
        self.chart_submit_button.configure(command=self.submit_chart)

    def start(self):
        self.top.mainloop()

    class select_button:

        def __init__(self, outer, data, index):
            self.outer = outer
            self.data = data
            self.index = index
            self.data_tree = self.outer.data_tree

        def __call__(self):

            if self.data == 'patient':
                data = self.data_tree[self.index]
                patient = data['patient'].serialize()
                first_chart = data['chart'][0].serialize()
                self.outer.patient.set_contents(**patient)
                self.outer.chart.set_contents(**first_chart)
                self.outer.patient_pointer = self.index

            elif self.data == 'chart':
                chart = self.data_tree[self.outer.patient_pointer]['chart'][self.index].serialize()
                self.outer.chart.set_contents(**chart)
                self.outer.chart_pointer = self.index

    def submit_patient(self):
        self.data_tree[self.patient_pointer] = {
            'patient': Patient(**self.patient.get_contents()),
            'chart': [Chart()] * 10,
        }

    def submit_chart(self):
        self.data_tree[self.patient_pointer]['chart'][self.chart_pointer] = Chart(**self.chart.get_contents())

    def search_patient(self):
        name = self.search_entry.get()

        for index, data in enumerate(self.data_tree):

            if name == data['patient'].name:
                self.patient_pointer = index
                self.chart_pointer = 0
                data = self.data_tree[self.patient_pointer]
                self.patient.set_contents(**data['patient'].serialize())
                self.chart.set_contents(**data['chart'][self.chart_pointer].serialize())

                break

if __name__ == '__main__':
    main_frame = MainFrame()
    main_frame.start()
