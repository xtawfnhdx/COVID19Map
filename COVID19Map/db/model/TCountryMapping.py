from COVID19Map.db.dbInit import db


# 定义ORM模型
class TCountryMapping(db.Model):
    __tablename__ = "TCountryMapping"
    id=db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True,nullable=False)
    FUID = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    Fiso2 = db.Column(db.String(100), nullable=True, unique=False)

    # region 暂时删除的列信息

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

    # endregion
    def __init__(self, FUID, Fiso2):
        self.FUID = FUID
        self.Fiso2 = Fiso2

    def __repr__(self):
        return '<TCountryMapping %s>' % self.FUID


class TCountryTest(db.Model):
    __tablename__ = "TCountryTest"
    # nullable：是否可为空，False不可为空
    # autoincrement：自增长
    # unique：设置某字段是否唯一
    # default：设置某字段的默认值
    # name：指定字段名，如果不指定，则默认使用前面的字段名
    # onupdate：在跟新的时候，使用该字段指定的默认值或者函数
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    textStr = db.Column(db.String(50), default="")
    def __init__(self,str):
        self.textStr=str
    #region  外键与映射  但是业务中一般不做这种硬编码
    '''
    uid=db.Column(db.Integer,db.ForeignKey("TCountryMapping.id"))

    #第一个参数“对象或者类”名
    #第二个参数：“表”名   代表反向引用，对方访问我的字段名
    counts=db.relationship("TCountryMapping",backref="TCountryTests")
    
    '''

    #endregion
