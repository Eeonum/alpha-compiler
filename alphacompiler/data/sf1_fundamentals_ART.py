# Code to assist loading fundamentals data from Quandl/SF1 by sherrytp
# https://www.quandl.com/data/SF1-Core-US-Fundamentals-Data/
# requires Python Quandl package and Quandl API key to be set as an ENV variable QUANDL_API_KEY.

from alphacompiler.util.sparse_data import SparseDataFactor
from alphacompiler.util.zipline_data_tools import get_ticker_sid_dict_from_bundle
from zipline.utils.paths import zipline_root


# TODO Separate ART and ARQ
# this code should go with your application code.
class FundamentalsART(SparseDataFactor):
    window_safe = True
    # fields = ['reportperiod', 'marketcap', 'evebit', 'roa', 'assets', 'ncfo', 'de',
    #           'currentratio', 'shareswa', 'grossmargin', 'assetturnover']
    fields = ['reportperiod', 'marketcap', 'evebit', 'roa', 'assets', 'de',
              'currentratio', 'shareswa', 'grossmargin', 'assetturnover',  # QuantRocket
              'netmargin',  # Warren Buffet: profit margin
              'epsdil',  # Steven
              'ps1',
              'divyield',
              'fcf',  # free cash flow
              'fcfps',
              'ncfo',  # Operating cash flow
              'pb',  # price to book value
              'ev',  # enterprise value
              'ebitda'
              ]
    dimensions = ['ART'] * len(fields)
    outputs = ['{}_{}'.format(i, j) for i, j in zip(fields, dimensions)]

    def __init__(self, *args, **kwargs):
        super(FundamentalsART, self).__init__(*args, **kwargs)
        self.N = len(get_ticker_sid_dict_from_bundle("sep")) + 1  # max(sid)+1 get this from the bundle

        self.data_path = zipline_root() + '/data/SF1_basic_fundamentals_trading_ART.npy'
