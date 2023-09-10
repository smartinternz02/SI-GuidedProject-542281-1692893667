from flask import Flask,request,render_template
import os
import ibm_boto3
from ibm_botocore.client import Config, ClientError




app = Flask(__name__)



@app.route('/')
def abc():
    return render_template('abc.html')

@app.route('/result',methods = ['POST'])
def result():
    if request.method=="POST":
       f=request.files['image']
       basepath=os.path.dirname(__file__) #getting the current path i.e where app.py is present
       #print("current path",basepath)
       filepath=os.path.join(basepath,'uploads',f.filename) #from anywhere in the system we can give image but we want that image later  to process so we are saving it to uploads folder for reusing
       #print("upload folder is",filepath)
       f.save(filepath)
       COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints"
       COS_API_KEY_ID = "4a3-wUStAb4f5AEJJcPRwZSOBmQi1RsTFQZT8awhizPS"
       COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/41ee733258814953b400f2e30be703ca:e3c515ec-240e-4b5d-a4b8-7147f6cd9a94::"
       cos = ibm_boto3.client("s3",ibm_api_key_id=COS_API_KEY_ID,ibm_service_instance_id=COS_INSTANCE_CRN, config=Config(signature_version="oauth"),endpoint_url=COS_ENDPOINT)
       print(cos)
       cos.upload_file(Filename= filepath,Bucket='balan',Key='Transformer load test.png')
       
       
    
if __name__== "__main__":
    app.run(debug=False,port = 8080)