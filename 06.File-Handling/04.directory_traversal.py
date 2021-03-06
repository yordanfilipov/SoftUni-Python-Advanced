import os


def extract_files(dir):
    return [el for el in dir if os.path.isfile(el)]


def get_report_for_files_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_files_extensions(files)

result_str = ""
for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result_str += f".{extension}\n"
    for name in file_names:
        result_str += f"- - - {name}.{extension}\n"

with open("C:\\Users\\yordan\\Desktop\\my_report_result.txt", "w") as file:
    file.write(result_str)