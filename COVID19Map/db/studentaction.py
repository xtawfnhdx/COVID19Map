from COVID19Map.db.mysqlInit import Session


def search_student():
    session = Session()
    sql = '''
        SELECT * FROM test.TStudent
    '''
    cursor = session.execute(sql)
    result = cursor.fetchall()
    session.close()
    return result
if __name__=="__main__":
    res=search_student()
    print(res)