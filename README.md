# BroadCastMailer

BroadCastMailer is an automated email sending tool designed for efficient and personalized outreach campaigns. Ideal for various purposes, it offers a streamlined approach to sending emails, managing recipient lists, and customizing content, suitable for users from diverse backgrounds.

## Features

- Automated email sending from a Gmail account.
- Recipient list management through an Excel file.
- Customizable email template for personalized messages.
- Support for attaching files, like resumes or brochures, to emails.

## Getting Started

Follow these instructions to set up and run BroadCastMailer for your email outreach.

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- A Gmail account with 'Less Secure Apps' enabled or an App-Specific Password

### Installation

1. **Clone the Repository:**
```
git clone https://github.com/[YourGitHubUsername]/BroadCastMailer.git
cd BroadCastMailer
```

2. **Install Dependencies:**
```
pip install openpyxl
```

### Setup

1. **Configure Gmail:**
- Set `gmail_email` and `gmail_password` as environment variables.

2. **Prepare the Excel File:**
- Create `Recruiter-emails.xlsx` with the columns: 'company', 'email', and 'name'.

3. **Customize Email Template:**
- Modify `email_template.txt` for your email content.

4. **Add Your Attachment:**
- Place the file to be attached in the project directory.

### Usage

1. **Run the Script:**
```
python coldmail.py
```

2. **Verify Emails:**
- Check the 'Sent' folder in your Gmail.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/Kushal-Shankar-1/BroadCastMailer/issues) if you want to contribute.

## Author

- [@Kushal-Shankar-1](https://github.com/Kushal-Shankar-1)

## License

This project is [MIT licensed](LICENSE).

## Acknowledgments

- Inspired by the Coldmail-script project on GitHub.
