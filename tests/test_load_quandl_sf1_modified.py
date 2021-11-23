# Created by Eonum, Inc

import unittest
import os
from alphacompiler.data.load_quandl_sf1 import populate_raw_data_from_dump

from alphacompiler.util.zipline_data_tools import get_ticker_sid_dict_from_bundle


class Test_Populate_From_Dump(unittest.TestCase):
    def test_reads_file(self):
        # bundle_name = 'sharadar-eqfd'
        bundle_name = 'sep'
        tickers = get_ticker_sid_dict_from_bundle(bundle_name)
        self.assertTrue(len(tickers) > 0)  # test the bundle is not empty

        BASE = os.path.dirname(os.path.realpath(__file__))
        RAW_FLDR = "raw"  # folder to store the raw text file

        # fields = ['netinc', 'equity', 'bvps', 'sps', 'fcfps', 'price']  # basic QV
        fields0 = ['accoci', 'assets', 'assetsavg', 'assetsc', 'assetsnc', 'assetturnover', 'bvps', 'capex',
                   'cashneq', 'cashnequsd', 'cor', 'consolinc', 'currentratio', 'de', 'debt', 'debtc',
                   'debtnc', 'debtusd', 'deferredrev', 'depamor', 'deposits', 'divyield', 'dps', 'ebit',
                   'ebitda', 'ebitdamargin', 'ebitdausd', 'ebitusd', 'ebt', 'eps', 'epsdil', 'epsusd',
                   'equity', 'equityavg', 'equityusd', 'ev', 'evebit', 'evebitda', 'fcf', 'fcfps',
                   'fxusd', 'gp', 'grossmargin', 'intangibles', 'intexp', 'invcap', 'invcapavg', 'inventory',
                   'investments', 'investmentsc', 'investmentsnc', 'liabilities', 'liabilitiesc', 'liabilitiesnc',
                   'marketcap', 'ncf', 'ncfbus', 'ncfcommon', 'ncfdebt', 'ncfdiv', 'ncff', 'ncfi', 'ncfinv',
                   'ncfo', 'ncfx', 'netinc', 'netinccmn', 'netinccmnusd', 'netincdis', 'netincnci',
                   'netmargin', 'opex', 'opinc', 'payables', 'payoutratio', 'pb', 'pe', 'pe1', 'ppnenet',
                   'prefdivis', 'price', 'ps', 'ps1', 'receivables', 'retearn', 'revenue', 'revenueusd',
                   'rnd', 'roa', 'roe', 'roic', 'ros', 'sbcomp', 'sgna', 'sharefactor', 'sharesbas',
                   'shareswa', 'shareswadil', 'sps', 'tangibles', 'taxassets', 'taxexp', 'taxliabilities',
                   'tbvps', 'workingcapital']
        fields1 = ['accoci', 'assets', 'assetsavg', 'assetsc', 'assetsnc', 'assetturnover', 'bvps', 'capex',
                   'cashneq', 'cashnequsd', 'cor', 'consolinc', 'currentratio', 'de', 'debt', 'debtc',
                   'debtnc', 'debtusd', 'deferredrev', 'depamor', 'deposits', 'divyield', 'dps', 'ebit',
                   'ebitda', 'ebitdamargin', 'ebitdausd', 'ebitusd', 'ebt', 'eps', 'epsdil', 'epsusd',
                   'equity', 'equityavg', 'equityusd', 'ev', 'evebit', 'evebitda', 'fcf', 'fcfps',
                   'fxusd', 'gp', 'grossmargin', 'intangibles', 'intexp', 'invcap', 'invcapavg', 'inventory',
                   'investments', 'investmentsc', 'investmentsnc', 'liabilities', 'liabilitiesc', 'liabilitiesnc',
                   'marketcap', 'ncf', 'ncfbus', 'ncfcommon', 'ncfdebt', 'ncfdiv', 'ncff', 'ncfi', 'ncfinv',
                   'ncfo', 'ncfx', 'netinc', 'netinccmn', 'netinccmnusd', 'netincdis', 'netincnci',
                   'netmargin', 'opex', 'opinc', 'payables', 'payoutratio', 'pb', 'pe', 'pe1', 'ppnenet',
                   'prefdivis', 'price', 'ps', 'ps1', 'receivables', 'retearn', 'revenue', 'revenueusd',
                   'rnd', 'roa', 'roe', 'roic', 'ros', 'sbcomp', 'sgna', 'sharefactor', 'sharesbas',
                   'shareswa', 'shareswadil', 'sps', 'tangibles', 'taxassets', 'taxexp', 'taxliabilities',
                   'tbvps', 'workingcapital']
        fields2 = ['accoci', 'assets', 'assetsavg', 'assetsc', 'assetsnc', 'assetturnover', 'bvps', 'capex',
                   'cashneq', 'cashnequsd', 'cor', 'consolinc', 'currentratio', 'de', 'debt', 'debtc',
                   'debtnc', 'debtusd', 'deferredrev', 'depamor', 'deposits', 'divyield', 'dps', 'ebit',
                   'ebitda', 'ebitdamargin', 'ebitdausd', 'ebitusd', 'ebt', 'eps', 'epsdil', 'epsusd',
                   'equity', 'equityavg', 'equityusd', 'ev', 'evebit', 'evebitda', 'fcf', 'fcfps',
                   'fxusd', 'gp', 'grossmargin', 'intangibles', 'intexp', 'invcap', 'invcapavg', 'inventory',
                   'investments', 'investmentsc', 'investmentsnc', 'liabilities', 'liabilitiesc', 'liabilitiesnc',
                   'marketcap', 'ncf', 'ncfbus', 'ncfcommon', 'ncfdebt', 'ncfdiv', 'ncff', 'ncfi', 'ncfinv',
                   'ncfo', 'ncfx', 'netinc', 'netinccmn', 'netinccmnusd', 'netincdis', 'netincnci',
                   'netmargin', 'opex', 'opinc', 'payables', 'payoutratio', 'pb', 'pe', 'pe1', 'ppnenet',
                   'prefdivis', 'price', 'ps', 'ps1', 'receivables', 'retearn', 'revenue', 'revenueusd',
                   'rnd', 'roa', 'roe', 'roic', 'ros', 'sbcomp', 'sgna', 'sharefactor', 'sharesbas',
                   'shareswa', 'shareswadil', 'sps', 'tangibles', 'taxassets', 'taxexp', 'taxliabilities',
                   'tbvps', 'workingcapital']
        fields3 = ['accoci', 'assets', 'assetsavg', 'assetsc', 'assetsnc', 'assetturnover', 'bvps', 'capex',
                   'cashneq', 'cashnequsd', 'cor', 'consolinc', 'currentratio', 'de', 'debt', 'debtc',
                   'debtnc', 'debtusd', 'deferredrev', 'depamor', 'deposits', 'divyield', 'dps', 'ebit',
                   'ebitda', 'ebitdamargin', 'ebitdausd', 'ebitusd', 'ebt', 'eps', 'epsdil', 'epsusd',
                   'equity', 'equityavg', 'equityusd', 'ev', 'evebit', 'evebitda', 'fcf', 'fcfps',
                   'fxusd', 'gp', 'grossmargin', 'intangibles', 'intexp', 'invcap', 'invcapavg', 'inventory',
                   'investments', 'investmentsc', 'investmentsnc', 'liabilities', 'liabilitiesc', 'liabilitiesnc',
                   'marketcap', 'ncf', 'ncfbus', 'ncfcommon', 'ncfdebt', 'ncfdiv', 'ncff', 'ncfi', 'ncfinv',
                   'ncfo', 'ncfx', 'netinc', 'netinccmn', 'netinccmnusd', 'netincdis', 'netincnci',
                   'netmargin', 'opex', 'opinc', 'payables', 'payoutratio', 'pb', 'pe', 'pe1', 'ppnenet',
                   'prefdivis', 'price', 'ps', 'ps1', 'receivables', 'retearn', 'revenue', 'revenueusd',
                   'rnd', 'roa', 'roe', 'roic', 'ros', 'sbcomp', 'sgna', 'sharefactor', 'sharesbas',
                   'shareswa', 'shareswadil', 'sps', 'tangibles', 'taxassets', 'taxexp', 'taxliabilities',
                   'tbvps', 'workingcapital']
        fields4 = ['accoci', 'assets', 'assetsavg', 'assetsc', 'assetsnc', 'assetturnover', 'bvps', 'capex',
                   'cashneq', 'cashnequsd', 'cor', 'consolinc', 'currentratio', 'de', 'debt', 'debtc',
                   'debtnc', 'debtusd', 'deferredrev', 'depamor', 'deposits', 'divyield', 'dps', 'ebit',
                   'ebitda', 'ebitdamargin', 'ebitdausd', 'ebitusd', 'ebt', 'eps', 'epsdil', 'epsusd',
                   'equity', 'equityavg', 'equityusd', 'ev', 'evebit', 'evebitda', 'fcf', 'fcfps',
                   'fxusd', 'gp', 'grossmargin', 'intangibles', 'intexp', 'invcap', 'invcapavg', 'inventory',
                   'investments', 'investmentsc', 'investmentsnc', 'liabilities', 'liabilitiesc', 'liabilitiesnc',
                   'marketcap', 'ncf', 'ncfbus', 'ncfcommon', 'ncfdebt', 'ncfdiv', 'ncff', 'ncfi', 'ncfinv',
                   'ncfo', 'ncfx', 'netinc', 'netinccmn', 'netinccmnusd', 'netincdis', 'netincnci',
                   'netmargin', 'opex', 'opinc', 'payables', 'payoutratio', 'pb', 'pe', 'pe1', 'ppnenet',
                   'prefdivis', 'price', 'ps', 'ps1', 'receivables', 'retearn', 'revenue', 'revenueusd',
                   'rnd', 'roa', 'roe', 'roic', 'ros', 'sbcomp', 'sgna', 'sharefactor', 'sharesbas',
                   'shareswa', 'shareswadil', 'sps', 'tangibles', 'taxassets', 'taxexp', 'taxliabilities',
                   'tbvps', 'workingcapital']
        fields5 = ['accoci', 'assets', 'assetsavg', 'assetsc', 'assetsnc', 'assetturnover', 'bvps', 'capex',
                   'cashneq', 'cashnequsd', 'cor', 'consolinc', 'currentratio', 'de', 'debt', 'debtc',
                   'debtnc', 'debtusd', 'deferredrev', 'depamor', 'deposits', 'divyield', 'dps', 'ebit',
                   'ebitda', 'ebitdamargin', 'ebitdausd', 'ebitusd', 'ebt', 'eps', 'epsdil', 'epsusd',
                   'equity', 'equityavg', 'equityusd', 'ev', 'evebit', 'evebitda', 'fcf', 'fcfps',
                   'fxusd', 'gp', 'grossmargin', 'intangibles', 'intexp', 'invcap', 'invcapavg', 'inventory',
                   'investments', 'investmentsc', 'investmentsnc', 'liabilities', 'liabilitiesc', 'liabilitiesnc',
                   'marketcap', 'ncf', 'ncfbus', 'ncfcommon', 'ncfdebt', 'ncfdiv', 'ncff', 'ncfi', 'ncfinv',
                   'ncfo', 'ncfx', 'netinc', 'netinccmn', 'netinccmnusd', 'netincdis', 'netincnci',
                   'netmargin', 'opex', 'opinc', 'payables', 'payoutratio', 'pb', 'pe', 'pe1', 'ppnenet',
                   'prefdivis', 'price', 'ps', 'ps1', 'receivables', 'retearn', 'revenue', 'revenueusd',
                   'rnd', 'roa', 'roe', 'roic', 'ros', 'sbcomp', 'sgna', 'sharefactor', 'sharesbas',
                   'shareswa', 'shareswadil', 'sps', 'tangibles', 'taxassets', 'taxexp', 'taxliabilities',
                   'tbvps', 'workingcapital']
        # dims = ['ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ']
        dims0 = ['ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY', 'ARY',
                 'ARY']
        dims1 = ['ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ', 'ARQ',
                 'ARQ']
        dims2 = ['ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART',
                 'ART']
        dims3 = ['MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY', 'MRY',
                 'MRY']
        dims4 = ['MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ', 'MRQ',
                 'MRQ']
        dims5 = ['MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT', 'MRT',
                 'MRT']

        # populate_raw_data_from_dump(tickers, fields, dims, raw_path=os.path.join(BASE, RAW_FLDR))
        populate_raw_data_from_dump(tickers, fields0, dims0, raw_path=os.path.join(BASE, RAW_FLDR))
        populate_raw_data_from_dump(tickers, fields1, dims1, raw_path=os.path.join(BASE, RAW_FLDR))
        populate_raw_data_from_dump(tickers, fields2, dims2, raw_path=os.path.join(BASE, RAW_FLDR))
        populate_raw_data_from_dump(tickers, fields3, dims3, raw_path=os.path.join(BASE, RAW_FLDR))
        populate_raw_data_from_dump(tickers, fields4, dims4, raw_path=os.path.join(BASE, RAW_FLDR))
        populate_raw_data_from_dump(tickers, fields5, dims5, raw_path=os.path.join(BASE, RAW_FLDR))

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
