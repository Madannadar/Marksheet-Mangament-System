from win32com import client
import os
import win32com

def word_pdf(file_location):
    wrd = client.Dispatch("Word.Application")
    wrd.Visible = False
    doc = wrd.Documents.Open(file_location)
    output = os.path.splitext(file_location)[0]
    doc. SaveAs(output, FileFormat=17)
    doc. Close()

def excel_pdf(file_location):
    app = client.DispatchEx("Excel.Application")
    app. Interactive = False
    app.Visible = False

    workbook = app.Workbooks.open(file_location)
    output = os.path.splitext(file_location)[0]

    workbook. ActiveSheet. ExportAsFixedFormat(0, output)
    workbook. Close()

excel_pdf('C:/sAIML-SEM3.exc')
word_pdf('C:/sAIML-SEM3.exc')