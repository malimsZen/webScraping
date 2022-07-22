# In this module I'll be extracting data from Trading Economics using thier APIs and indicators.

import tradingeconomics as te
import pandas as pd

te.login()

indicatorData = te.getIndicatorData(output_type='df')
df = pd.DataFrame(indicatorData)
print(df)

