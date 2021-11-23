from flask import Flask, render_template, request,  jsonify, current_app
from sqlalchemy import create_engine, text
import datetime 
import pymysql 
import mysql.connector
app = Flask(__name__)

def get_MySQLConnection(): # return MySQLConnection object 
    mydb = mysql.connector.connect( 
            host="127.0.0.1",
            user="root",
            passwd="dkssud",
            database="flask_test")
    return mydb

#mysql_con = None

@app.route('/', methods=["POST","GET"])
def main_page():
    return render_template('index.html') # 메인 페이지

outer_user_SSN = ''
@app.route('/user', methods=["POST","GET"])
def user_info():
    global outer_user_SSN 
    mysql_connection = get_MySQLConnection()
    mysql_cursor = mysql_connection.cursor(dictionary=True)

    user_info = request.form.get('get_user') # 내 정보 확인 

    if request.method == "POST":   
        data = (user_info)
        sql = """select * from user where user_name = %s;"""
        mysql_cursor.execute(sql, (data,))

        for row in mysql_cursor:
            dic = row 
            break 
        
        if len(dic) > 0:
            user_SSN = dic['user_SSN']
            user_name = dic['user_name']
            user_address = dic['user_address']
            user_birth = dic['user_birth']
            user_email = dic['user_email']
            user_phone = dic['user_phone']
            user_job = dic['user_job']

            outer_user_SSN = user_SSN 

            return render_template('user.html',
            user_SSN = user_SSN,user_name = user_name,user_address = user_address, 
            user_birth = user_birth, user_email = user_email,user_phone = user_phone,user_job = user_job)

    return render_template('user.html')

@app.route('/user/update', methods=["POST","GET"])
def user_info_update():
    global outer_user_SSN 
    mysql_connection = get_MySQLConnection()
    mysql_cursor = mysql_connection.cursor(dictionary=True)

    user_address_info = request.form.get('get_address') # 내 정보 확인 
    user_job_info = request.form.get('get_job')

    if request.method == "POST":   
        data = (user_address_info, user_job_info, outer_user_SSN)
        sql = """update user set user_address=%s, user_job=%s where user_SSN= %s; commit;"""
        mysql_cursor.execute(sql, (data))

        data2 = (outer_user_SSN)
        sql = """select * from user where user_SSN = %s;"""
        mysql_cursor.execute(sql, (data2,))
        for row in mysql_cursor:
            dic = row 
            break 
        
        if len(dic) > 0:
            user_SSN = dic['user_SSN']
            user_name = dic['user_name']
            user_address = dic['user_address']
            user_birth = dic['user_birth']
            user_email = dic['user_email']
            user_phone = dic['user_phone']
            user_job = dic['user_job']
            return render_template('user.html',
            user_SSN = user_SSN,user_name = user_name,user_address = user_address, 
            user_birth = user_birth, user_email = user_email,user_phone = user_phone,user_job = user_job)

    return render_template('user.html')


@app.route('/card', methods=["POST","GET"])
def card_info():
    mysql_connection = get_MySQLConnection()
    mysql_cursor = mysql_connection.cursor(dictionary=True)

    get_my_card_limit_by_user_SSN = request.form.get('get_my_card_limit_by_user_SSN') # 내 카드 한도 확인 
    if request.method == "POST":   
        data = (get_my_card_limit_by_user_SSN,get_my_card_limit_by_user_SSN)
        sql = """select c.card_limit, u.user_name from card c, user u where c.card_user_SSN = %s and u.user_SSN=%s;"""
        mysql_cursor.execute(sql, (data))
        for row in mysql_cursor:
            dic = row 
            break 
        if len(dic) > 0: 
            card_limit = dic['card_limit']
            card_limit_user = dic['user_name']
            return render_template('card.html', card_limit = card_limit, card_limit_user = card_limit_user)
        
    return render_template('card.html')

global_account_user_SSN = ''
global_account_left=0
@app.route('/account', methods=["POST","GET"])
def account_info():
    global global_account_user_SSN
    global global_account_left

    mysql_connection = get_MySQLConnection()
    mysql_cursor = mysql_connection.cursor(dictionary=True)
    account_info_by_SSN = request.form.get('get_account_info_by_SSN') # 내 계좌정보 확인

    global_account_user_SSN = account_info_by_SSN 
    if request.method == "POST":
        data = (account_info_by_SSN)
        print("sql ready")
        sql = """select 
        a.account_user_name, a.account_user_phone, a.account_user_email, ar.account_class, ar.account_content, ar.record_amount, ar.account_left
        from user_account a, account_record ar 
        where a.account_user_SSN = %s and a.account_id = ar.account_id;"""


        mysql_cursor.execute(sql, (data, ))
        print("sql success")
        for row in mysql_cursor:
            dic = row
            print(row)
            break 
        if len(dic) > 0: 
            account_user_name = dic['account_user_name']
            account_user_phone = dic['account_user_phone']
            account_user_email = dic['account_user_email']
            account_class = dic['account_class']
            account_content = dic['account_content']
            record_amount = dic['record_amount']
            account_left = dic['account_left']
            global_account_left = account_left
            return render_template('account.html',
            account_user_name = account_user_name, account_user_phone = account_user_phone
            ,account_user_email=account_user_email,account_class=account_class,
            account_content=account_content,record_amount=record_amount,account_left =account_left )

    return render_template('account.html')

