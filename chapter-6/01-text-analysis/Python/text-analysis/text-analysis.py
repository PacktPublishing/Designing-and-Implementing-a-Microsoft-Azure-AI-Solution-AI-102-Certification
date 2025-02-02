from dotenv import load_dotenv
import os

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)


        # Analyze each text file in the reviews folder
        reviews_folder = 'reviews'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Get language
            detected_language = ai_client.detect_language(documents=[text])[0]
            print('\nLanguage: {}'.format(detected_language.primary_language.name))


            # Get sentiment
            sentiment_analysis = ai_client.analyze_sentiment(documents=[text])[0]
            print("\nSentiment: {}".format(sentiment_analysis.sentiment))


            # Get key phrases
            phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
            if phrases:
                print("\nKey Phrases:")
                for phrase in phrases:
                    print('\t{}'.format(phrase))


            # Get entities
            entities = ai_client.recognize_entities(documents=[text])[0].entities
            if entities:
                print("\nEntities")
                for entity in entities:
                    print('\t{} ({})'.format(entity.text, entity.category))


            # Get linked entities
            linked_entities = ai_client.recognize_linked_entities(documents=[text])[0].entities
            if linked_entities:
                print("\nLinks")
                for linked_entity in linked_entities:
                    print('\t{} ({})'.format(linked_entity.name, linked_entity.url))



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()