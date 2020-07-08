"""
Program: invoice.py
Author: Ryan Elliott
Last date modified: 07/7/2020
Invoice Class with Driver and imported Customer Class
"""
from class_definitions.customer import Customer


class Invoice:
    """Invoice Class """

    def __init__(self, invoid, cust='', iwp=dict()):
        """Invoice constructor"""
        # exception should be raised in the constructor, because the object should not be made if it has an incorrect data type
        try:
            if not isinstance(invoid, int):
                raise AttributeError
        except AttributeError:
            raise AttributeError
            print("'Invoice' object has no attribute 'cid'")
        self._invoice_id = invoid
        self._customer = cust
        self._items_with_price = iwp

    def add_item(self, dictadd):
        """Add item to dictionary
        :param dictadd, dictionary item to add
        """
        self._items_with_price.update(dictadd)

    def create_invoice(self):
        """Creates invoice with prices, tax and total
        """
        total = 0
        for x in self._items_with_price:
            print(str(x))
        for x in self._items_with_price.values():
            print("$"+str(x))
            total += x
        tax = total * 0.06
        print("Tax "+"$"+str(round(tax,2)))
        total += tax
        print("Total "+"$"+str(round(total,2)))

    def __str__(self):
        """str override"""
        return "invoice id " + str(self._invoice_id) + " " + str(self._customer.__str__())

    def __repr__(self):
        """repr override"""
        return "invoice id " + str(self._invoice_id) + " " + str(self._customer.__repr__())


# Driver
if __name__ == '__main__':
    captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
    invoice = Invoice(1, captain_mal)
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
    print(str(invoice))
    print(repr(invoice))
