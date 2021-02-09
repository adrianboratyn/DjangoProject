from django.apps import AppConfig


#clasa potrzebana do zarejestrowania aplikacji w settings.py
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """Metoda pomocnicza w automatycznym tworzeniu profilu użytkownika po rejestracji.
        """
        import users.signals