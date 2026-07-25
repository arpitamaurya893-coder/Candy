class Language:

    def detect(self, text):

        hindi_words = [
            "kya",
            "kaise",
            "kaisi",
            "tum",
            "tumhara",
            "aap",
            "mera",
            "meri",
            "mujhe",
            "naam",
            "kar",
            "rahi",
            "ho"
        ]

        text = text.lower()

        for word in hindi_words:
            if word in text:
                return "hindi"

        return "english"