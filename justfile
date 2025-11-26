set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]
default:
    @just --list

run:
    just cleanup download_lessons extract_exercises

download_lessons:
    @echo "Pulling latest updates from brendan's repository..."
    @git pull --recurse-submodules

[unix]
extract_exercises:
    @echo "Extracting exercises..."
    @python3 PracticeQuestionExtractor.py

[windows]
extract_exercises:
    @echo "Extracting exercises..."
    @python PracticeQuestionExtractor.py

[unix]
cleanup:
    @echo "Cleaning up code..."
    @rm -rf extracted_java

[windows]
cleanup:
    @echo "Cleaning up code..."
    @powershell -NoLogo -NoProfile -Command "if (Test-Path 'extracted_java') { Remove-Item -Recurse -Force 'extracted_java' }"
