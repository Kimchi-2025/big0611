# 내장 패키지
import os

# 외부 패키지
from dotenv import load_dotenv
import pymysql

#사용자 패키지
from ex01_주식크롤링 import stock

# 1. .env 파일의 환경 변수 로드
load_dotenv()

res = stock()

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_DATABASE"),
    charset="utf8"
)

# 데이터 삽입
# INSERT INTO 데이터베이스명.테이블명(테이블 열 이름) VALUES(삽입하고 싶은 자료형);

sql_state = '''INSERT INTO stock.daily_market(dt, item_name, item_code, price, foreign_ownership_ratio, rel_return, per, per_12m, per_ind, pbr, dividend_yield, volume, trans_price, market_capital_prefer, market_capital_common) VALUES ('%s', '%s', '%s', %d, %f, %f, %f, %f, %f, %f, %f, %d, %d, %d, %d)'''%(tuple(res))
print(sql_state)

# 1. 연결 객체 생성
db = conn.cursor()
# 2. SQL 쿼리문을 실행
db.execute(sql_state)
# 3. DB에 변경 사항 반영
conn.commit()
# 4. 연결 닫기
conn.close()


