from xlrd import open_workbook


def read_locators(sheetname):
    wb = open_workbook("C:/Users/Rudra/PycharmProjects/V_Tiger/Data/objects.xls")
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    data = {}
    for i in range(1,used_rows):
        rows = ws.row_values(i)
        data[rows[0]] = (rows[1], rows[2])
    return data


# print(read_locators("login"))

def read_headers(test_case_name,sheetname):
    wb = open_workbook("C:/Users/Rudra/PycharmProjects/V_Tiger/Data/testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    for i in range(0,used_rows):
        rows = ws.row_values(i)
        if rows[0] == test_case_name:
            row = ws.row_values(i-1)
            return ",".join(row[1:])

# print(read_headers("test_add_lead","addleads"))




def read_data(test_case_name,sheetname):
    wb = open_workbook("C:/Users/Rudra/PycharmProjects/V_Tiger/Data/testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    data = []
    for i in range(1,used_rows):
        rows = ws.row_values(i)
        # print(rows)
        if test_case_name == rows[0]:
            data.append(tuple(rows[1:]))
    return data


# print(read_data("test_add_lead","addleads"))




