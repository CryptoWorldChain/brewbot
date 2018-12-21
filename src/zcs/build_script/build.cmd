@echo off
conan install "%~dp0\ska.conan" -pr pr-win-x86_64-release -b missing -b ska -o ska:shared=True -if %~dp0
copy /Y /B "%~dp0\bin\*.dll" "%~dp0\..\"
rmdir /S /Q "%~dp0\bin"
del /S /F conan_imports_manifest.txt
del /S /F conaninfo.txt
del /S /F conanbuildinfo.txt
