import mysql

data = mysql.from_mysql_get_all_info('select * from a')
mysql.write_csv('C:\\Users\\86178\\Desktop\\test\\data\\a.csv',data)

mysql.write_mysql('C:\\Users\\86178\\Desktop\\test\\data\\jin-shamingsong.csv',name='a')