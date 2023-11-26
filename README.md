# BroadCastMailer

BroadCastMailer is an automated email-sending tool designed for efficient and personalized outreach campaigns. It's ideal for a variety of purposes, such as job application outreach, marketing campaigns, or networking efforts. This tool simplifies the process of sending bulk emails, making it accessible and convenient for users of all backgrounds.

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
- A Gmail account. For security, use an [App-Specific Password](https://support.google.com/accounts/answer/185833) or enable ['Less Secure Apps'](https://support.google.com/accounts/answer/6010255) (less recommended).

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
   To use your Gmail account for sending emails securely, you need to set your Gmail email and password as environment variables. This approach helps to keep sensitive information secure.

   #### Setting Environment Variables

   - **For Windows Users:**
     - Accessing Environment Variables:
       - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
       - Click on 'Advanced system settings' and navigate to the 'Advanced' tab.
       - Click on 'Environment Variables'.
     - Creating New Variables:
       - Under 'User variables', click 'New'.
       - Set 'Variable name' as `gmail_email` and 'Variable value' as your Gmail address.
       - Repeat the process with `gmail_password` as the 'Variable name' and your Gmail password or app-specific password as the 'Variable value'.

   - **For macOS/Linux Users:**
     - Open Terminal:
       - Applications -> Utilities -> Terminal on macOS, or use your preferred Linux terminal.
     - Define Variables:
       - Type `export gmail_email="your-email@gmail.com"` and `export gmail_password="your-password"`, replacing with your actual Gmail credentials.
     - Persisting Variables:
       - To make these changes permanent, add the `export` commands to your `~/.bashrc`, `~/.zshrc`, or equivalent shell configuration file.

   #### Security Recommendations

   - **App-Specific Password:** If your Gmail account has 2-Step Verification enabled, generate and use an app-specific password.
   - **Less Secure Apps Access:** Enabling 'Less Secure Apps' access is not recommended. Use 2-Step Verification and an app-specific password for enhanced security.

2. **Prepare the Excel File:**
   An Excel file named `Recruiter-emails.xlsx` is included in the project. To use it:
   
   - Open the `Recruiter-emails.xlsx` file located in the project directory.
   - Fill out the columns with the relevant information for each recipient. The columns are:
     - `company`: The name of the company or organization.
     - `email`: The email address of the recipient.
     - `name`: The name of the recipient (or leave blank if unknown).
   - Save your changes to the file before running the script.

3. **Customize Email Template:**
   The `email_template.txt` file in the project directory serves as the template for your emails. To customize it:

   - Open `email_template.txt` in a text editor.
   - Edit the content to suit your message. The template includes placeholders like `{{ recruiter_name }}` and `{{ company_name }}`, which will be automatically replaced by the script with actual values from the Excel file.
   - Feel free to add or modify any part of the email text to personalize your message.
   - Save your changes to the file after editing.
   
   Note: Do not remove the placeholders unless you intend to manually input those details for each email.

4. **Add Your Attachment:**
   For ease of use, the script expects a specific filename for the resume. Please follow these steps to add your resume:

   - Rename your resume file to `My-Resume.pdf` and place it in the project directory.
   - The script is pre-configured to look for a file named `My-Resume.pdf`. Ensure your file's name and format match this expectation.
   
   Alternatively, if you wish to use a different filename, you can modify the script as follows:

   - Place your resume file in the project directory.
   - Open the `coldmail.py` script in a text editor or IDE.
   - Locate the line `resume_path = Path('.', 'My-Resume.pdf')`.
   - Replace `'My-Resume.pdf'` with the actual name of your resume file. For example, if your resume is named `JohnDoe_Resume.pdf`, update the line to `resume_path = Path('.', 'JohnDoe_Resume.pdf')`.


### Usage

1. **Run the Script:**
```
python coldmail.py
```
Upon successful execution, the script will send emails to the recipients listed in `Recruiter-emails.xlsx`. Check the console output for any success or error messages.

2. **Verify Emails:**
- Check the 'Sent' folder in your Gmail account to confirm the emails were sent.

### Troubleshooting

If you encounter any issues while setting up or running BroadCastMailer, check the following:

- Ensure that your environment variables for Gmail credentials are correctly set.
- Verify that the `Recruiter-emails.xlsx` file is properly formatted and saved in the correct directory.
- Make sure that the `email_template.txt` file contains the necessary placeholders.

For further assistance, feel free to open an issue on the [GitHub issues page](https://github.com/Kushal-Shankar-1/BroadCastMailer/issues).

## Contributing

We welcome contributions of all kinds, from bug reports and feature requests to code contributions. Please feel free to check our [issues page](https://github.com/Kushal-Shankar-1/BroadCastMailer/issues) for existing issues or to open a new one.

## Contact

For support or queries regarding BroadCastMailer, reach out via [GitHub](https://github.com/Kushal-Shankar-1) or email me at [kushalshankar03@gmail.com].
## Author

- [@Kushal-Shankar-1](https://github.com/Kushal-Shankar-1)

## License

This project is [MIT licensed](LICENSE).

## Acknowledgments

- Inspired by the Coldmail-script project on GitHub.
