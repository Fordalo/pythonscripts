from itertools import count
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import gspread


gauth = GoogleAuth()
drive = GoogleDrive(gauth)
gc = gspread.service_account(filename= '/Users/admin/Desktop/python scripts/project2/service_account.json' )


folder = '1_6xDE5HJtUdlr9Tmr36ASot2vvLzY8LP'
urlLink_base = 'https://drive.google.com/file/d/'
directory = "/Users/admin/Desktop/python scripts/project2/pdffiles"
spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/15FuibFh0Eu-A16E7O9jTyGT3YVZ3Dn9nlqaOQEJ8Shw/edit#gid=0')
worksheet = spreadsheet.get_worksheet(0)

#for i in os.listdir(directory):
#    filepath = os.path.join(directory, i)
#    print(filepath)
#    gfile = drive.CreateFile({'parents' :  [{ 'id' : folder}], 'title' : i})
#    gfile.SetContentFile(filepath)
#    gfile.Upload()



gfile_name = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false" }).GetList()
for file in gfile_name:
    
    count1 = 1
    currentrow = 'A' 
    finalurl = urlLink_base + file['id'] + '/view'
    print(file['id'])
    print(finalurl)
    
    worksheet.update('A1', finalurl)
    count1 = count1 + 1
    