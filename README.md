
# Alpha Compiler

----------- *From the creator* -----------

Various tools for quantitative finance with Python.  Many tools for working with the Zipline open source library, and replicating Quantopian tools in your personal env.   

*Update March 2021 now tested with Python 3.6, and Zipline 1.4.1*


You can find details on Alpha Compiler [here](https://pbharrin.github.io/alpha-compiler/syntax "Title")


----------- *From Us* -----------

In order to make the original version of Alpha Compiler work in our local machine, we need to perform a series of complex steps. While we believe there are better ways out there, we still attempt to do some slight modifications on Alpha Compiler to ease the pain of redirecting multiple input data paths, to fix minor bugs so that the Fundamentals class will work as intended, as well as to provide proper documentation so new users won't have to go through the confusions we had gone through. 

*Update November 2021 now tested with python 3.7.11 (Python virtual environment) on MacOS Big Sur v11.6, and zipline-trader*

Remark: we believe alpha-compiler is compatible with any python version and any zipline version, as long as you are able to install zipline into your python environment and make it function proper, i.e. data ingestion, run_algorithm, etc.

## **Installation Instruction**
1. Git clone our version of alpha-compiler to your project directory, i.e. ```$cd path/to/your/project```, and then ```$git clone https://github.com/Eeonum/alpha-compiler.git```
2. Install quandl as it is the main library for alpha-compiler to fetch the fundamentals data from *[Sharadar Core US Equities Bundle](https://data.nasdaq.com/databases/SFA/data)*
first ```$pip install --upgrade pip``` and then ```$pip install quandl```

3. To load and parse the fundamentals data, we have two ways:
    * we can manually download the data (assume you've subscribed to the database), i.e. SHARADAR/SF1 (which is faster than loading them using quandl API), at [data.nasdaq.com](https://data.nasdaq.com/databases/SFA/usage/export). 
      * after the download, move the data (file name is something like this SHARADAR_SF1_017f04a0d2ef7cc409f920be72167ada.csv) to ```~/.zipline/data-for-alpha-compiler``` (I assume that you have had zipline installed in your machine once which auto created .zipline at the root directory)
        * if you don't have the directory yet, then ```$cd ~/.zipline``` and then ```$mkdir data-for-alpha-compiler```.
    * or, we can download the data using quandl library, which we've installed at step 1.
      * will explain in later section.

4. Here comes the tricky steps:
   1. Before starting loading fundamentals data, you must first have an ingested zipline bundle, as alpha-compiler will try to fetch all the available tickers from the zipline bundle and then fetch fundamentals based off these tickers.
      * The zipline bundle we use is 'sep', and if you have a different bundle, make sure to change ```BUNDLE_NAME='sep'``` at the bottom of ```alphacompiler/data/load_quandl_sf1.py``` to the name of your bundle. 
   2. After you've completed the steps above, you can in the terminal, under your project directory, with your python env activated,
      
      ```$cd alpha-compiler/```
      and then 
      ```$python setup.py install```
   3. We will create a empty folder to contain the raw fundamentals data files.
      1. ```mkdir alphacompiler/data/raw```
   4. Finally, you can run ```$python alphacompiler/data/load_quandl_sf1.py```
   5. After the script is done running, you should see a SF1.npy file in ```~.zipline/data/```. If you do, congratulations, you've successfully loaded and parsed the data into a zipline-friendly form, and you can start working with fundamentals data under zipline environment.

## IMPORTANT: **Test if the Fundamentals class is working and how to work with it**
Let's test if it works by running alphacompiler/examples/pipeline_CAPEX.py.
* Open alpha-compiler/alphacompiler/data/sf1_fundamentals.py as it is where Fundamentals class is located in. Watch the outputs closely, i.e. ```outputs = ['equity_ART', 'netinc_ART']```.
  * You need to have an idea of which set of fundamentals you've loaded, either by checking any csv file located at ```alpha-compiler/alphacompiler/data/raw/```, or the fields variable at the bottom of ```alpha-compiler/alphacompiler/data/load_quandl_sf1.py```, i.e.
  
  ```fields4 = ['netinc', 'equity', 'bvps', 'sps', 'fcfps', 'price', 'roe', 'roe']```
  
  ```dimensions = ['ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ART', 'ARQ']```
* Make sure to save the fundamentals you want to use in ```outputs``` and the names of the fundamentals should be consistent with what's shown in the first row of the csv files in the raw folder.
  * For example, I want to use netinc_ART and equity_ART in my analysis, so my outputs is ```outputs = ['equity_ART', 'netinc_ART']```, and the way I use the data with Fundamentals, is demonstrated in alphacompiler/examples/pipeline_CAPEX.py, i.e. ```fd.equity_ART```.
* After all the setups in the above, last step is to run in the terminal ```python setup.py install``` like you did at step 4.2 to update the package.
  * You will have to do this every time you modify the ```outputs```.
* If you see an output after running pipeline_CAPEX.py like this:
```2021-01-04 21:00:00+00:00
                    longs  shorts       netinc        equity
Equity(0 [A])       False   False  719000000.0  4.873000e+09
Equity(2 [AA])      False   False -469000000.0  3.395000e+09
Equity(15 [AACG])   False   False -122253989.0  3.056352e+08
Equity(21 [AACQU])  False   False          NaN           NaN
Equity(22 [AADI])   False   False   -4043797.0  4.731842e+07
2021-01-05 21:00:00+00:00
                    longs  shorts       netinc        equity
Equity(0 [A])       False   False  719000000.0  4.873000e+09
Equity(2 [AA])      False   False -469000000.0  3.395000e+09
Equity(15 [AACG])   False   False -122253989.0  3.056352e+08
Equity(21 [AACQU])  False   False          NaN           NaN
Equity(22 [AADI])   False   False   -4043797.0  4.731842e+07
```
Congratulations, this works boss!

### *Tips*
* If you have multiple zipline projects which employ different set of fundamentals features, make sure to change ```FN = "SF1.npy"``` to not overwrite the existing data at alpha-compiler/alphacompiler/data/load_quandl_sf1.py and ```self.data_path = zipline_root() + '/data/SF1.npy'``` at alpha-compiler/alphacompiler/data/sf1_fundamentals.py. After the changes, you need to again update the package like you did at step 4.2.