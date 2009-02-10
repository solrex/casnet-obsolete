xcopy /YS ..\..\src\* .
python setup_4_py2exe.py py2exe
makensis.exe casnet.nsi
