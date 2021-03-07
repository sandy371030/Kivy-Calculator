import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window


Window.size=(500,700)

Builder.load_file("calculator.kv")
 

class MyLayout(Widget):
    
    def click (self,button):

        #getting data from text box
        prev=self.ids.calc_inp.text
        if prev=="Error":
            prev=""
        if (prev=="0"):
            self.ids.calc_inp.text=f"{button}"  
        else:
            self.ids.calc_inp.text=f"{prev}{button}"
    
    def equal(self):
        prev=self.ids.calc_inp.text
        try:

            ans=eval(prev) 
            self.ids.calc_inp.text=str(ans)
        except:
            self.ids.calc_inp.text="Error"

    def pos_neg(self):
        prev=self.ids.calc_inp.text
        if "-" in prev:
            self.ids.calc_inp.text= f'{prev.replace("-"," ")}'
        else:
            self.ids.calc_inp.text="-"+prev

    def remove(self):
        prev=self.ids.calc_inp.text
        self.ids.calc_inp.text=prev[:-1]

    def math_sign(self,sign):
        prev=self.ids.calc_inp.text
        self.ids.calc_inp.text=f"{prev}{sign}"
  
    def dot(self): 
        prev=self.ids.calc_inp.text
        numlist=prev.split("+")

        if "+" in prev and "." not in numlist[-1]:
            self.ids.calc_inp.text=f'{prev}.'
        elif "." in prev:
            pass
        else:
            self.ids.calc_inp.text=f'{prev}.'

    def clear(self):
        self.ids.calc_inp.text="0"

   
class CalculatorApp(App):
    def build(self):
        return MyLayout()  



# runs only when this is the main file
if __name__== "__main__" :
    CalculatorApp().run()        