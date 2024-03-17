import re
from moviepy.editor import TextClip

class Subtitle():
    def __init__(self):
        self.sync_time = {}

    def pass_args(self, script: str, rate: int):
        self.script = str(script)
        self.rate = int(rate)
        self.clips = []

    def count_syllables(self, word: str):
        vowels = "aeiouy"
        count = 0
        prev_char_was_vowel = False

        for char in word.lower():
            if char in vowels:
                if not prev_char_was_vowel:
                    count += 1
                prev_char_was_vowel = True
            else:
                prev_char_was_vowel = False

        if len(word) == 1:
            count = 1

        return count

    def est_speech(self):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.script)
        words = cleaned_text.split()
        #current_time = 0

        for word in words:
            syllables = self.count_syllables(word)
            word_time = (60 / self.rate) * syllables
            #current_time += word_time
            self.sync_time[word] = round(word_time)

    def subtitle(self):
        elapsed = 0
        for key, value in self.sync_time.items():
            clip = self.generate(key, elapsed, elapsed + value)
            elapsed += value

    def generate(self, word, start_time, end_time, fontsize=50, color="white", bg_color="black", font="Arial"):
        clip = TextClip(word, fontsize=fontsize, color=color, bg_color=bg_color, font=font)
        clip.transparent = True
        self.clips.append(clip.set_start(start_time).set_end(end_time))

    def dump(self):
        return self.clips 

if __name__ == "__main__":
    print("DO NOT RUN THIS FILE DIRECTLY. IT IS A MODULE.")
    print("Please run the main file.")
    print("418 / https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418")
