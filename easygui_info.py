#Enter parts of your address and display the whole thing 
import easygui
name=easygui.enterbox("What's your name?")
addr=easygui.enterbox("Where is your street address?")
city=easygui.enterbox("What is your city?")
state=easygui.enterbox("What is your state or province?")
code=easygui.enterbox("What's your postal code or zip code?")
whole_addr=name+"\n"+addr+"\n"+city+","+state+"\n"+code
easygui.msgbox(whole_addr,"Here is your address:")
