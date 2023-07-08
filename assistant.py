from deal_negotiation import DealNegotiation

class Assistant:
    def __init__(self):
        self.deal_negotiation = DealNegotiation()

    def handle_task(self, task):
        if 'negotiate' in task:
            return self.deal_negotiation.negotiate(task)
        # TODO: Handle other tasks
        pass