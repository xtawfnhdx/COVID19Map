from COVID19Map.PublicFun.model import TCountryMapping


def TCountryMappingInsert(modelList: []):
    pass


def TCountryMappingUpdateByUid(model: TCountryMapping):
    print(model.UID)


if __name__ == "__main__":
    countryConfig1 = TCountryMapping.TCountryMapping()
    countryConfig1.UID = "123"
    countryConfig2 = TCountryMapping.TCountryMapping()
    countryConfig2.UID = "1234"
    print(countryConfig1.UID, countryConfig2.UID)
    TCountryMappingUpdateByUid(countryConfig1)
