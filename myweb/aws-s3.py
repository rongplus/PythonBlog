from flask import Flask, request
import boto3

app = Flask(__name__)

# Initialize the S3 client
s3_client = boto3.client('s3')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the file from the POST request
    file = request.files['file']
    filename = file.filename
    
    # Save the file to S3
    s3_client.upload_fileobj(file, 'your-bucket-name', filename)
    
    return f'File {filename} uploaded to S3 successfully.'

if __name__ == '__main__':
    app.run(debug=True)
