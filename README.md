# Text-to-speech

This script reads a PDF file and stores its contents as string to send  HTTP requests to Voicerss API (https://www.voicerss.org) and receive a response with audio data (Voicerss text-to-speech service).

The maximum amount of characters workable is about (arbitrarily) 1000 characters, so the text is split into chunks that are requested from the API one by one until the full original text is rendered as speech.

The dependencies are to be found in the `requirements.txt` file.

## How tu run

Run the script giving the arguments in this order: path to pdf file and language of the file as follows:
`python main.py path_to_file file_language`

The latter argument is optional.
