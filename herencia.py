#This is a book system to barber Shop


class Book:
    def __init__(self,name,date,hour):
        self.name = name
        self.date = date
        self.hour = hour


    def book_confirmed(self):
        print(f"Book confirmed to: {self.name}, the {self.date} to {self.hour}")

class BookToCut(Book):
    def __init__ (self,name,date, hour,style):
        super().__init__(name,date, hour)
        self.style = style
        

    def details(self):
        print(f"Cut booked to {self.name} with style {self.style}")


class BookFreshFace(Book):
    def __init__(self, name, date, hour, treatment):
        super().__init__(name, date, hour)
        self.treatment = treatment


    def details(self):
        print(f"Face treatment booked for {self.name}")


cut= BookToCut("Jeff", "15/05/2025", "4:00pm", "Fade")
cut.book_confirmed()
cut.details()

print()

face=BookFreshFace("Jeff", "15/05/2025", "4:00pm", "Face VIP")
face.book_confirmed()
face.details()