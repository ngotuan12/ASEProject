rem set "mongo_path=C:\data\db\mongo"
rem set mongo_path = "D:\App\mongodb\bin\mongo.exe"
set "mongo_path=C:\data\db"
call "%mongo_path%\mongo.exe" 127.0.0.1/my_db "%cd%\usertype.js"
pause
call "%mongo_path%\mongo.exe" 127.0.0.1/my_db "%cd%\workfeild.js"
pause
call "%mongo_path%\mongo.exe" 127.0.0.1/my_db "%cd%\jobtitle.js"
pause
call "%mongo_path%\mongo.exe" 127.0.0.1/my_db "%cd%\userprofile.js"
pause
call "%mongo_path%\mongo.exe" 127.0.0.1/my_db "%cd%\mentorpost.js"
pause
call "%mongo_path%\mongo.exe" 127.0.0.1/my_db "%cd%\commentpost.js"