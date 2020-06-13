################################################################################
#
# Detect-LectureNotes
#
# File Name: AudioToLectureNotes.py
# Date: 13th June 2020
# Version: 0.1
################################################################################
# IMPORTS
import argparse
import uuid
import dialogflow_v2 as dialogflow
# GLOBAL VARIABLE
session_client = dialogflow.SessionsClient()

# MAIN CODE
def detect_intent_audio(project_id, audio_file_path):
    """Returns the result of detect intent with an audio file as input.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = 16000

    session = session_client.session_path(project_id, str(uuid.uuid4()))
    # print('Session path: {}\n'.format(session))

    with open(audio_file_path, 'rb') as audio_file:
        input_audio = audio_file.read()

    audio_config = dialogflow.types.InputAudioConfig(audio_encoding=audio_encoding, 
    	language_code='en-US',sample_rate_hertz=sample_rate_hertz)
    query_input = dialogflow.types.QueryInput(audio_config=audio_config)

    response = session_client.detect_intent(session=session, query_input=query_input,
        input_audio=input_audio)

    print('=' * 50)
    print('Query text: {}'.format(response.query_result.query_text))
    # print('Detected intent: {} (confidence: {})\n'.format(
    	# response.query_result.intent.display_name,
        # response.query_result.intent_detection_confidence))
    # print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project-id',
        help='Project/agent id.  Required.',
        required=True)
    parser.add_argument(
        '--audio-file-path',
        help='Path to the audio file.',
        required=True)

    args = parser.parse_args()
    detect_intent_audio(args.project_id, args.audio_file_path)