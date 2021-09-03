from COVID19Map.PublicFun.model import TCountryMapping

#TODO:插入功能还未实现
def TCountryMappingListInsert(modelList: []):
    print("插入成功")


def TCountryMappingUpdateByUid(model: TCountryMapping):
    print(model.UID)


if __name__ == "__main__":
    countryConfig1 = TCountryMapping.TCountryMapping()
    countryConfig1.UID = "123"
    countryConfig2 = TCountryMapping.TCountryMapping()
    countryConfig2.UID = "1234"
    print(countryConfig1.UID, countryConfig2.UID)
    TCountryMappingUpdateByUid(countryConfig1)
