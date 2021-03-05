from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
import os
from kivy.uix.popup import Popup
from connected import Connected

class MessageBox(Popup):
    def openPopup(self,TextMessage):
        message = MessageBox()
        message.messageForText.text = TextMessage
        message.open()

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
       
  

    def convert_calvariables(self):
        message = MessageBox()
        if len(self.ids['password'].text) == 0:   # if text is not empty
            message.openPopup('Enter password')
        if len(self.ids['login'].text) == 0:   # if text is not empty
            message.openPopup('Enter login')
 
    

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )
        
    def check(self):
        var = self.app.password.get()
        if var == '':
            print ("The value is not valid")
        else:
            print ("The value is valid")

if __name__ == '__main__':
    LoginApp().run()
