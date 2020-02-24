class Default(object):

    def calculate_default(order):
        return order.value * 0.05


class Express(object):

    def calculate_express(order):
        return order.value * 0.1
