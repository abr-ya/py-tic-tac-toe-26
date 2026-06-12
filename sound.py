import atexit
import math
import shutil
import struct
import subprocess
import sys
import tempfile
import threading
import wave
from pathlib import Path


class ButtonSound:
    def __init__(self, frequency: int = 800, duration: float = 0.08) -> None:
        self.path = self._create_tone(frequency, duration)
        atexit.register(self.path.unlink, missing_ok=True)

    def play(self) -> None:
        if sys.platform == "win32":
            import winsound

            threading.Thread(
                target=winsound.PlaySound,
                args=(str(self.path), winsound.SND_FILENAME),
                daemon=True,
            ).start()
            return

        player = next(
            (
                path
                for name in ("paplay", "pw-play", "aplay")
                if (path := shutil.which(name))
            ),
            None,
        )
        if player:
            subprocess.Popen(
                [player, str(self.path)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

    @staticmethod
    def _create_tone(frequency: int, duration: float) -> Path:
        sample_rate = 44_100
        sample_count = int(sample_rate * duration)
        tone_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        tone_path = Path(tone_file.name)
        tone_file.close()

        with wave.open(str(tone_path), "wb") as wav_file:
            wav_file.setparams(
                (1, 2, sample_rate, sample_count, "NONE", "not compressed")
            )
            for sample in range(sample_count):
                fade = 1 - sample / sample_count
                value = int(
                    12_000
                    * fade
                    * math.sin(2 * math.pi * frequency * sample / sample_rate)
                )
                wav_file.writeframesraw(struct.pack("<h", value))

        return tone_path
