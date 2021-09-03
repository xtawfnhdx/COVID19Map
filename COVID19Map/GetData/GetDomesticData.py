import urllib.request
import csv
import io
from COVID19Map.PublicFun.sql import TCountryMappingRepository
from COVID19Map.PublicFun.model import TCountryMapping


def getCSVFile(filePath: str):
    try:
        res = urllib.request.urlopen(filePath)
        context = res.read().decode("utf-8")
        return csv.reader(io.StringIO(context))
    except IOError as ioerror:
        print(ioerror)
    except Exception as e:
        print(e)


def saveCountryMapping(csvFile):
    try:
        countryMappingList = []
        firstline = True
        for line in csvFile:
            if firstline:
                firstline = False
                continue
            temp = TCountryMapping.TCountryMapping()
            temp.UID = line[0]
            temp.iso2 = line[1]
            temp.iso3 = line[2]
            temp.code3 = line[3]
            temp.FIPS = line[4]
            temp.Admin2 = line[5]
            temp.ProvinceState = line[6]
            temp.CountryRegion = line[7]
            temp.PointLat = line[8]
            temp.PointLong = line[9]
            temp.CombinedKey = line[10]
            temp.Population = line[11]
            countryMappingList.append(temp)
        TCountryMappingRepository.TCountryMappingListInsert(countryMappingList)

    except:
        pass


if __name__ == "__main__":
    golbalfile = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    countryMappingFileUrl = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv"
    csvFile = getCSVFile(countryMappingFileUrl)
    saveCountryMapping(csvFile)
