from shippings import calculate_default, calculate_experss

class CalculateShipping(object):

    def execute_calculation(self, order, shipping):
        if shipping == 'Default':
            total = calculate_default()
        elif shipping == 'Express':
            total = calculate_experss
        print(total)