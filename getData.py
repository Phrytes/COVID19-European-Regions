from gitsnapshot import load_repo

# Italy
load_repo('../Data/IT', 'https://github.com/pcm-dpc/COVID-19', use_existing=True)
# Netherlands
load_repo('../Data/NL', 'https://github.com/J535D165/CoronaWatchNL.git', use_existing=True)
# France
load_repo('../Data/FR', 'https://github.com/opencovid19-fr/data', use_existing=True)
# Germany:
#RKI_cases <- htmltab(doc = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html", which = "//th[text() = 'Bundesland']/ancestor::table") %>%
#  rename(german_name = Bundesland)

# United Kingdom
load_repo('../Data/UK', 'https://github.com/emmadoughty/Daily_COVID-19', use_existing=True)
# Belgium

# Switzerland
load_repo('../Data/CH', 'https://github.com/openZH/covid_19/', use_existing=True)
