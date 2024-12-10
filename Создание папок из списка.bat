@echo off
setlocal enabledelayedexpansion

REM Проверяем наличие файла file.txt
if not exist file.txt (
    echo Ошибка: файл file.txt не найден.
    pause
    exit /b
)

REM Читаем содержимое файла file.txt
for /f "tokens=*" %%A in (file.txt) do (
    REM Разделяем строку на имена папок
    for %%B in (%%A) do (
        REM Создаем папку
        mkdir "%%B" 2>nul
        
        REM Извлекаем цифры из начала названия
        set "prefix=%%B"
        for /f "tokens=1-3 delims=_" %%C in ("!prefix!") do (
            set "prefix=%%C_%%D"
        )
        
        REM Создаем пустой файл в папке
        type nul > "%%B\!prefix!.py"
    )
)

echo Готово.
pause