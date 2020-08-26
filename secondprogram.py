# BME 547 Class 8/26/20
#print("The name of the secondprogram module is {}".format(__name__))
#import calculator as calc
from calculator import HDL_driver as driver
# No parenthese in import, you don't want to run the func
# Python will run interface because of the import statement
driver()
