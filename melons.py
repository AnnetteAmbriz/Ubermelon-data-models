"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty, country_code="USA"):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

        if country_code == "USA":
            self.order_type = "domestic"
        else:
            self.order_type = "international"

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        country_code = raw_input("What country are you shipping to? > ")
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)
        self.tax = 0.17

    def get_total(self):
        """Calls super get_total, adds $3 if quantity is less than 10"""
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """Initialize goverment melon order, which has no tax. """

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
