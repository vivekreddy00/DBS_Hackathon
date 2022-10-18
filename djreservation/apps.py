from django.apps import AppConfig


class ReservationConfig(AppConfig):
    name='reservation'
    default_auto_field = 'django.db.models.BigAutoField'
    
    def ready(self):
        import djreservation.signals
        AppConfig.ready(self)
