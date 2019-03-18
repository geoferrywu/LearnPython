import mysql.connector

def test():
    config = {
        'host': '127.0.0.1',
        'user': 'test',
        'password': '12345678',
        'port': 3306,
        'database': 'world',
        'charset': 'utf8'
    }
    try:
        cnn = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
        return
    
    cursor = cnn.cursor()

    try:
        sql_query = 'select ID,Name from world.city ;'
        cursor.execute(sql_query)
        
        alldata = cursor.fetchall()

        print(alldata)
        # for id, name in cursor:
        #     pass
        #     # print (id, name)
        # print(cursor.rowcount)
    except mysql.connector.Error as e:
        print('query error!{}'.format(e))
    finally:
        cursor.close()
        cnn.close()

def main():
    """
        主函数
    """
    test()


if __name__ == '__main__':
    main()