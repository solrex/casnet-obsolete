mkdir casnet
xcopy /YS ..\..\src\* casnet\
copy /Y ..\..\*.txt casnet\
move casnet\casnet-gui.py casnet\casnet-gui.pyw
7z a casnet.zip casnet
copy /Y setup_4_py2exe.py casnet
copy /Y casnet.nsi casnet
cd casnet
python setup_4_py2exe.py py2exe
echo "�뽫 GTK ��� etc, lib, share ������ casnet\dist ��"
pause
makensis.exe casnet.nsi
move casnet_setup.exe ..\
cd ..
::rmdir /S /Q casnet
echo "���"
pause
