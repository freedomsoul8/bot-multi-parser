import logging

from log import logger
import pysqlite3._sqlite3 as sqlite3

db = sqlite3.connect('db.db',check_same_thread=False)
cursor = db.cursor()

def create_tables_users():
    try:
        sql = '''CREATE TABLE users(user_id text unique ,reg_date text,username text,lang text)'''
        cursor.execute(sql)
        db.commit()
        logger.info('Table Users created')
        return 20
    except Exception as e:
        logger.error('Unable to create table Users',exc_info=True)

async def add_user(user_id,reg_date,username,lang):
    try:
        sql = '''INSERT INTO users(user_id, reg_date, username,lang) VALUES (?,?,?,?)'''
        values = (user_id,reg_date,str(username),str(lang),)
        cursor.execute(sql,values)
        db.commit()
        db.close()
        logger.info(f'User {user_id} sucsesfully added')
        return 20
    except Exception as e:
        logger.error(f'User {user_id} not added',exc_info=True)
        return


def get_user_data(user_id,type):
    if type == 'reg_date':
        try:
            sql = '''SELECT reg_date FROM users WHERE user_id=?'''
            value = (user_id,)
            cursor.execute(sql,value)
            result = cursor.fetchall()
            db.close()
            logger.info(f'Get user {user_id} reg_date')
            return result
        except Exception as e:
            logger.info(f'Unable to get user {user_id} reg_date',exc_info=True)
            return 40

    elif type == 'lang':
        try:
            sql = '''SELECT lang FROM users WHERE user_id=?'''
            value = (user_id,)
            cursor.execute(sql,value)
            result = cursor.fetchall()
            db.close()
            if result == []:
                logger.error(f'Unable to get user {user_id} lang')
                return 40
            else:
                logger.info(f'Get user {user_id} lang')
                return result
        except Exception as e:
            logging.error(f'Unable to get user {user_id} lang',exc_info=True)
            return 40
    else:
        logger.error(f'Unable to get user {user_id} data',exc_info=True)
        return 40

def create_table_parsers():
    try:
        sql = '''CREATE TABLE parsers(parser_id text,user_id text,date_created text,data text,code text)'''
        cursor.execute(sql)
        db.commit()
        db.close()

        return 20
    except Exception as e:
        logger.error(f'Error',exc_info=True)
        return 40





#
if __name__ == '__main__':
    # create_tables_users()
    # add_user(user_id='0',reg_date='0',username='_',lang='_')
    get_user_data(user_id="0",type="la")
