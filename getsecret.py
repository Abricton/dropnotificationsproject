import boto3
import base64


def get_secret():

    secret_name = "vscrap22/password"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )


    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except:
        print("Error retrieving secret value: " + get_secret_value_response)