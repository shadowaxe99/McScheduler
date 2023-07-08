class FoodOrderingIntegration:
    def __init__(self):
        self.delivery_platforms = ['DoorDash', 'GoPuff']

    def order_food(self, delivery_platform, meal):
        if delivery_platform not in self.delivery_platforms:
            raise ValueError(f'Unsupported delivery platform: {delivery_platform}')
        # TODO: Implement food ordering from DoorDash and GoPuff
        pass