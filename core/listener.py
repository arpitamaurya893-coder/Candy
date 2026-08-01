import speech_recognition as sr


class Listener:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        # Recognition settings
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.5

        self.calibrated = False

    def listen(self):

        try:

            with sr.Microphone(device_index=1) as source:

                print("🎤 Listening...")

                # Calibrate only once
                if not self.calibrated:

                    print("🔧 Calibrating microphone...")

                    self.recognizer.adjust_for_ambient_noise(
                        source,
                        duration=1
                    )

                    self.calibrated = True

                    print("✅ Microphone ready.")

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

            return command.lower().strip()

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

            print(f"⚠️ Listener Error: {e}")
            return ""