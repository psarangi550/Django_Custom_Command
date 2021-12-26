from django.core.management.base import BaseCommand
from CustomCommadBinderApp.models import Employee

class Command(BaseCommand):
    help = 'This Command Will help in adding the Employee Model Object from the Custom Command'
    def add_arguments(self, parser):
        parser.add_argument("num", help="Enter Integer Number",type=int)
        parser.add_argument("name", help="Enter String Name", type=str)
        parser.add_argument("dept", choices=["EM","MG"],help="Enter The Deptarment as EM for Employee or MG for Manager")
        parser.add_argument("--option",action="store_true",help="Provide if you want to see the Employee Active")
    
    def handle(self,*args, **kwargs):
      
        emp=Employee.objects.create(
            eno=kwargs.get("num"),
            ename=kwargs.get("name"),
            edept=kwargs.get("dept"),
            eactive=kwargs.get("option")
            )
        # emp.save()
        self.stdout.write(self.style.SUCCESS("Employee Addedd Successfully"))
