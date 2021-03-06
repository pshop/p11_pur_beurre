from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label="Entrez un nom d'utilisateur")
    email = forms.EmailField(label="Entrez votre adresse mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password_check = forms.CharField(label="Entrez à nouveau votre mot de passe", widget=forms.PasswordInput)


class LoginForm(forms.Form):
    email = forms.CharField(max_length=150, label="Entrez votre adresse mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class PasswordResetForm(forms.Form):
    email = forms.CharField(max_length=150, label="Email")


class NewPasswordForm(forms.Form):
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password_check = forms.CharField(label="Entrez à nouveau votre mot de passe", widget=forms.PasswordInput)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="Entrez votre ancien mot de passe", widget=forms.PasswordInput)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password_check = forms.CharField(label="Entrez à nouveau votre mot de passe", widget=forms.PasswordInput)
