class TCountryMapping(object):
    """
    国家地区配置映射类
    """
    __slots__ = (
        "_UID", "_iso2", "_iso3", "_code3", "_FIPS", "_Admin2", "_ProvinceState", "_CountryRegion", "_PointLat",
        "_PointLong", "_CombinedKey", "_Population")

    def __init__(self):
        self._UID = None
        self._iso2 = None
        self._iso3 = None
        self._code3 = None
        self._FIPS = None
        self._Admin2 = None
        self._ProvinceState = None
        self._CountryRegion = None
        self._PointLat = None
        self._PointLong = None
        self._CombinedKey = None
        self._Population = None

    @property
    def UID(self):
        return self._UID

    @UID.setter
    def UID(self, value):
        self._UID = value

    @property
    def iso2(self):
        return self._iso2

    @iso2.setter
    def iso2(self, value):
        self._iso2 = value

    @property
    def iso3(self):
        return self._iso3

    @iso3.setter
    def iso3(self, value):
        self._iso3 = value

    @property
    def code3(self):
        return self._code3

    @code3.setter
    def code3(self, value):
        self._code3 = value

    @property
    def FIPS(self):
        return self._FIPS

    @FIPS.setter
    def FIPS(self, value):
        self._FIPS = value

    @property
    def Admin2(self):
        return self._Admin2

    @Admin2.setter
    def Admin2(self, value):
        self._Admin2 = value

    @property
    def ProvinceState(self):
        return self._ProvinceState

    @ProvinceState.setter
    def ProvinceState(self, value):
        self._ProvinceState = value

    @property
    def CountryRegion(self):
        return self._CountryRegion

    @CountryRegion.setter
    def CountryRegion(self, value):
        self._CountryRegion = value

    @property
    def PointLat(self):
        return self._PointLat

    @PointLat.setter
    def PointLat(self, value):
        self._PointLat = value

    @property
    def PointLong(self):
        return self._PointLong

    @PointLong.setter
    def PointLong(self, value):
        self._PointLong = value

    @property
    def CombinedKey(self):
        return self._CombinedKey

    @CombinedKey.setter
    def CombinedKey(self, value):
        self._CombinedKey = value

    @property
    def Population(self):
        return self._Population

    @Population.setter
    def Population(self, value):
        self._Population = value


if __name__ == "__main__":
    test = TCountryMapping()
    test.UID = "123"
    test2 = TCountryMapping()
    test2.UID = "12345"
    print(test.UID, test2.UID)
