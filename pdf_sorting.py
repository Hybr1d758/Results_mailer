import os

# Folder containing PDFs
pdf_folder = "results/"

# Check if all PDFs exist
data = {'Result_ID': [1, 2, 3, 4]}  # data, replace with actual data source
missing_files = []
for result_id in data['Result_ID']:
    file_path = os.path.join(pdf_folder, f"{result_id}.pdf")
    if not os.path.exists(file_path):
        missing_files.append(result_id)

if missing_files:
    print(f"Missing PDFs: {missing_files}")
else:
    print("All PDFs are ready!")


