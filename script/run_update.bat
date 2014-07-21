set "mongo_path=C:\mongodb\bin"
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%cd%\usertype.js"
pause
