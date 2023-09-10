from flask import Flask,render_template,request

registration=Flask(__name__)

@registration.route('/',methods=['GET','POST'])

def student_assignment_registration_form():
    if request.method=='POST':
        name_of_the_student=request.form['name_of_the_student']
        section=request.form['section']
        phone_number=request.form['phone_number']
        registration_number=request.form['registration_number']
        course_name=request.form['course_name']
        submitted=True
    
        #Pass the form data to the template
        return render_template('Front.html',
                               name_of_the_student=name_of_the_student,
                               section=section,
                               phone_number=phone_number,
                               registration_number=registration_number,
                               course_name=course_name,
                               submitted=submitted
                               )
        return render_template('Front.html')

if __name__=='__main__':
    registration.run(debug=True)