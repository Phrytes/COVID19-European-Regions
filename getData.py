from gitsnapshot import load_repo

# Italy
load_repo('../Data/Sources/IT', 'https://github.com/pcm-dpc/COVID-19', use_existing=True)

# Netherlands
load_repo('../Data/Sources/NL', 'https://github.com/J535D165/CoronaWatchNL.git', use_existing=True)

# France
load_repo('../Data/Sources/FR', 'https://github.com/opencovid19-fr/data', use_existing=True)

# United Kingdom
load_repo('../Data/Sources/UK', 'https://github.com/emmadoughty/Daily_COVID-19', use_existing=True)

# Belgium

# Switzerland
load_repo('../Data/Sources/CH', 'https://github.com/openZH/covid_19/', use_existing=True)

# Germany:
# Downloaded directly from the source. Check editDataGermany.py