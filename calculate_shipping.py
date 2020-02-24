class CalculateShipping(object):

    def execute_calculation(self, order):
        total = order.value * 0.05
        print(total)