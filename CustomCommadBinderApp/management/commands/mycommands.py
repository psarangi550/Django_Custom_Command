from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    help="This is Just a normal Simple Commad Args"
    def add_arguments(self,parser):
        parser.add_argument("num1", help="Please Provide Valide Number Between 1 to 100" ,type=int)
        parser.add_argument("chars", nargs=3, help="Please Provide the 3 String to iterate over")
        parser.add_argument("--options",help="THis is a Optiona String Paraameter",type=str,default="default")
        parser.add_argument("--options2", action="store_true")
        
        
    def handle(self,*args,**kwargs):
        # print("Command : My Command")
        if kwargs['num1']<100:
            self.stdout.write(self.style.SUCCESS('You Provided Value between 100'))
        else:
            raise CommandError('Please Provide Number below 100')
        
        # for value in  kwargs['chars']:
        #     self.stdout.write(self.style.WARNING(f'{value}'))
        
        if kwargs['options2']:
            self.stdout.write(self.style.WARNING("You Provided True Value"))
        else:
            self.stderr.write(self.style.ERROR("you Provided False Value"))
            
            