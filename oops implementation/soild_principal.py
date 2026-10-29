#1single responsbillity principle:(SRP):
#one class should have one main responsibility
class student:
    def __init__(self,name):
        self.name=name          

class report:
    def report(self,student):
        print("student name:", student.name)  


student=student("ravi")
student_report=report()             
student_report.report(student)


#2open and close principle:(OCP):
#Open for extension, closed for modification.
class payment:
    def pay(self,amount):
        raise NotImplementedError("Subclasses must implement this method")


class cash_payment(payment):
    def pay(self, amount):
        print("Paid in cash:", amount)

class upl_payment(payment):
    def pay(self, amount):
        print("Paid via UPI:", amount)

cash_payment().pay(1000)
upl_payment().pay(2000)


#3liskov substitution principle:(LSP):
#Subclasses should work wherever the parent class is expected.
class animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class dog(animal):
    def make_sound(self):
        print("Dog is barking")


class cat(animal):
    def make_sound(self):
        print("cat is meowing")


dog=dog()
cat=cat()                
dog.make_sound()
cat.make_sound()


#4interface segregation principle:(ISP):
#Classes should not be forced to use methods they don't need

class printer:
    def print_document(self,document):
        print("prining document:",document)


class scanner:
    def scan_document(self,document):
        print("scanning document:",document)



printer=printer()
scanner=scanner()      


printer.print_document("Report.pdf")
scanner.scan_document("Image.jpg")

#5dependency inversion principle:(DIP):
#high-level classes should depend on abstractions:

class mail_service:
    def send_email(self, message):
        print("Sending message:", message)




class notification:
    def __init__(self,service):
        self.service = service


    def notify(self,message):
        self.service.send(message)




mail = mail_service()
notification = notification()     
notification.notify("welcome to python!")       