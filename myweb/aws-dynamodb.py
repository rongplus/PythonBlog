from flask import Flask, request
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Replace 'your-table-name' with your DynamoDB table name
table = dynamodb.Table('your-table-name')

@app.route('/save', methods=['POST'])
def save_data():
    # Extract data from the request
    data_to_save = request.json
    
    try:
        # Save the data to DynamoDB
        response = table.put_item(Item=data_to_save)
        return f"Data saved successfully: {response}"
    except ClientError as e:
        return f"An error occurred: {e.response['Error']['Message']}"

if __name__ == '__main__':
    app.run(debug=True)
