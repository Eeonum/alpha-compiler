"""
This file is for loading the sector codes from Sharadar.  The sector codes come in a
'ticker' file.
The sectors are coded as an integer and stored in a .npy file for fast loading during
a Zipline algorithm run.
Make sure you get the ticker file from:
https://www.quandl.com/tables/SHARADAR-TICKERS/export?api_key=your_api_key
not from the Quandl web GUI.
Created by Peter Harrington (pbharrin) on 8/5/19.
"""

import os
import pandas as pd
import numpy as np
from alphacompiler.util.zipline_data_tools import get_ticker_sid_dict_from_bundle
from zipline.data.bundles.core import register

TICKER_FILE = '~/.zipline/data-for-alpha-compiler/SHARADAR_TICKERS_6cc728d11002ab9cb99aa8654a6b9f4e.csv'
BUNDLE_NAME = 'sep'

ZIPLINE_DATA_DIR = '/Users/work/.zipline/data/'  # TODO: get this from Zipline api
SID_FILE = "SHARDAR_sectors.npy"  # persisted np.array
STATIC_FILE = "SHARDAR_static.npy"  # persisted np.array

SECTOR_CODING = {'Technology': 0,
                 'Industrials': 1,
                 'Energy': 2,
                 'Utilities': 3,
                 'Consumer Cyclical': 4,
                 'Healthcare': 5,
                 'Financial Services': 6,
                 'Basic Materials': 7,
                 'Consumer Defensive': 8,
                 'Real Estate': 9,
                 'Communication Services': 10,
                 np.nan: -1}  # a few tickers are missing sectors, these should be ignored

EXCHANGE_CODING = {'NYSE': 0,
                   'NASDAQ': 1,
                   'NYSEMKT': 2,  # previously AMEX
                   'OTC': 3,
                   'NYSEARCA': 4,
                   'BATS': 5}

# this is organized so that we can filter out the tradable stuff with one less than operation
CATEGORY_CODING = {'Domestic Stock Warrant': 0,
                   'Domestic Preferred Stock': 1,
                   'Domestic Common Stock Primary Class': 2,
                   'Canadian Common Stock Secondary Class': 3,
                   'ADR Common Stock': 4,
                   'ADR Stock Warrant': 5,
                   'ADR Preferred Stock': 6,
                   'Canadian Preferred Stock': 7,
                   'ADR Common Stock Secondary Class': 8,
                   'Canadian Common Stock Primary Class': 9,
                   'Canadian Common Stock': 10,
                   'Canadian Stock Warrant': 11,
                   'Domestic Common Stock Secondary Class': 12,
                   'Domestic Common Stock': 13,
                   'ADR Common Stock Primary Class': 14}

