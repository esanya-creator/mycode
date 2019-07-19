import pytest
from common.helpers.base import CurrencyConvert
class TestCurrencyConverter(object):
    currency_base=CurrencyConvert()

    def test_Currency_Converter(self):
        list_country=self.currency_base.get_countryfrom_list()
        for i in list_country:
            response=self.currency_base.get_currency_convert(i)
            currency=self.currency_base.get_currency(response)
            print("The converted currency from "+i+" to INR is:", currency)


