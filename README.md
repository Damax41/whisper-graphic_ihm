# Whisper Graphic IHM v1.1.0

> **Damax41** - *Développeur* - [Link](https://github.com/Damax41)

## Overview

Whisper Graphic IHM is a user-friendly application that allows you to transcribe audio files using the Whisper Automatic Speech Recognition (ASR) models. This application provides a simple graphical user interface to select audio files and the desired transcription model. The transcriptions can be viewed within the app and saved to a text file.

## New in v1.1.0

- **Updated Retranscript class :** The `Retranscript` class has been updated for better code structure and more control over the transcription process.

- **Direct transcription method :** The Whisper model's direct transcription method is now used for transcribing audio files.

- **Improved user interface :** Users can now select an audio file and a transcription model from the main menu. A progress bar has been added to show the transcription process, and a results view has been added to display the transcription and offer options to save the transcription or return to the main menu.

- **Better error handling :** Error messages are now displayed to the user in a more user-friendly way.

- **Multithreading support :** The transcription process now runs in a separate thread to prevent blocking the GUI. This change was facilitated by the introduction of a new Monitor class.

## Installation

1. Clone the repository :

```bash
git clone https://github.com/Damax41/whisper-graphic_ihm.git whisper-graphic_ihm
```

2. Change to the app directory :

```bash
cd whisper-graphic_ihm
```

3. Install the required packages :

```bash
pip install -r requirements.txt
```

## Usage

Run the main script :

```bash
python (or python3) "Whisper (Graphical version).py"
```

This will open the Whisper Transcription App GUI. From here, you can:

1. Select an audio file by clicking on "Choose an audio file".

2. Select a transcription model from the dropdown menu.

3. Click "Retranscript" to start the transcription process.

4. Once the transcription is complete, you can view the results, save them to a text file, or return to the main menu to start a new transcription.

## Version History

-v1.1.1 (current)
- v1.1.0
- v1.0.2(initial release)

## Support

For support or to report bugs, please submit an issue on the GitHub repository.

## Contributing

Pull requests are welcome. Please open an issue to discuss any changes you would like to make.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Damax41/whisper-graphic_ihm/blob/main/license) file for details.

> Please note: This application uses the Whisper ASR models, which are developed and maintained by OpenAI.