INDUSTRY_CODING = {'Tobacco': 0,
                   'Data Storage': 1,
                   'REIT - Residential': 2,
                   'Luxury Goods': 3,
                   'Biotechnology': 4,
                   'Metal Fabrication': 5,
                   'Home Furnishings & Fixtures': 6,
                   'Oil & Gas Drilling': 7,
                   'Insurance Brokers': 8,
                   'Aerospace & Defense': 9,
                   'Electrical Equipment & Parts': 10,
                   'Lumber & Wood Production': 11,
                   'Computer Hardware': 12,
                   'Utilities - Diversified': 13,
                   'Lodging': 14,
                   'Staffing & Outsourcing Services': 15,
                   'Financial Exchanges': 16,
                   'Travel Services': 17,
                   'Business Services': 18,
                   'Insurance - Life': 19,
                   'Oil & Gas E&P': 20,
                   'Apparel Manufacturing': 21,
                   'Oil & Gas Midstream': 22,
                   'Electronics & Computer Distribution': 23,
                   'Pharmaceutical Retailers': 24,
                   'Apparel Retail': 25,
                   'Farm & Construction Equipment': 26,
                   'Steel': 27,
                   'Drug Manufacturers - Major': 28,
                   'Home Improvement Retail': 29,
                   'Banks - Diversified': 30,
                   'Recreational Vehicles': 31,
                   'Grocery Stores': 32,
                   'Furnishings': 33,
                   'Farm & Heavy Construction Machinery': 34,
                   'Airports & Air Services': 35,
                   'Software - Infrastructure': 36,
                   'Software - Application': 37,
                   'Medical Care Facilities': 38,
                   'Real Estate - Development': 39,
                   'Medical Distribution': 40,
                   'Medical Instruments & Supplies': 41,
                   'Residential Construction': 42,
                   'Building Products & Equipment': 43,
                   'Real Estate Services': 44,
                   'Utilities - Regulated Water': 45,
                   'Semiconductors': 46,
                   'Confectioners': 47,
                   'Insurance - Property & Casualty': 48,
                   'Healthcare Plans': 49,
                   'Building Materials': 50,
                   'Internet Retail': 51,
                   'Insurance - Reinsurance': 52,
                   'Personal Services': 53,
                   'Industrial Distribution': 54,
                   'Specialty Chemicals': 55,
                   'Entertainment': 56,
                   'Diversified Industrials': 57,
                   'Education & Training Services': 58,
                   'Coking Coal': 59,
                   'Utilities - Independent Power Producers': 60,
                   'Solar': 61,
                   'Aluminum': 62,
                   'Long-Term Care Facilities': 63,
                   'Food Distribution': 64,
                   'Textile Manufacturing': 65,
                   'Drug Manufacturers - Specialty & Generic': 66,
                   'Security & Protection Services': 67,
                   'Oil & Gas Integrated': 68,
                   'Oil & Gas Equipment & Services': 69,
                   'Asset Management': 70,
                   'NaN': 71,
                   'Apparel Stores': 72,
                   'Specialty Business Services': 73,
                   'Farm Products': 74,
                   'Agricultural Inputs': 75,
                   'Leisure': 76,
                   'Business Equipment': 77,
                   'Insurance - Specialty': 78,
                   'Semiconductor Memory': 79,
                   'Scientific & Technical Instruments': 80,
                   'Furnishings Fixtures & Appliances': 81,
                   'Gold': 82,
                   'Infrastructure Operations': 83,
                   'Consulting Services': 84,
                   'REIT - Specialty': 85,
                   'Media - Diversified': 86,
                   'Footwear & Accessories': 87,
                   'Beverages - Wineries & Distilleries': 88,
                   'Shell Companies': 89,
                   'Chemicals': 90,
                   'Information Technology Services': 91,
                   'Banks - Regional': 92,
                   'Tools & Accessories': 93,
                   'Oil & Gas Refining & Marketing': 94,
                   'Household & Personal Products': 95,
                   'REIT - Hotel & Motel': 96,
                   'Rental & Leasing Services': 97,
                   'Trucking': 98,
                   'REIT - Office': 99,
                   'Broadcasting - TV': 100,
                   'Business Equipment & Supplies': 101,
                   'Financial Data & Stock Exchanges': 102,
                   'Auto & Truck Dealerships': 103,
                   'Specialty Retail': 104,
                   'Savings & Cooperative Banks': 105,
                   'Specialty Finance': 106,
                   'Real Estate - General': 107,
                   'Engineering & Construction': 108,
                   'Health Information Services': 109,
                   'Utilities - Renewable': 110,
                   'Mortgage Finance': 111,
                   'Paper & Paper Products': 112,
                   'Other Industrial Metals & Mining': 113,
                   'Copper': 114,
                   'Pollution & Treatment Controls': 115,
                   'Health Care Plans': 116,
                   'Capital Markets': 117,
                   'Staffing & Employment Services': 118,
                   'Electronic Components': 119,
                   'Integrated Freight & Logistics': 120,
                   'Advertising Agencies': 121,
                   'REIT - Retail': 122,
                   'Utilities - Regulated Electric': 123,
                   'Beverages - Non-Alcoholic': 124,
                   'Consumer Electronics': 125,
                   'Auto Parts': 126,
                   'Silver': 127,
                   'Drug Manufacturers - General': 128,
                   'Shipping & Ports': 129,
                   'Department Stores': 130,
                   'Airlines': 131,
                   'Coal': 132,
                   'Internet Content & Information': 133,
                   'Other Precious Metals & Mining': 134,
                   'Medical Devices': 135,
                   'Electronic Gaming & Multimedia': 136,
                   'Telecom Services': 137,
                   'Home Improvement Stores': 138,
                   'Real Estate - Diversified': 139,
                   'Publishing': 140,
                   'Beverages - Brewers': 141,
                   'Computer Systems': 142,
                   'Broadcasting - Radio': 143,
                   'Beverages - Soft Drinks': 144,
                   'Utilities - Regulated Gas': 145,
                   'REIT - Mortgage': 146,
                   'REIT - Healthcare Facilities': 147,
                   'Insurance - Diversified': 148,
                   'Marine Shipping': 149,
                   'REIT - Diversified': 150,
                   'Uranium': 151,
                   'Auto Manufacturers': 152,
                   'Resorts & Casinos': 153,
                   'REIT - Industrial': 154,
                   'Financial Conglomerates': 155,
                   'Packaged Foods': 156,
                   'Communication Equipment': 157,
                   'Credit Services': 158,
                   'Specialty Industrial Machinery': 159,
                   'Industrial Metals & Minerals': 160,
                   'Gambling': 161,
                   'Conglomerates': 162,
                   'Railroads': 163,
                   'Diagnostics & Research': 164,
                   'Discount Stores': 165,
                   'Thermal Coal': 166,
                   'Broadcasting': 167,
                   'Waste Management': 168,
                   'Semiconductor Equipment & Materials': 169,
                   'Banks - Regional - US': 170,
                   'Medical Care': 171,
                   'Packaging & Containers': 172,
                   'Restaurants': 173}


