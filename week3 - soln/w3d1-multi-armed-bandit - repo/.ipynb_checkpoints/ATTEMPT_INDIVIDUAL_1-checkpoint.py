from pprint import pprint
import math
import statsmodels.stats as sms
import statsmodels.api as sm
import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

dfA=pd.read_csv('data/siteA.txt', sep=' ')


# def beta_distribution(views, dfA, dfB):
    