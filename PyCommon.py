###############################################
##  Common Python code used by the examples  ##
###############################################
from math import isnan
import pandas as pd
import requests
import platform
import sys
from textwrap import dedent
from natsort import natsorted, index_natsorted, order_by_index

__version__ = "0.1.0"

def isNaN(x):
    return x!=x
    
def carboncrosstab(topseries : pd.Series, sideseries : pd.Series, colpercents : bool=False,natsort : bool =False,dps:int=2): #,basis : pd.Series = pd.Series([1.0 for x in range(len(df.index))])):
    topcd=topseries.to_list()
    sidecd=sideseries.to_list()
    postdata={"top": topcd,"side": sidecd, 'props':f'Decimals.Frequencies={dps}' }
    headers = {'content-type': 'application/json; charset=utf-8','Accept':'application/json','UserID':'16499372','Password': 'C6H12O6'}
    
    try:
        response = requests.post('https://rcsapps.azurewebsites.net/carbontest/python/crosstab/alphacodes', json=postdata,headers=headers)
        if colpercents:
            freqs=pd.DataFrame(response.json()).astype(float)
            basis=pd.Series([1.0 for x in range(len(topseries.index))])
            bases=carboncrosstab(topseries,basis,False,dps).astype(float).squeeze()
            if natsort:
                tab=freqs.div(bases).mul(100).round(dps)
                tab=tab.reindex(index=natsorted(tab.index))
                return tab
            else:
                return freqs.div(bases).mul(100).round(dps)
        else:
            if natsort:
                tab = pd.DataFrame(response.json())
                tab = tab.reindex(index=natsorted(tab.index))
                return tab
            else:
                return pd.DataFrame(response.json())
    except:
        return requests.post('https://rcsapps.azurewebsites.net/carbontest/python/crosstab/alphacodes', json=postdata,headers=headers)

def removeCatNaNs(nas:str):
    global df
    for col in df.columns:
        entries=[]
        if df[col].isna().values.any():
            for r in df[col]:
                if isNaN(r):
                    entries.append(nas)
                else:
                    entries.append(r)
        if len(entries) == len(df):
            df[col]=pd.Categorical(entries)
    return df

def naturalSort(dfdf:pd.DataFrame):
    dfdf = dfdf.reindex(index=natsorted(dfdf.index))
    return dfdf

def version_info() -> str:
    """Display the version of the program, python and the platform."""
    return dedent(
        f"""\
        ------------------------------------------------------------------
            PyCarbon: {__version__}
            Python: {sys.version.split(" ", maxsplit=1)[0]}
            Platform: {platform.platform()}
        ------------------------------------------------------------------"""
    )

def main():
    pass

if __name__ == '__main__':
    main()