def create_sid_table_from_file(filepath):
    """reads the raw_ART file, maps tickers -> SIDS,
    then maps sector strings to integers, and saves
    to the file: SID_FILE"""
    register(BUNDLE_NAME, int, )

    df = pd.read_csv(filepath, index_col="ticker")
    assert df.shape[0] > 10001  # there should be more than 10k tickers
    df = df[df.exchange != 'None']
    df = df[df.exchange != 'INDEX']
    df = df[df.table == 'SEP']

    coded_sectors_for_ticker = df["sector"].map(SECTOR_CODING)

    ae_d = get_ticker_sid_dict_from_bundle(BUNDLE_NAME)
    N = max(ae_d.values()) + 1

    # create empty 1-D array to hold data where index = SID
    sectors = np.full(N, -1, np.dtype('int64'))

    # iterate over Assets in the bundle, and fill in sectors
    for ticker, sid in ae_d.items():
        sector_coded = coded_sectors_for_ticker.get(ticker, -1)
        print(ticker, sid, sector_coded)
        sectors[sid] = sector_coded
    print(sectors)

    # finally save the file to disk
    np.save(ZIPLINE_DATA_DIR + SID_FILE, sectors)


def create_static_table_from_file(filepath):
    """Stores static items to a persisted np array.
    The following static fields are currently persisted.
    -Sector
    -exchange
    -category
    """
    register(BUNDLE_NAME, int, )

    df = pd.read_csv(filepath, index_col="ticker")
    assert df.shape[0] > 10001  # there should be more than 10k tickers
    df = df[df.exchange != 'None']
    df = df[df.exchange != 'INDEX']
    df = df[df.table == 'SEP']
    df['industry'].fillna('NaN', inplace=True)

    coded_sectors_for_ticker = df['sector'].map(SECTOR_CODING)
    coded_exchange_for_ticker = df['exchange'].map(EXCHANGE_CODING)
    coded_category_for_ticker = df['category'].map(CATEGORY_CODING)
    coded_industry_for_ticker = df['industry'].map(INDUSTRY_CODING)

    ae_d = get_ticker_sid_dict_from_bundle(BUNDLE_NAME)
    N = max(ae_d.values()) + 1

    # create 2-D array to hold data where index = SID
    sectors = np.full((4, N), -1, np.dtype('int64'))
    # sectors = np.full(N, -1, np.dtype('int64'))

    # iterate over Assets in the bundle, and fill in static fields
    for ticker, sid in ae_d.items():
        # print(ticker, sid, coded_sectors_for_ticker.get(ticker, -1))
        print(ticker, sid, coded_category_for_ticker.get(ticker, -1))
        sectors[0, sid] = coded_sectors_for_ticker.get(ticker, -1)
        sectors[1, sid] = coded_exchange_for_ticker.get(ticker, -1)
        sectors[2, sid] = coded_category_for_ticker.get(ticker, -1)
        sectors[3, sid] = coded_industry_for_ticker.get(ticker, -1)

    print(sectors)
    print(sectors[:, -10:])

    # finally save the file to disk
    # np.save(ZIPLINE_DATA_DIR + STATIC_FILE, sectors)
    sectors.dump(ZIPLINE_DATA_DIR + STATIC_FILE)


if __name__ == '__main__':
    create_static_table_from_file(TICKER_FILE)
    create_sid_table_from_file(TICKER_FILE)  # only SID sectors
