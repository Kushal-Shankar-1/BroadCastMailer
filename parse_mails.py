import openpyxl
from pathlib import Path

def parse_email_data(file_path):
    try:
        wb_obj = openpyxl.load_workbook(file_path)
        sheet = wb_obj.active

        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming first row is headers
            if row[0] and row[1]:  # Ensure company name and email are present
                name = row[2] if row[2] else None
                data.append({"company": row[0], "email": row[1], "name": name})
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Example Usage
# email_data = parse_email_data(Path('.', 'Recruiter-emails.xlsx'))
