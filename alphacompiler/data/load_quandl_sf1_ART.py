# Code to load raw_ART data from Quandl/SF1 by sherrytp
# https://www.quandl.com/data/SF1-Core-US-Fundamentals-Data/
# requires the python Quandl package, and the 
# Quandl API key to be set as an ENV variable QUANDL_API_KEY.

import quandl
from alphacompiler.util.zipline_data_tools import get_ticker_sid_dict_from_bundle
from alphacompiler.util.sparse_data import pack_sparse_data
from alphacompiler.util import quandl_tools
import alphacompiler.util.load_extensions  # this simply loads the extensions
from zipline.utils.paths import zipline_root
from logbook import Logger
import datetime
import os
import glob
import pandas as pd

BASE = os.path.dirname(os.path.realpath(__file__))
DS_NAME = 'SHARADAR/SF1'  # quandl DataSet code
RAW_FLDR = "raw_ART"  # folder to store the raw_ART text file
START_DATE = '2009-01-01'  # this is only used for getting data from the API
END_DATE = datetime.datetime.today().strftime('%Y-%m-%d')
ZIPLINE_DATA_DIR = zipline_root() + '/data/'
FN = "SF1_basic_fundamentals_trading_ART.npy"  # the file name to be used when storing this in ~/.zipline/data
DUMP_FILE = '~/.zipline/data-for-alpha-compiler/SHARADAR_SF1_017f04a0d2ef7cc409f920be72167ada.csv'
log = Logger('load_quandl_sf1_ART.py')


def clear_raw_folder(raw_folder_path):
    # removes all the files in the raw_ART folder
    print('   **   clearing the raw_ART/ folder   **')
    files = glob.glob(raw_folder_path + '/*')
    for f in files:
        os.remove(f)


def populate_raw_data_from_dump(tickers2sid, fields, dimensions, raw_path):
    """
    Populates the raw_ART/ folder based on a single dump download.

    :param tickers2sid: a dict with the ticker string as the key and the SID
    as the value
    :param fields: a list of field names
    :param dimensions: a list with dimensions for each field in fields
    :param raw_path: the path to the folder to write the files.
    """
    assert len(fields) == len(dimensions)

    df = pd.read_csv(DUMP_FILE)  # open dump file

    clear_raw_folder(RAW_FLDR)

    df = df[['ticker', 'dimension', 'datekey'] + fields]  # remove columns not in fields
    df = df.loc[:, ~df.columns.duplicated()]  # drop any columns with redundant names

    for tkr, df_tkr in df.groupby('ticker'):
        print('processing: ', tkr)

        sid = tickers2sid.get(tkr)
        if sid is None:
            print('no sid found for: {}'.format(tkr))
            continue
        print('sid: {}'.format(sid))

        df_tkr = df_tkr.rename(columns={'datekey': 'Date'}).set_index('Date')

        # loop over the fields and dimensions
        series = []
        for i, field in enumerate(fields):
            print(i, field)
            s = df_tkr[df_tkr.dimension == dimensions[i]][field]
            new_name = '{}_{}'.format(field, dimensions[i])
            s = s.rename(new_name)
            series.append(s)
        df_tkr = pd.concat(series, axis=1)
        df_tkr.index.names = ['Date']  # ensure that the index is named Date
        print("AFTER reorganizing")
        print(df_tkr)

        # write raw_ART file: raw_ART/
        df_tkr.to_csv(os.path.join(raw_path, "{}.csv".format(sid)))


