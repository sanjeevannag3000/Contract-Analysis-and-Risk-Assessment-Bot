from langdetect import detect

def check_language(text):
    try:
        lang = detect(text)
        return lang == 'en'  # Only allow English
    except:
        return True  # Assume English if detection fails