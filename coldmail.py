import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from parse_mails import parse_email_data
from pathlib import Path

def read_email_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()

def send_email(recipient, subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = os.environ["gmail_email"]
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the resume
    with open(attachment_path, 'rb') as attachment_file:
        part = MIMEApplication(attachment_file.read(), Name=os.path.basename(attachment_path))
    part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(attachment_path)
    msg.attach(part)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(os.environ["gmail_email"], os.environ["gmail_password"])
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    email_data = parse_email_data(Path('.', 'Recruiter-emails.xlsx'))
    email_template = read_email_template(Path('.', 'email_template.txt'))
    resume_path = Path('.', 'My-Resume.pdf')  # Replace with your resume file

    for recruiter in email_data:
        recruiter_name = recruiter["name"] if recruiter["name"] else "Hiring Manager"
        company_name = recruiter["company"]
        # Replace placeholders in the template
        email_body = email_template.replace("{{ recruiter_name }}", recruiter_name).replace("{{ company_name }}", company_name)
        subject = f"Interest in DevOps/Cloud Engineer Internship at {company_name}"
        send_email(recruiter["email"], subject, email_body, resume_path)

if __name__ == "__main__":
    main()