def populate_raw_data_from_api(tickers, fields, dimensions, raw_path):
    """tickers is a dict with the ticker string as the key and the SID
    as the value.
    For each field a dimension is required, so dimensions should be a list
    of dimensions for each field.
    """
    assert len(fields) == len(dimensions)
    quandl_tools.set_api_key()

    # existing = listdir(RAW_FLDR)

    for ticker, sid in tickers.items():
        # if "%d.csv" % sid in existing:
        #     continue
        try:
            query_str = "%s %s" % (DS_NAME, ticker)
            print("fetching data for: {}".format(query_str))

            # df = quandl.get_table(query_str, start_date=START_DATE, end_date=END_DATE)
            df = quandl.get_table(DS_NAME,
                                  calendardate={'gte': START_DATE, 'lte': END_DATE},
                                  ticker=ticker,
                                  qopts={'columns': ['dimension', 'datekey'] + fields})
            df = df.rename(columns={'datekey': 'Date'}).set_index('Date')

            # loop over the fields and dimensions
            series = []
            for i, field in enumerate(fields):
                s = df[df.dimension == dimensions[i]][field]
                series.append(s)
            df = pd.concat(series, axis=1)
            print(df)

            # write raw_ART file: raw_ART/
            df.to_csv(os.path.join(raw_path, "{}.csv".format(sid)))
        except quandl.errors.quandl_error.NotFoundError:
            print("error with ticker: {}".format(ticker))


def populate_raw_data_aqr(tickers, fields, raw_path):
    """tickers is a dict with the ticker string as the key and the SID
    as the value.
    Assumes that all fields desired are AQR.
    """
    quandl_tools.set_api_key()

    # existing = listdir(RAW_FLDR)

    for ticker, sid in tickers.items():
        # if "%d.csv" % sid in existing:
        #     continue
        try:
            query_str = "%s %s" % (DS_NAME, ticker)
            print("fetching data for: {}".format(query_str))

            # df = quandl.get_table(query_str, start_date=START_DATE, end_date=END_DATE)
            df = quandl.get_table(DS_NAME,
                                  calendardate={'gte': START_DATE, 'lte': END_DATE},
                                  ticker=ticker,
                                  qopts={'columns': ['dimension', 'datekey'] + fields})
            print(df)
            df = df[df.dimension == "ARQ"]  # only use As-Reported numbers

            #  Change column name to field
            df = df.rename(columns={"datekey": "Date"})
            df = df.drop(["dimension"], axis=1)

            # write raw_ART file: raw_ART/
            df.to_csv(os.path.join(raw_path, "{}.csv".format(sid)))
        except quandl.errors.quandl_error.NotFoundError:
            print("error with ticker: {}".format(ticker))


def demo():  # demo works on free data
    tickers = {"WMT": 3173, "HD": 2912, "DOGGY": 69, "CSCO": 2809}
    fields = ["GP", "CAPEX", "EBIT", "ASSETS"]
    populate_raw_data_from_api(tickers, fields, os.path.join(BASE, RAW_FLDR))


def all_tickers_for_bundle_from_api(fields, dims, bundle_name, raw_path=os.path.join(BASE, RAW_FLDR)):
    tickers = get_ticker_sid_dict_from_bundle(bundle_name)
    populate_raw_data_from_api(tickers, fields, dims, raw_path)


def all_tickers_for_bundle_from_dump(fields, dims, bundle_name, raw_path=os.path.join(BASE, RAW_FLDR)):
    tickers = get_ticker_sid_dict_from_bundle(bundle_name)
    populate_raw_data_from_dump(tickers, fields, dims, raw_path)


def num_tkrs_in_bundle(bundle_name):
    return len(get_ticker_sid_dict_from_bundle(bundle_name))


if __name__ == '__main__':
    # dimensions = ['ART'] * len(fields)  # use all ART

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

    BUNDLE_NAME = 'sep'
    num_tickers = num_tkrs_in_bundle(BUNDLE_NAME)
    print('number of tickers: ', num_tickers)

    # Uncomment this next line if you want to load the data using quandl api, and comment all_tickers_for_bundle_from_dump
    # all_tickers_for_bundle_from_api(fields, dimensions, 'sep')   all_tickers_for_bundle_from_dump(fields, dimensions, BUNDLE_NAME)  # downloads the data to /raw_ART
    fields_dimensions = ['{}_{}'.format(i, j) for i, j in zip(fields, dimensions)]
    pack_sparse_data(num_tickers + 1,  # number of tickers in bundle + 1
                     os.path.join(BASE, RAW_FLDR),
                     fields_dimensions,
                     ZIPLINE_DATA_DIR + FN)  # write directly to the zipline data dir

    print("------------------ finish work ----------------------")
