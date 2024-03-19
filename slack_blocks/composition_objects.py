def plain_text(text:str,emoji:bool=True):
    """ Receives text (str) and returns a plain_text object (dict) """
    if text is None:
        return None

    if type(text)==str:
        return {
            "type":"plain_text",
            "text":text,
            "emoji":emoji
        }
        
    if type(text)!=dict:
        raise Exception("Invalid input text")

    if text['type']=="plain_text":
        return text
    else:
        raise Exception("Input text had wrong type")
    

def mrkdwn(text:str, verbatim:bool=None):
    """ Receives text (str) and returns a mrkdwn object (dict)"""
    if text is None:
        return None
    
    if type(text)==str:
        OBJECT = {
            "type":"mrkdwn",
            "text":text
        }

        if verbatim is not None:
            OBJECT['verbatim'] = verbatim
        return OBJECT
    
    if type(text)!=dict:
        raise Exception("Invalid input text")

    if text['type']=="mrkdwn":
        return text
    else:
        raise Exception("Input text had wrong type")

def confirmation(title:str, text:str, confirm:str, deny:str, style:str=None):
    OBJECT = {
        "title":plain_text(title),
        "text":plain_text(text),
        "confirm":plain_text(confirm),
        "deny":plain_text(deny),
    }

    if style in ("red","danger"):
        OBJECT["style"] = "danger"
    elif style in ("green","primary"):
        OBJECT["style"] = "primary"

    return OBJECT

def conversation_filter(include:list,exclude_external_shared_channels:bool=None, exclude_bot_users:bool=None):
    OBJECT = {}
    if include is not None:
        OBJECT['include'] = include

    if exclude_external_shared_channels:
        OBJECT['exclude_external_shared_channels'] = exclude_external_shared_channels
    
    if exclude_bot_users:
        OBJECT['exclude_bot_users'] = exclude_bot_users

    return OBJECT

def dispatch_action_configuration(trigger_actions_on:list):
    OBJECT = {
        "trigger_actions_on":trigger_actions_on
    }
    return OBJECT


def option(text:str, value:str=None, text_type = "mrkdwn"):
    OPTION = {
        "text": mrkdwn(text) if text_type=="mrkdwn" else plain_text(text)
    }

    if value is not None:
        OPTION['value']=value

    return OPTION

def option_group(label:str, options:list, text_type:str = "plain_text"):
    OPTION_GROUP = {
            "label": plain_text(label),
            "options": [option(OPTION,text_type=text_type) for OPTION in options]
        }
    return OPTION_GROUP
    
def trigger(url:str, customizable_input_parameters:list=None):
    OBJECT = {
        "url": url
    }
    if customizable_input_parameters is not None:
        OBJECT['customizable_input_parameters'] =  customizable_input_parameters
    return OBJECT

def workflow(trigger:dict):
    return trigger

def slack_file(url:str=None, id:str=None):
    if url is not None:
        OBJECT = {
            "slack_file":{
                "url":url
            }
        }
    elif id is not None:
        OBJECT = {
            "slack_file":{
                "id":id
            }
        }
    return OBJECT