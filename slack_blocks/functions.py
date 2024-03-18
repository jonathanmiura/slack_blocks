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
    

def mrkdwn(text:str):
    """ Receives text (str) and returns a mrkdwn object (dict)"""
    if text is None:
        return None
    
    if type(text)==str:
        return {
            "type":"mrkdwn",
            "text":text
        }
    if type(text)!=dict:
        raise Exception("Invalid input text")

    if text['type']=="mrkdwn":
        return text
    else:
        raise Exception("Input text had wrong type")


def button(text:str, action_id:str=None, url:str=None, value:str=None, style:str=None, confirm:dict=None, accessibility_label:str=None):
    ELEMENT = {
        "type":"button",
        "text": plain_text(text=text)
    }

    optional_args = {"action_id":action_id, "url":url, "value":value, "style":style, "confirm":confirm, "accessibility_label":accessibility_label}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT

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

def checkboxes(options:list, action_id:str = None ,initial_options:list=[], confirm:dict=None, focus_on_load:bool=False, text_type = "mrkdwn"):
    ELEMENT = {
        "type":"checkboxes",
        "options": [option(OPTION,value=OPTION, text_type=text_type) for OPTION in options],
        "focus_on_load":focus_on_load
    }

    initial_options_object = [option(OPTION,value=OPTION, text_type=text_type) for OPTION in initial_options]

    if len(initial_options_object)==0:
        initial_options = None
    else:
        initial_options = initial_options_object


    optional_args = {"action_id":action_id, "confirm":confirm, "initial_options":initial_options}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT

def datepicker(action_id:str=None, initial_date:str=None, confirm:dict=None, focus_on_load:bool=False, placeholder:str=None):
    ELEMENT = {
        "type":"datepicker",
        "focus_on_load":focus_on_load
    }

    if placeholder is not None:
        placeholder = plain_text(placeholder)

    optional_args = {"action_id": action_id, "initial_date": initial_date, "confirm": confirm,  "placeholder": placeholder}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT


# def datetime_picker(action_id:str=None, initial_date:int=None, confirm:dict=None, focus_on_load:bool=False, placeholder:str=None):
#     ELEMENT = {
#         "type":"datetimepicker",
#         "focus_on_load":focus_on_load
#     }

#     optional_args = {"action_id": action_id, "initial_date": initial_date, "confirm": confirm, "placeholder": plain_text(placeholder)}
#     for KEY in optional_args.keys():
#         if optional_args[KEY] is not None:
#             ELEMENT[KEY] = optional_args[KEY]

#     return ELEMENT

def email(action_id:str=None, initial_value:str=None, dispatch_action_config:dict=None, focus_on_load:bool=False,  placeholder:str=None):
    ELEMENT = {
        "type":"email_text_input",
        "focus_on_load":focus_on_load
    }


    optional_args = {"action_id": action_id, "initial_value": initial_value, "dispatch_action_config": dispatch_action_config, "placeholder": plain_text(placeholder)}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT


def file(action_id:str=None, filetypes:list=None, max_files:int=10):
    ELEMENT = {
        "type":"file_input",
        "max_files":max_files
    }

    optional_args = {"action_id": action_id, "filetypes": filetypes}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]


    return ELEMENT


def image(alt_text:str, image_url:str=None, slack_file:dict=None):
    ELEMENT = {
        "type":"image",
        "alt_text":alt_text
    }

    if image_url is not None:
        ELEMENT['image_url'] = image_url
    elif slack_file is not None:
        ELEMENT['slack_file'] = slack_file
    else:
        raise Exception("Either image_url or slack_file must be provided")
    
    return ELEMENT


def multi_static_select(options:list=None, action_id:str=None, option_groups:list=None, initial_options:list=None, confirm:dict=None, focus_on_load:bool=False, placeholder:str=None):
    ELEMENT = {
        "type":"multi_static_select",
        "focus_on_load":focus_on_load,
    }

    if options is not None:
        ELEMENT['options'] = [option(OPTION, text_type='plain_text') for OPTION in options]
    elif option_groups is not None:
        ELEMENT['option_groups'] = option_groups
    else:
        raise Exception("Either options or option_groups must be provided!")
    
    optional_args = {"action_id":action_id, "initial_options":initial_options, "confirm,":confirm, "placeholder":plain_text(placeholder)}


    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT


