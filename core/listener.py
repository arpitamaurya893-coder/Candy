import speech_recognition as sr


class Listener:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        try:

            with sr.Microphone(device_index=1) as source:

                print("🎤 Listening...")

                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                audio = self.recognizer.listen(
                    source,
                    timeout=10,
                    phrase_time_limit=5
                )

            command = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print(f"Boss said: {command}")

            return command.lower()

        except sr.WaitTimeoutError:
            print("⌛ No one spoke.")
            return ""

        except sr.UnknownValueError:
            print("🤍 Sorry Boss, I couldn't understand.")
            return ""

        except sr.RequestError:
            print("🌐 Internet Error.")
            return ""

        except Exception as e:
            print(e)
            return ""