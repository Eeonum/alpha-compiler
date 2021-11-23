
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
      * after the downloads, move both data files to ```~/.zipline/data-for-alpha-compiler``` (I assume that you have had zipline installed in your machine once which auto created .zipline at the root directory)
        * if you don't have the directory yet, then ```$cd ~/.zipline``` and then ```$mkdir data-for-alpha-compiler```.
    * or, we can download the data using quandl library, which we've installed at step 1.
      * will explain in later section.
