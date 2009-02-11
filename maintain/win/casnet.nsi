; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "CASNET"
!define PRODUCT_VERSION "1.3"
!define PRODUCT_PUBLISHER "Solrex Yang"
!define PRODUCT_WEB_SITE "http://share.solrex.cn/casnet/"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\casnet-gui.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor bzip2

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; Language Selection Dialog Settings
!define MUI_LANGDLL_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_LANGDLL_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_LANGDLL_REGISTRY_VALUENAME "NSIS:Language"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!insertmacro MUI_PAGE_LICENSE "licence.txt"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\casnet-gui.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "SimpChinese"

; Reserve files
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "casnet_setup.exe"
InstallDir "$PROGRAMFILES\casnet"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Function .onInit
  !insertmacro MUI_LANGDLL_DISPLAY
FunctionEnd

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite try
  File "dist\atk.pyd"
  File "dist\bz2.pyd"
  File "dist\cairo._cairo.pyd"
  File "dist\casnet-gui.exe"
  CreateDirectory "$SMPROGRAMS\casnet"
  CreateShortCut "$SMPROGRAMS\casnet\CASNET.lnk" "$INSTDIR\casnet-gui.exe"
  CreateShortCut "$DESKTOP\CASNET.lnk" "$INSTDIR\casnet-gui.exe"
  SetOutPath "$INSTDIR\etc\gtk-2.0"
  File "dist\etc\gtk-2.0\gdk-pixbuf.loaders"
  File "dist\etc\gtk-2.0\gtkrc"
  SetOutPath "$INSTDIR\etc\pango"
  File "dist\etc\pango\pango.modules"
  SetOutPath "$INSTDIR"
  File "dist\gobject._gobject.pyd"
  File "dist\gtk._gtk.pyd"
  File "dist\iconv.dll"
  File "dist\intl.dll"
  SetOutPath "$INSTDIR\lib\gtk-2.0\2.10.0\engines"
  File "dist\lib\gtk-2.0\2.10.0\engines\libwimp.dll"
  SetOutPath "$INSTDIR\lib\gtk-2.0\2.10.0\loaders"
  File "dist\lib\gtk-2.0\2.10.0\loaders\libpixbufloader-png.dll"
  SetOutPath "$INSTDIR\lib\pango\1.6.0\modules"
  File "dist\lib\pango\1.6.0\modules\pango-basic-win32.dll"
  SetOutPath "$INSTDIR"
  File "dist\libatk-1.0-0.dll"
  File "dist\libcairo-2.dll"
  File "dist\libfontconfig-1.dll"
  File "dist\libfreetype-6.dll"
  File "dist\libgdk-win32-2.0-0.dll"
  File "dist\libgdk_pixbuf-2.0-0.dll"
  File "dist\libglib-2.0-0.dll"
  File "dist\libgmodule-2.0-0.dll"
  File "dist\libgobject-2.0-0.dll"
  File "dist\libgthread-2.0-0.dll"
  File "dist\libgtk-win32-2.0-0.dll"
  File "dist\libpango-1.0-0.dll"
  File "dist\libpangocairo-1.0-0.dll"
  File "dist\libpangoft2-1.0-0.dll"
  File "dist\libpangowin32-1.0-0.dll"
  File "dist\libpng12.dll"
  File "dist\library.zip"
  File "dist\libxml2.dll"
  File "dist\pango.pyd"
  File "dist\pangocairo.pyd"
  SetOutPath "$INSTDIR\pics"
  File "pics\casnet.ico"
  File "pics\casnet.png"
  File "pics\offline.png"
  File "pics\online.png"
  SetOutPath "$INSTDIR"
  File "dist\python25.dll"
  SetOutPath "$INSTDIR\share\themes\MS-Windows\gtk-2.0"
  File "dist\share\themes\MS-Windows\gtk-2.0\gtkrc"
  SetOutPath "$INSTDIR"
  File "dist\zlib1.dll"
  File "dist\_socket.pyd"
  File "dist\_ssl.pyd"
SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\casnet\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\casnet\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\casnet-gui.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\casnet-gui.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从你的计算机移除。"
FunctionEnd

