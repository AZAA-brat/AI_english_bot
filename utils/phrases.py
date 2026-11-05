phrases = {
    "ru":
        {"greeting": "Привет! {name}",
         "mode": "Режим сменён",
         "dir": "Направление изменено",
         "choice": "Что будем делать?",
         "error": "Произошла ошибка",
         "wait": "Подождите минутку",
         "translate": "Перевод",
         "grammar": "Грамматика",
         "writing": "Письмо 📝",
         "lang_change": "Поменять язык"
         },
    "en":
        {"greeting": "Hi! {name}",
         "mode": "Mode changed",
         "dir": "Directory changed",
         "choice": "What's on your mind today?",
         "error": "Error occurred",
         "wait": "Wait a minute",
         "translate": "Translate",
         "grammar": "Grammar",
         "writing": "Writing 📝",
         "lang_change": "Change language"
        }
}
def get_phrase(key, lang):
    return phrases[lang][key]