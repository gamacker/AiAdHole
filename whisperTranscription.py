import os
import whisper

# Load Whisper model
model = whisper.load_model("large.en")  # You can use "small", "medium", or "large" for better accuracy

# Folder containing MP3 files
output_folder = "ProcessedPodcasts"
input_folder= "rawPodcasts"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through all MP3 files in the folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".mp3"):
        file_path = os.path.join(input_folder, file_name)
        print(f"Transcribing: {file_name}")

        # Transcribe the file
        result = model.transcribe(file_path)

        # Save transcription to a text file
        transcription_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_transcription.txt")
        with open(transcription_file, "w") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{start:.2f} - {end:.2f}] {text}\n")

        print(f"Transcription saved to: {transcription_file}")