def multi_external_select(action_id:str=None, min_query_length:int=None, confirm:dict=None, max_selected_items:int=None, focus_on_load:bool=False, placeholder:str=None):
    ELEMENT = {
        "type":"multi_external_select",
        "focus_on_load":focus_on_load,
    }
    
    optional_args = {"action_id":action_id, "min_query_length":min_query_length, "max_selected_items":max_selected_items, "confirm,":confirm, "placeholder":plain_text(placeholder)}

    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT


def multi_users_select(action_id:str=None, initial_users:list=None, confirm:dict=None, max_selected_items:int=None, focus_on_load:bool=False, placeholder:str=None):
    ELEMENT = {
        "type":"multi_users_select",
        "focus_on_load":focus_on_load
    }

    optional_args = {"action_id":action_id, "initial_users":initial_users, "max_selected_items":max_selected_items, "confirm,":confirm, "placeholder":plain_text(placeholder)}

    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT

def multi_conversations_select(action_id:str=None, initial_conversations:list=None, default_to_current_conversation:bool=False, confirm:dict=None, max_selected_items:int=None, filter:dict=None, focus_on_load:bool=False, placeholder:str=None):
    ELEMENT = {
        "type":"multi_conversations_select",
        "focus_on_load":focus_on_load,
        "default_to_current_conversation":default_to_current_conversation
    }

    optional_args = {"action_id":action_id, "initial_conversations":initial_conversations, "max_selected_items":max_selected_items, "confirm,":confirm, "filter":filter, "placeholder":plain_text(placeholder)}

    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT

def multi_channels_select(action_id:str=None, initial_channels:list=None, confirm:dict=None, max_selected_items:int=None, focus_on_load:bool=False, placeholder:str=None):
    ELEMENT = {
        "type":"multi_channels_select",
        "focus_on_load":focus_on_load,
    }

    optional_args = {"action_id":action_id, "initial_channels":initial_channels, "max_selected_items":max_selected_items, "confirm,":confirm, "placeholder":plain_text(placeholder)}

    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT

def number(is_decimal_allowed:bool=False, action_id:str=None, initial_value:str=None, min_value:str=None, max_value:str=None, dispatch_action_config:dict=None, focus_on_load:bool=False, placeholder:str=None):
    ELEMENT = {
        "type":"number_input",
        "is_decimal_allowed":is_decimal_allowed,
        "focus_on_load":focus_on_load
    }

    optional_args = {"action_id":action_id, "initial_value":initial_value, "min_value":min_value, "max_value":max_value, "dispatch_action_config":dispatch_action_config, "placeholder":plain_text(placeholder)}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]


    return ELEMENT

## TO Do

def overflow():
    ELEMENT = {
        "type":"overflow"
    }
    return ELEMENT

def plain_text_input():
    ELEMENT = {
        "type":"plain_text_input"
    }

    return ELEMENT

def radio_button():
    ELEMENT = {
        "type":"radio_buttons"
    }
    return ELEMENT

def static_select():
    ELEMENT = {
        "type":"static_select"
    }
    return ELEMENT

def external_select():
    ELEMENT = {
        "type":"static_select"
    }
    return ELEMENT


def users_select():
    ELEMENT = {
        "type":"users_select"
    }
    return ELEMENT

def conversations_select():
    ELEMENT = {
        "type":"conversations_select"
    }
    return ELEMENT

def channels_select():
    ELEMENT = {
        "type":"channels_select"
    }
    return ELEMENT

def timepicker():
    ELEMENT = {
        "type":"timepicker"
    }
    return ELEMENT


def url_text_input():
    ELEMENT = {
        "type":"url_text_input"
    }
    return ELEMENT

def workflow_button():
    ELEMENT = {
        "type":"workflow_button"
    }
    return ELEMENT

