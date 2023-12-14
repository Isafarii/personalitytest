cd C:\Users\Fireb\personality_test
cd C:\Users\Fireb\personality_test\traits
echo.
echo Processing Python files:
for /R %%i in (*.py) do (
    echo %%i | find /I "venv" > nul || (
        type "%%i"
    )
)
cd C:\Users\Fireb\personality_test