i = 100 
@app.route('/account_record/deposit', methods=["POST","GET"])
def account_record_info_deposit():
    global global_account_left 
    global i 
    mysql_connection = get_MySQLConnection()
    mysql_cursor = mysql_connection.cursor(dictionary=True)
    account_record_class = request.form.get('get_account_record_class') # 내 거래 기록 확인 
    account_record_content = request.form.get('get_account_record_content') # 내 거래 기록 확인
    account_record_amount = request.form.get('get_account_record_amount') # 내 거래 기록 확인
    now = str(datetime.datetime.now())  

    if request.method == "POST":
        data = (global_account_user_SSN)
        sql = "select account_id from user_account where account_user_SSN= %s;"
        mysql_cursor.execute(sql, (data, ))
        for row in mysql_cursor:
            dic = row
            print(row)
            break 
        if len(dic) > 0:
            account_id = dic['account_id']
            account_left = int(global_account_left) + int(account_record_amount)
            i += 1
            data2 = (account_id, now, i, account_record_class, account_record_content, account_record_amount, account_left)
            print("sql ready")
            sql = """insert into account_record(account_id, banking_date, record_number, account_class, account_content, record_amount, account_left)
                    values(%s, %s, %s, %s, %s, %s, %s);"""
            mysql_cursor.execute(sql, (data2))

            print("update account_left")
            data3 = (account_left, account_id)
            sql2 = """update user_account set account_left=%s where account_id= %s; commit;"""
            mysql_cursor.execute(sql2, (data3))

            print("sql success")
            for row in mysql_cursor:
                dic = row
                print(row)
                break 
            return render_template('account_record.html')
        
    return render_template('account_record.html')

@app.route('/account_record/fetch', methods=["POST","GET"])
def account_record_info_fetch():
    global global_account_left 
    global i 
    mysql_connection = get_MySQLConnection()
    mysql_cursor = mysql_connection.cursor(dictionary=True)
    account_record_class_fecth = request.form.get('get_account_record_class_fecth') # 내 거래 기록 확인 
    account_record_content_fecth = request.form.get('get_account_record_content_fecth') # 내 거래 기록 확인
    account_record_amount_fecth = request.form.get('get_account_record_amount_fecth') # 내 거래 기록 확인
    now = str(datetime.datetime.now())  

    if request.method == "POST":
        data = (global_account_user_SSN)
        sql = "select account_id from user_account where account_user_SSN= %s;"
        mysql_cursor.execute(sql, (data, ))
        for row in mysql_cursor:
            dic = row
            print(row)
            break 
        if len(dic) > 0:
            account_id = dic['account_id']
            account_left = int(global_account_left) - int(account_record_amount_fecth)
            i += 1
            data2 = (account_id, now, i, account_record_class_fecth, account_record_content_fecth, account_record_amount_fecth, account_left)
            print("sql ready")
            sql = """insert into account_record(account_id, banking_date, record_number, account_class, account_content, record_amount, account_left)
                    values(%s, %s, %s, %s, %s, %s, %s); commit;"""
            mysql_cursor.execute(sql, (data2))

            print("sql success")
            for row in mysql_cursor:
                dic = row
                print(row)
                break 
            return render_template('account_record.html')
        
    return render_template('account_record.html')

@app.route('/account_record', methods=["POST","GET"])
def account_record_info():

    mysql_connection = get_MySQLConnection()
    mysql_cursor = mysql_connection.cursor(dictionary=True)

    li = [] 

    if request.method == "POST":
        sql = "select * from account_record;"
        print("select * from account_record; <- ready")
        mysql_cursor.execute(sql)
        print("select * from account_record; <- success")
        for row in mysql_cursor:
            print(row)
            li.append(row)
        if len(li) > 0:
            return render_template('account_record.html',li=li)
        
    return render_template('account_record.html')

if __name__ == "__main__" :
    app.run(host = '127.0.0.1', port = 5000 , debug=True)