Function un.onInit
!insertmacro MUI_UNGETLANGUAGE
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "你确实要完全移除 $(^Name) ，其及所有的组件？" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\_ssl.pyd"
  Delete "$INSTDIR\_socket.pyd"
  Delete "$INSTDIR\zlib1.dll"
  Delete "$INSTDIR\w9xpopen.exe"
  Delete "$INSTDIR\unicodedata.pyd"
  Delete "$INSTDIR\share\themes\MS-Windows\gtk-2.0\gtkrc"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\python25.dll"
  Delete "$INSTDIR\pics\online.png"
  Delete "$INSTDIR\pics\offline.png"
  Delete "$INSTDIR\pics\casnet.png"
  Delete "$INSTDIR\pics\casnet.ico"
  Delete "$INSTDIR\pangocairo.pyd"
  Delete "$INSTDIR\pango.pyd"
  Delete "$INSTDIR\libxml2.dll"
  Delete "$INSTDIR\library.zip"
  Delete "$INSTDIR\libpng12.dll"
  Delete "$INSTDIR\libpangowin32-1.0-0.dll"
  Delete "$INSTDIR\libpangoft2-1.0-0.dll"
  Delete "$INSTDIR\libpangocairo-1.0-0.dll"
  Delete "$INSTDIR\libpango-1.0-0.dll"
  Delete "$INSTDIR\libgtk-win32-2.0-0.dll"
  Delete "$INSTDIR\libgthread-2.0-0.dll"
  Delete "$INSTDIR\libgobject-2.0-0.dll"
  Delete "$INSTDIR\libgmodule-2.0-0.dll"
  Delete "$INSTDIR\libglib-2.0-0.dll"
  Delete "$INSTDIR\libgdk_pixbuf-2.0-0.dll"
  Delete "$INSTDIR\libgdk-win32-2.0-0.dll"
  Delete "$INSTDIR\libfreetype-6.dll"
  Delete "$INSTDIR\libfontconfig-1.dll"
  Delete "$INSTDIR\libcairo-2.dll"
  Delete "$INSTDIR\libatk-1.0-0.dll"
  Delete "$INSTDIR\lib\pango\1.6.0\modules\pango-basic-win32.dll"
  Delete "$INSTDIR\lib\gtk-2.0\2.10.0\loaders\libpixbufloader-png.dll"
  Delete "$INSTDIR\lib\gtk-2.0\2.10.0\engines\libwimp.dll"
  Delete "$INSTDIR\intl.dll"
  Delete "$INSTDIR\iconv.dll"
  Delete "$INSTDIR\gtk._gtk.pyd"
  Delete "$INSTDIR\gobject._gobject.pyd"
  Delete "$INSTDIR\etc\pango\pango.modules"
  Delete "$INSTDIR\etc\gtk-2.0\gtkrc"
  Delete "$INSTDIR\etc\gtk-2.0\gdk-pixbuf.loaders"
  Delete "$INSTDIR\casnet-gui.exe"
  Delete "$INSTDIR\cairo._cairo.pyd"
  Delete "$INSTDIR\bz2.pyd"
  Delete "$INSTDIR\atk.pyd"
  Delete "$SMPROGRAMS\casnet\Uninstall.lnk"
  Delete "$SMPROGRAMS\casnet\Website.lnk"
  Delete "$DESKTOP\CASNET.lnk"
  Delete "$SMPROGRAMS\casnet\CASNET.lnk"

  RMDir "$SMPROGRAMS\casnet"
  RMDir "$INSTDIR\share\themes\MS-Windows\gtk-2.0"
  RMDir "$INSTDIR\share\themes\MS-Windows"
  RMDir "$INSTDIR\share\themes"
  RMDir "$INSTDIR\share"
  RMDir "$INSTDIR\pics"
  RMDir "$INSTDIR\lib\pango\1.6.0\modules"
  RMDir "$INSTDIR\lib\pango\1.6.0"
  RMDir "$INSTDIR\lib\pango"
  RMDir "$INSTDIR\lib\gtk-2.0\2.10.0\loaders"
  RMDir "$INSTDIR\lib\gtk-2.0\2.10.0\immodules"
  RMDir "$INSTDIR\lib\gtk-2.0\2.10.0\engines"
  RMDir "$INSTDIR\lib\gtk-2.0\2.10.0"
  RMDir "$INSTDIR\lib\gtk-2.0\"
  RMDir "$INSTDIR\lib"
  RMDir "$INSTDIR\etc\pango"
  RMDir "$INSTDIR\etc\gtk-2.0"
  RMDir "$INSTDIR\etc"
  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd