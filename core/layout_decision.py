""" # Decide where to divert the flow.
   Designed By : ANKESH"""

from Guis import signin_layout,create_account_layout,forgot_password_layout
def create_lay(self, title1):
    if title1 == "Create Account":
        #Diverted the flow towards create account window
        create_account_layout.create_ac(self,title1)
    elif title1 == "SignIn":
        # Diverted the flow towards Signin window
        signin_layout.signin(self, title1)
    elif title1 == "Forgot Password":
        # Diverted the flow towards Reset Password window
        forgot_password_layout.forgot_lay(self,title1)
