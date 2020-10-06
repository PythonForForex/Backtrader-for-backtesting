============================================================================
Backtrader for Backtesting (Python) - A Complete Guide - AlgoTrading101 Blog
============================================================================

This is the code used in `Backtrader for Backtesting (Python) <https://algotrading101.com/learn/backtrader-for-backtesting/>`_ published on the Algotrading101 Blog

-----------------
Table of Contents
-----------------

* `What is Backtrader?  <https://algotrading101.com/learn/backtrader-for-backtesting/#what-is-backtrader>`_
* `Why should I learn Backtrader?  <https://algotrading101.com/learn/backtrader-for-backtesting/#why-learn-backtrader>`_
* `Why shouldn’t I learn Backtrader?  <https://algotrading101.com/learn/backtrader-for-backtesting/#why-shouldnt-i-learn-backtrader>`_
* `Overview of how Backtrader works  <https://algotrading101.com/learn/backtrader-for-backtesting/#backtrader-overview>`_
* `How to install Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#how-to-install-backtrader>`_
* `Choosing which IDE to use with Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#choosing-ide-to-use-with-backtrader>`_
* `How to configure the basic Backtrader setup  <https://algotrading101.com/learn/backtrader-for-backtesting/#how-to-configure-the-basic-backtrader-setup>`_
* `How to get data and import it into Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#get-data-and-import-to-backtrader>`_
* `How to print or log data using the strategy class in Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#log-data-using-strategy-class-backtrader>`_
* `How to run a backtest using Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#run-a-backtest-using-backtrader>`_
* `How to use the built-in crossover indicator  <https://algotrading101.com/learn/backtrader-for-backtesting/#use-the-builtin-crossover-indicator>`_
* `How to run optimization in Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#run-optimization-in-backtrader>`_
* `How to build a stock screener in Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#build-a-stock-screener-in-backtrader>`_
* `How to code an indicator in Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#code-an-indicator-in-backtrader>`_
* `How to plot in Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#how-to-plot-in-backtrader>`_
* `How to use alternative data in Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#use-alternative-data-in-backtrader>`_
* `How to add visual stats to a backtest  <https://algotrading101.com/learn/backtrader-for-backtesting/#how-to-add-visual-stats-to-backtest>`_
* `How to save backtest data to a CSV file  <https://algotrading101.com/learn/backtrader-for-backtesting/#how-to-save-backtest-data-to-csv>`_
* `Alternatives to Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#alternatives-to-backtrader>`_
* `Final Thoughts on Backtrader  <https://algotrading101.com/learn/backtrader-for-backtesting/#final-thoughts-on-backtrader>`_

------------
Requirements
------------

* `python <https://www.python.org>`_ >= 3.6+
* `backtrader <https://github.com/mementum/backtrader>`_ (tested to work with >= 1.9.76.123 )
* `QuantStats <https://github.com/ranaroussi/quantstats>`_ (tested to work with >= 0.0.25 )
* `pandas <https://github.com/pandas-dev/pandas>`_ (tested to work with >= 1.0.3 )

-----------
Author Info
-----------

:author: Jignesh Davda 
:author page: https://algotrading101.com/learn/author/jdavda/
:published: 2020-03-05
