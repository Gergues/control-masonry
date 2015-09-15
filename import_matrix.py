from openpyxl import load_workbook
# from yaml import dump
from json import dump


def load_worksheet(file_name):
    """ Open a xlsx workbook and open the first worksheet """
    workbook = load_workbook(file_name)
    return workbook.get_active_sheet()


def parse_worksheet(worksheet):
    """ Convert worksheet into dictionary """
    controls = dict()
    for row in worksheet.rows[1:]:
        control_id = row[0].value
        control_title = row[1].value
        paas_description = row[-2].value
        laas_description = row[-1].value
        controls[control_id] = {
            'control_title': control_title,
            'paas_description': paas_description,
            'laas_description': laas_description
        }
    return controls


def export_yaml(data):
    """ Export Dict data in yaml format """
    with open('data.yml', 'w') as outfile:
        dump(data, outfile)


if __name__ == '__main__':
    worksheet = load_worksheet(file_name='FedRampMatrix.xlsx')
    controls_data = parse_worksheet(worksheet=worksheet)
    print(controls_data)
    export_yaml(controls_data)
