# Code snippet from Code Institute Boutique Ado project

from django.http import HttpResponse

class StripeWH_Handler:
    """
    Handler for Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handler for webhook events
        """

        return HttpResponse(
            content = f'Unhandled webhook received: {event["type"]}',
            status = 200,
        )
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handler for successful paymentIntent webhook
        """

        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200,
        )
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handler for unsuccessful paymentIntent webhook
        """

        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200,
        )