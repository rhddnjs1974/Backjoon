@echo off

echo ============================
echo   Git Push Script
echo ============================

set /p msg=Commit message 입력: 

if "%msg%"=="" (
    echo 커밋 메시지를 입력해야 합니다.
    pause
    exit
)

git add *
git commit -m "%msg%"
git push origin master

pause
