default:
    @just --list

run:
    just cleanup download_lessons extract_exercises

download_lessons:
    @echo "Pulling latest updates from brendan's repository..."
    @git submodule update --recursive --remote

extract_exercises:
    @echo "Extracting exercises..."
    @python3 PracticeQuestionExtractor.py


cleanup:
    @echo "Cleaning up code..."
    @rm -r extracted_java
