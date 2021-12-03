from COVID19Map.db.dbInit import db


class TCountryMapping(db.Model):
    __tablename__ = "TCountryMapping"
    FUID = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    Fiso2 = db.Column(db.String(100), nullable=True, unique=False)

    # Fiso3 = db.Column(db.String(100), nullable=True)
    # Fcode3 = db.Column(db.String(100), nullable=True, unique=False)
    # FFIPS = db.Column(db.String(100), nullable=True, unique=False)
    # FAdmin2 = db.Column(db.String(100), nullable=True, unique=False)
    # FProvinceState = db.Column(db.String(100), nullable=True, unique=False)
    # FCountryRegion = db.Column(db.String(100), nullable=True, unique=False)
    # FPointLat = db.Column(db.String(100), nullable=True, unique=False)
    # FPointLong = db.Column(db.String(100), nullable=True, unique=False)
    # FCombinedKey = db.Column(db.String(100), nullable=True, unique=False)
    # FPopulation = db.Column(db.String(100), nullable=True, unique=False)
    def __init__(self, FUID, Fiso2):
        self.FUID = FUID
        self.Fiso2 = Fiso2

    def __repr__(self):
        return '<TCountryMapping %s>' % self.FUID
