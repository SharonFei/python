#Easygui version of temperature-conversion program
#converts Fahrenheit to Celsius
import easygui
easygui.msgbox("This program converts Fahrenheit to Celsius")
temperature=easygui.enterbox('Type in a temperature in Fahrenheit:')
fahrenheit=float(temperature)
celeius=5.0/9*(fahrenheit - 32)
easygui.msgbox('That is '+str(celeius)+' degree Celsius')
