import boto3
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME: str = "aws-s3-cil"


def backup_files(bucket: str) -> None:
    num_backed_up = 0
    Objects: dict = s3.list_objects_v2(Bucket=BUCKET_NAME, MaxKey=1000)
    for Object in Objects["Content"]:
        try:
            obj: dict = s3.get_object(Bucket=BUCKET_NAME, Key=Object["Key"])
        except Exception as error:
            continue
        with open(f"myS3backup/{Object['Key']}", 'wb') as file:
            file.write(obj["Body"].read())

        num_backed_up += 1

    print(f"[INFO]\tBackup complete.\n[INFO]\tNumber of files backup up today ({datetime.today().date()}): {num_backed_up} files.")


if __name__ == "__main__":
    backup_files(bucket=BUCKET_NAME)
