from gitsnapshot import load_repo

# Maybe use this: https://apify.com/covid-19

# Italy
load_repo('../Data/Sources/IT', 'https://github.com/pcm-dpc/COVID-19', use_existing=True)

# Netherlands
load_repo('../Data/Sources/NL', 'https://github.com/J535D165/CoronaWatchNL.git', use_existing=True)

# France
load_repo('../Data/Sources/FR', 'https://github.com/opencovid19-fr/data', use_existing=True)

# United Kingdom
load_repo('../Data/Sources/UK', 'https://github.com/emmadoughty/Daily_COVID-19', use_existing=True)

# Belgium
#load_repo('../Data/Sources/DE', 'https://github.com/Phrytes/COVID19_Sciensano_Belgium/', use_existing=True)

# Switzerland
load_repo('../Data/Sources/CH', 'https://github.com/openZH/covid_19/', use_existing=True)

# Germany:
#load_repo('../Data/Sources/DE', 'https://github.com/Phrytes/COVID19_RKI_Germany/', use_existing=True)

# Spain:
load_repo('../Data/Sources/ES', 'https://github.com/datadista/datasets/', use_existing=True)