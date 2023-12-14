:ProcessHTML
echo.
echo Processing HTML files:
cd C:\Users\Fireb\personality_test\traits\templates\traits
for /r %%i in (*.html) do (
    echo %%i | find /I "venv" > nul || (
        type "%%i"
    )
)
cd C:\Users\Fireb\personality_test


