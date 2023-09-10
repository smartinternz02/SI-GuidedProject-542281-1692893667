from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def Faculty_Profile():
    if request.method=='POST':
        name=request.form['name']
        qualification=request.form['qualification']
        phone_number=request.form['phone_number']
        branch=request.form['branch']
        specialization=request.form['specialization']
        submitted=True
    
        #Pass the form data to the template
        return render_template('index.html',
                               name=name,
                               qualification=qualification,
                               phone_number=phone_number,
                               branch=branch,
                               specialization=specialization,
                               submitted=submitted
                               )
    
    
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)