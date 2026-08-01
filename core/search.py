import webbrowser
import urllib.parse


class Search:

    def execute(self, command):

        command = command.lower().strip()

        # ---------- Google Search ----------
        search_triggers = [
            "search ",
            "google ",
            "find ",
            "look for "
        ]

        for trigger in search_triggers:

            if command.startswith(trigger):

                query = command[len(trigger):].strip()

                if query:
                    url = (
                        "https://www.google.com/search?q="
                        + urllib.parse.quote(query)
                    )

                    webbrowser.open(url)

                    return f"Searching Google for {query}, Boss."

        # ---------- YouTube Search ----------
        youtube_triggers = [
            "play ",
            "youtube ",
            "youtube pe ",
            "youtube par "
        ]

        for trigger in youtube_triggers:

            if command.startswith(trigger):

                query = command[len(trigger):].strip()

                if query:
                    url = (
                        "https://www.youtube.com/results?search_query="
                        + urllib.parse.quote(query)
                    )

                    webbrowser.open(url)

                    return f"Searching YouTube for {query}, Boss."

        return None