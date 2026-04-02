import logging

class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount, currency):
        try:
            payment_result = self.payment_gateway.process_payment(amount, currency)
            logging.info(f'Payment processed successfully: {payment_result}')
            return payment_result
        except Exception as e:
            logging.error(f'Payment processing error: {str(e)}')
            raise

class PaymentGateway:
    def process_payment(self, amount, currency):
        # Simulate a payment processing operation
        # In a real-world scenario, this would be replaced with actual payment gateway code
        if amount < 0.0:
            raise ValueError('Invalid amount')
        if currency not in ['USD', 'EUR', 'GBP']:
            raise ValueError('Invalid currency')
        return f'Payment successful for {amount} {currency}'

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Create a payment gateway instance
    payment_gateway = PaymentGateway()

    # Create a payment processor instance
    payment_processor = PaymentProcessor(payment_gateway)

    # Process a payment
    try:
        payment_result = payment_processor.process_payment(10.0, 'USD')
        print(payment_result)
    except ValueError as e:
        print(str(e))