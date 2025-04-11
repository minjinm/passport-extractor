import boto3
import pymysql

def upload_to_s3(image_path, myfirstbucket00282905, object_name):
    s3 = boto3.client('s3')
    s3.upload_file(image_path, myfirstbucket00282905, object_name)
    return f"s3://{myfirstbucket00282905}/{object_name}"

def insert_to_aurora(data, connection_params):
    conn = pymysql.connect(**connection_params)
    with conn.cursor() as cursor:
        sql = "INSERT INTO passports (name, passport_number) VALUES (%s, %s)"
        cursor.execute(sql, (data["Name"], data["Passport_Number"]))
    conn.commit()
    conn.close()
