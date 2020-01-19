# GENERAL PERMISSIONS

ADMINISTRATOR = int("0x8", 0)
VIEW_AUDIT_LOG = int("0x80", 0)
MANAGE_SERVER = int("0x20", 0)
MANAGE_ROLES = int("0x10000000", 0)
MANAGE_CHANNELS = int("0x10", 0)
KICK_MEMBERS = int("0x2", 0)
BAN_MEMBERS = int("0x4", 0)
CREATE_INSTANT_INVITE = int("0x1", 0)
CHANGE_NICKNAME = int("0x4000000", 0)
MANAGE_NICKNAMES = int("0x8000000", 0)
MANAGE_EMOJIS = int("0x40000000", 0)
MANAGE_WEBHOOKS = int("0x20000000", 0)

ALL_GENERAL = ADMINISTRATOR + VIEW_AUDIT_LOG + MANAGE_SERVER + MANAGE_ROLES + MANAGE_CHANNELS + KICK_MEMBERS + BAN_MEMBERS + CREATE_INSTANT_INVITE + CHANGE_NICKNAME + MANAGE_NICKNAMES + MANAGE_EMOJIS + MANAGE_WEBHOOKS

# TEXT PERMISSIONS

READ_MESSAGES = int("0x400", 0)
SEND_TTS_MESSAGES = int("0x1000", 0)
EMBED_LINKS = int("0x4000", 0)
READ_MESSAGE_HISTORY = int("0x10000", 0)
USE_EXTERNAL_EMOJIS = int("0x40000", 0)
SEND_MESSAGES = int("0x800", 0)
MANAGE_MESSAGES = int("0x2000", 0)
ATTACH_FILES = int("0x8000", 0)
MENTION_EVERYONE = int("0x20000", 0)
ADD_REACTIONS = int("0x40", 0)

ALL_TEXT = READ_MESSAGES + SEND_TTS_MESSAGES + EMBED_LINKS + READ_MESSAGE_HISTORY + USE_EXTERNAL_EMOJIS + SEND_MESSAGES + MANAGE_MESSAGES + ATTACH_FILES + MENTION_EVERYONE + ADD_REACTIONS

# VOICE PERMISSIONS

VIEW_CHANNEL = int("0x400", 0)
CONNECT = int("0x100000", 0)
MUTE_MEMBERS = int("0x400000", 0)
MOVE_MEMBERS = int("0x1000000", 0)
SPEAK = int("0x200000", 0)
DEAFEN_MEMBERS = int("0x800000", 0)
USE_VOICE_ACTIVITY = int("0x2000000", 0)
PRIORITY_SPEAKER = int("0x100", 0)

ALL_VOICE = VIEW_CHANNEL + CONNECT + MUTE_MEMBERS + MOVE_MEMBERS + SPEAK + DEAFEN_MEMBERS + USE_VOICE_ACTIVITY + PRIORITY_SPEAKER

# EVERYTHING

EVERYTHING = ALL_GENERAL + ALL_TEXT + ALL_VOICE

print("INVITE v1.0.0")
print("Provide a valid bot ID")
try:
    id = int(input())
except ValueError:
    print("Bot ID must be an integer")
    exit()

print("What permissions should the bot have?")
print("Input 8 for default permissions (Administrator)")
print("Input 'Everything' for all the permissions")
print("Input 'General' for all general permissions")
print("Input 'Text' for all text permissions")
print("Input 'Voice' for all voice permissions")
permissions = input()

if permissions == "8":
     print("Here is your invite URL: " + "https://discordapp.com/oauth2/authorize?client_id=" + str(id) + "&permissions=" + str(ADMINISTRATOR) + "&scope=bot")
elif permissions == "Everything":
    print("Here is your invite URL: " + "https://discordapp.com/oauth2/authorize?client_id=" + str(id) + "&permissions=" + str(EVERYTHING) + "&scope=bot")
elif permissions == "General":
    print("Here is your invite URL: " + "https://discordapp.com/oauth2/authorize?client_id=" + str(id) + "&permissions=" + str(ALL_GENERAL) + "&scope=bot")
elif permissions == "Text":
    print("Here is your invite URL: " + "https://discordapp.com/oauth2/authorize?client_id=" + str(id) + "&permissions=" + str(ALL_TEXT) + "&scope=bot")
elif permissions == "Voice":
    print("Here is your invite URL: " + "https://discordapp.com/oauth2/authorize?client_id=" + str(id) + "&permissions=" + str(ALL_VOICE) + "&scope=bot")
else: 
    print("Provide a permission that is listed above")