import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # For Gmail
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"

# Create the email sender function
def send_email(recipient_email, recipient_name, pdf_path):
    try:
        # Email content
        subject = "Your Test Results"
        body = f"Dear {recipient_name},\n\nPlease find attached your test results.\n\nBest regards,\nYour Company"
        
        # Setup the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach the PDF
        with open(pdf_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(pdf_path)}",
            )
            msg.attach(part)
        
        # Connect to email server and send
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_name} ({recipient_email})")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Iterate through the data and send emails
for index, row in data.iterrows():
    pdf_path = os.path.join(pdf_folder, f"{row['Result_ID']}.pdf")
    send_email(row['Email'], row['Name'], pdf_path)
