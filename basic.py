from gtts import gTTS
import os

tts = gTTS('ฉันอาศัยอยู่ในประเทศไทย. คุณอาศัยอยู่ที่ไหน ?', lang='th')
tts.save('morning.mp3')
os.system("cvlc --play-and-exit morning.mp3")