import xlrd,xlwt
from openpyxl import Workbook,load_workbook
from xlutils.copy import copy
from kpi.models import Themetics,Userslist,Indicators


""" Writing  a xlsv file  through importing a data from themetic model"""

def Themetics_xlsx(path):
    themetic=Themetics.objects.all()
    xls_file=xlrd.open_workbook(path)
    total_sheets = xls_file.nsheets
    wb=copy(xls_file)
    worksheet_data=wb.add_sheet("list_of_themetics")
    worksheet_data.write(0,0,"Themetic Id")
    worksheet_data.write(0,1,"Active")
    worksheet_data.write(0,2,"Themetic Name")
    worksheet_data.write(0,3,"Themetic Code")
    for i in range(len(themetic)):
        worksheet_data.write(i+1,0,themetic[i].id)
        worksheet_data.write(i+1,1,themetic[i].active)
        worksheet_data.write(i+1,2,themetic[i].themeticname )
        worksheet_data.write(i+1,3,themetic[i].code )
    wb.save("/home/mahiti/Desktop/themetics.xlsx")
path="/home/mahiti/Desktop/themetics.xlsx"





"""exporting a xlsx file's data into a database"""


def exporting_userdata(path2):
    wb=xlrd.open_workbook(path2)
    sheet=wb.sheet_by_index(1)
    data_length=sheet.nrows
    for i in range(1,data_length):
        user=sheet.row_values(i,0)
        Userslist.objects.create(user=user[0],username=user[1],firstname=user[2],lastname=user[3],roleid=user[4],roletype=user[5])
path2="/home/mahiti/Desktop/user_data.xlsx"



""" Exporting a data from model Indicators to a xlsx sheet """


def indicators_xlsx(path3):
    #create a workbook
    wb=Workbook()
    ws=wb.active
    ws.title="Indicators Data"
    wb.save(path3)

    #opening a saved workbook
    wb=load_workbook(path3)
    ws=wb.active
    column_name=("id","active","created","modified","indicatorname","shortcode","themetic id")
    ws.append(column_name)
    wb.save(path3)
    Indicator_list=Indicators.objects.all()

    for i in Indicator_list:
        row_data=(i.id , i.active, i.created , i.modified , i.indicatorname,i.shortcode ,i.themetic_id)
        ws.append(row_data)
        wb.save(path3)
path3="/home/mahiti/Desktop/indicator.xlsx"
indicators_xlsx(path3)


