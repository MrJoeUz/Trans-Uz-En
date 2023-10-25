# Trans-Uz-En
Project: English - Uzbek Dictionary

Created: 25.10.2023

Author: Mr. Joe Uz

Telegram:
https://t.me/MrJoeUz
YouTube:
https://youtube.com/MrJoeUz
E-mail:
MrJoeUz@gmail.com
     
Example-1. English - Uzbek:
1-Misol. Inglizcha - O'zbekcha:

from uz_en_dictionary import Translator
d = Translator(from_lang='en', to='uz')
print(d.translate("hi"))

>>> int salom!

Example-2. Uzbek-English:
2-Misol. O'zbekcha - Inglizcha:

from uz_en_dictionary import Translator
d = Translator(from_lang='uz', to='en')
print(d.translate("bomba"))
    
>>> (Russian) bomb.
