from django.apps import AppConfig


class UsersConfig(AppConfig):
    # klasa potrzebana do zarejestrowania aplikacji w settings.py
    name = 'users'

    def ready(self):
        """Metoda pomocnicza w automatycznym tworzeniu profilu użytkownika po rejestracji.
        """
        import users.signals