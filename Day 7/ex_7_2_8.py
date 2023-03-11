class MySQL:
    def __init__(self):
        pass

    def select(self, rows, cols):
        return MySQLResult(rows, cols)


class MySQLResult:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        print("trace:", trace)
        self.close()

    def get_row(self, i):
        if i < 0 or i > self.rows:
            raise ValueError("输入的范围错误")
        else:
            print(f"Get row {i}")

    def get_col(self, i):
        if i < 0 or i > self.cols:
            raise ValueError("输入的范围错误")
        else:
            print(f"Get col {i}")

    def close(self):
        print("退出")
        exit()

sql = MySQL()
sqlr = sql.select(5,5)

with MySQLResult(5,5) as msql:
    msql.get_col(2)
    msql.get_row(6)


