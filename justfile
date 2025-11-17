default:
    @just --list

download_lessons:
    @echo "Pulling latest updates from brendan's repository..."
    @git submodule update --recursive --remote

extract_exercises:
    @echo "Extracting exercises..."
    @python3 PracticeQuestionExtractor.py
