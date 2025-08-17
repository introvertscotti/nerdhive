import sqlite3 as sql

def load_jobs():
    with sql.connect('nerdhive.sqlite') as conn:
        cursor = conn.cursor()
        results = cursor.execute('SELECT * FROM jobs').fetchall()
        jobs = []
        for job in results:
            job = {'id': job[0], 'title':job[1], 'company': job[2],  'location': job[3], 'about_company': job[4], 'company_website': job[5], 'responsibilities': job[6], 'requirements': job[7],  'salary': job[8], 'currency': job[9], 'open_until': job[10],  }
            jobs.append(job)

    return jobs

def load_applications():
    with sql.connect('nerdhive.sqlite') as conn:
        cursor = conn.cursor()
        results = cursor.execute('SELECT * FROM applications').fetchall()
        applications = []
        for application in results:
            applied_job = cursor.execute(f'SELECT * FROM jobs WHERE id = {application[1]}').fetchall()
            application = {'id': application[0], 'job_title':applied_job[0][1], 'fullname': application[2], 'salary': application[3], 'currency': application[4]}
            applications.append(application)

    return applications


def load_job_item(job_id):
    with sql.connect('nerdhive.sqlite') as conn:
        cursor = conn.cursor()
        job = cursor.execute(f'SELECT * FROM jobs WHERE id = {job_id}').fetchall()
        job = job[0]
        job = {'id': job[0], 'title':job[1], 'company': job[2], 'location': job[3], 'about_company': job[4], 'company_website': job[5], 'responsibilities': job[6], 'requirements': job[7], 'salary': job[8], 'currency': job[9], 'open_until': job[10]}

    return job

def post_new_job(job_details):
    with sql.connect('nerdhive.sqlite') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO jobs (title,company,location,about_company,company_website,salary,responsibilities,requirements,open_until) VALUES (?,?,?,?,?,?,?,?,?)', job_details)
        conn.commit()

    return 'New Job Successfully Posted'

def save_job_application(application_details):
    with sql.connect('nerdhive.sqlite') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO applications (job_id,fullname,email,linkedin_url,education_bg,work_exp,resume_url,sent_on) VALUES (?,?,?,?,?,?,?,?)', application_details)
        conn.commit()

    return 'job-applied.html'


def get_login_data(email):
    with sql.connect('nerdhive.sqlite') as conn:
            cursor = conn.cursor()
            user_data = cursor.execute(f'SELECT password, user_role FROM users WHERE email="{email}"').fetchall()

    return user_data


def load_application_details(application_id):
    with sql.connect('nerdhive.sqlite') as conn:
            cursor = conn.cursor()
            application_data = cursor.execute(f'SELECT * FROM applications WHERE id="{application_id}"').fetchall()
            for application in application_data:
                applied_job = cursor.execute(f'SELECT * FROM jobs WHERE id = {application[1]}').fetchall()
                appl = {'id': application[0], 'job_title':applied_job[0][1], 'fullname': application[2], 'email': application[3], 'linkedin_url': application[4], 'education_bg': application[5], 'work_exp': application[6], 'resume_url': application[7], 'sent_on': application[8]}

    return appl