@echo off
set "targetDir=c:\dev\luanny"
set "outputFile=%targetDir%\file_structure.md"

echo Generating file tree for %targetDir%...

:: Generate the tree and wrap it in a Markdown code block for better rendering
echo # Project Structure > "%outputFile%"
echo. >> "%outputFile%"
echo ``` >> "%outputFile%"
tree "%targetDir%" /f /a >> "%outputFile%"
echo ``` >> "%outputFile%"

echo Done! Results saved to %outputFile%
pause