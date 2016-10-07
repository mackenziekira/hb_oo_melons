"""This file should have our order classes in it."""

from random import randint

class AbstractMelonOrder(object):

    def __init__(self, species, qty, tax=0.0, order_type=None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


    def get_base_price(self):
        """Returns a random base price from 5 to 9. """

        return randint(5,9)


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "Christmas melon":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder,self).__init__(species, qty, 0.08, "domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder,self).__init__(species, qty, 0.17, 'international')
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    "A government melon order"

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder,self).__init__(species, qty)
        self.passed_inspection = False


    def mark_inspection(self, passed):
        """Marks melon as passed if user enters True."""

        if passed:
            self.passed_inspection = True

