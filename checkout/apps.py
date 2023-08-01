from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # From Code Institue's "Boutique Ado" Walkthrough Project
    def ready(self):
        import checkout.signals
