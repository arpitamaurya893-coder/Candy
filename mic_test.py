import speech_recognition as sr

r = sr.Recognizer()

print("Available Microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(index, ":", name)

print("\nUsing Microphone 12...")

with sr.Microphone(device_index=12) as source:
    print("🎤 Speak NOW...")
    r.adjust_for_ambient_noise(source, duration=2)

    audio = r.listen(
        source,
        timeout=10,
        phrase_time_limit=5
    )

print("✅ Audio Captured!")

try:
    text = r.recognize_google(audio, language="en-IN")
    print("You said:", text)

except Exception as e:
    print("Error:", e)