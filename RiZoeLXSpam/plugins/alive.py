from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/8f38c2a68e7a4c2e3f6c9.jpg"
  

          
rizoel = "â§ ð·ð¹ð¶ð­ð¬ðºðºð¶ð¹ ðºð·ð¨ð´ðºð»ð¬ð¹ðº â§\n\n"

rizoel += f"ââââââââââââââââââââ\n"

rizoel += f"â£â£ **á´Êá´Êá´É´ á´ á´ÊsÉªá´É´** : `3.9.6`\n"

rizoel += f"â£â£ **á´á´Êá´á´Êá´É´ á´ á´ÊsÉªá´É´** : `{version.__version__}`\n"

rizoel += f"â£â£ **á´Êá´Òá´ssá´Ê sá´á´á´sá´á´Ês**  : `{rizoelversion}`\n"

rizoel += f"ââââââââââââââââââââ\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("á´Êá´É´É´á´Ê", "https://t.me/AGORABOT_INFO"),
        Button.url("sá´á´á´á´Êá´", "https://t.me/AGORA_SPAM_OFFICIAL")
        ],
        [
        Button.url("â¢ Êá´á´á´ â¢", "https://github.com/Agora-OS/PROFESSOR-SPAMSTERS")
        ]
        ]
        )
    
