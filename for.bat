@echo on
cd C:\Users\Fireb\personality_test

echo Processing Python files:
for /r %%i in (*.py) do (
    echo %%i | find /I "venv" > nul || (
        echo %%i | find /I "migrations" > nul && (
            echo Exiting Python file processing as "migrations" directory found.
            goto ProcessHTML
        ) || (
            findstr /V /C:"migrations" "%%i" > nul && (
                type "%%i"
            )
        )
    )
)

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