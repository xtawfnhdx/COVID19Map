import urllib.request
import csv
import io
from COVID19Map.PublicFun.sql import TCountryMappingRepository
from COVID19Map.PublicFun.model import TCountryMapping


def getCSVFile(filePath: str):
    try:
        res = urllib.request.urlopen(filePath)
        context = res.read().decode("utf-8")
        csvreader = csv.reader(io.StringIO(context))
        for line in csvreader:
            print(line)
    except IOError as ioerror:
        print(ioerror)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    abc = TCountryMapping.TCountryMapping()
    abc.UID="123456"
    TCountryMappingRepository.TCountryMappingUpdateByUid(abc)
    #
    # golbalfile = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    # getCSVFile(golbalfile)
