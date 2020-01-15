import pymysql
import csv
import pandas as pd

def from_mysql_get_all_info(sql):
    conn = pymysql.connect(
        host='120.26.240.13',
        port=3306,
        user='root',
        db='roman',
        password='roman',
        charset='utf8mb4')
    cursor = conn.cursor()
    #sql = 'select * from apt_data'
    cursor.execute(sql.encode('utf-8'))
    data = cursor.fetchall()
    conn.close()
    return data

def write_csv(filename,data):
    #print(data)
    with open(filename,mode='w',encoding='utf8') as f:
        write = csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)
    data = pd.read_csv(filename,encoding = 'gbk')

    #data = df.drop(['1'],axis=1)
    data.to_csv(filename,index=0, header=1)#单引号中间表示保存的文件名称
    #print(data)

