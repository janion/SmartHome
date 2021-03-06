import re

import smart_home.common.Constants as Constants
from smart_home.client_implementations.voice_assistant.commands.Command import Command


class CommandRegex:

    def __init__(self, regex, the_group, item_group, action_group, value_group):
        self.regex = regex
        self.the_group = the_group
        self.item_group = item_group
        self.action_group = action_group
        self.value_group = value_group


class SwitchOnItemCommand(Command):

    # Almost worked: "(?:please ?)?turn (on|off) (?:the ?)?(.*)(?: please?)?"
    SWITCH_ON_X_REGEX = CommandRegex(".*(turn|switch) (%s|%s) ((?:the ?)?)(.*)" % (Constants.ON, Constants.OFF), 3, 4, 1, 2)
    SWITCH_X_ON_REGEX = CommandRegex(".*(turn|switch) ((?:the ?)?)(%s|%s)(.*)" % (Constants.ON, Constants.OFF), 2, 3, 1, 4)
    COMMAND_REGEXES = [SWITCH_ON_X_REGEX,
                       SWITCH_X_ON_REGEX]

    def consume(self, parsed_speech):
        for command in self.COMMAND_REGEXES:
            match = re.match(command.regex, parsed_speech.replace(" please", "").replace("please ", ""))
            if match:
                the = match.group(command.the_group)
                item = match.group(command.item_group).strip()
                action = match.group(command.action_group)
                value = match.group(command.value_group)
                return_data = self.server_connection.update_field(item, value)
                if return_data[Constants.JSON_STATUS] == Constants.JSON_STATUS_OK:
                    self.sound_player.speak("OK", "%sing %s" % (action, value), "%s%s" % (the, item))
                elif return_data[Constants.JSON_STATUS] == Constants.JSON_STATUS_FAIL:
                    print(parsed_speech)
                    print("I'm sorry, I don't know about %s%s" % (the, item.replace("my", "your")))
                    self.sound_player.speak("I'm sorry, I don't know about", "%s%s" % (the, item.replace("my", "your")))
                return True
        return False
