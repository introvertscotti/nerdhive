from flask import Flask, render_template, request, url_for, redirect
# from flask_login import login_manager, login_required, current_user, login
from database import load_jobs, load_job_item, load_applications, post_new_job, save_job_application, get_login_data, load_application_details
from datetime import datetime
from cryptography.fernet import Fernet

app = Flask(__name__)


@app.route('/')
def index():
    jobs_list = load_jobs()
    return render_template('careers.html', jobs=jobs_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check for received method
    if request.method == 'POST':
        # Log Users In
        entered_email = request.form['email']
        entered_password = request.form['password']

        user_data = get_login_data(entered_email)
        if len(user_data) == 0:
            return render_template('auth.html', msg='Email is Incorrect. Try again.')

        encry_key = b'yDCl07tmOonEoOnvG6Rha3k_Bnrh0-OXdCmYZkkOLJg='
        fer = Fernet(encry_key)
        user_password = user_data[0][0].encode()
        user_password = fer.decrypt(user_password).decode()

        if entered_password == user_password:
            return redirect(url_for('admin_panel'))
        else:
            return render_template('auth.html', msg='Password is Incorrect. Try again.')
    else:
        return render_template('auth.html')
    
    
@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_panel():
    jobs = load_jobs()
    applications = load_applications()
    if request.method == 'GET':
        return render_template('admin.html', jobs=jobs, applications=applications)
    elif request.method == 'POST':
        job_title = request.form['job-title']
        company = request.form['company']
        about_company = request.form['about-company']
        company_website = request.form['company-website']
        location = request.form['location']
        if request.form['salary']:
            salary = request.form['salary']
        else:
            salary = ''
        responsibilities = request.form['responsibilities']
        requirements = request.form['requirements']
        close_date = '31 May, 2023'

        new_job = (job_title,company,location,about_company,company_website,salary,responsibilities,requirements,close_date)
        job_post_msg = post_new_job(new_job)

        return render_template('admin.html', jobs=jobs, applications=applications, msg=job_post_msg)


@app.route('/<application_id>/review')
def review_application(application_id):
    application_details = load_application_details(application_id)

    return render_template('review-application.html', details=application_details)


@app.route('/jobs/<job_id>', methods=['GET', 'POST'])
def load_job_page(job_id):
    if request.method == 'GET':
        details = load_job_item(job_id)
        return render_template('jobitem.html', details=details)
    if request.method == 'POST':
        applied_job_id = job_id
        fullname = request.form['fullname']
        email = request.form['email']
        if request.form['linkdin']:
            linkedin_url = request.form['linkdin']
        else:
            linkedin_url = ''
        resume_url = request.form['resume-url']
        education_bg = request.form['education']
        work_exp = request.form['work-exp']

        application_details = (applied_job_id,fullname,email,linkedin_url,education_bg,work_exp,resume_url, f'{datetime.now()}'.split(' ')[0])
        return render_template(save_job_application(application_details), applicant=application_details[1])
