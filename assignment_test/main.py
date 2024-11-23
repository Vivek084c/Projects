from reportlab.pdfgen import canvas 

class pdfgenerator:
    def __init__(self,filename, cpname, email, contact,itemlist):
        self.filename  =filename
        self.cpname = cpname
        self.email  =email
        self.contact = contact
        self.itemlist=  itemlist

    def generate_data(self):
        pdf =         

