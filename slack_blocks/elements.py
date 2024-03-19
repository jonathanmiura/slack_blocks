from composition_objects import *

def button(text:str, action_id:str=None, url:str=None, value:str=None, style:str=None, confirm:dict=None, accessibility_label:str=None):
    ELEMENT = {
        "type":"button",
        "text": plain_text(text=text)
    }

    if style in ["red","danger"]:
        ELEMENT['style'] = "danger"
    elif style in ['green', 'primary']:
        ELEMENT['style'] = "primary"

    optional_args = {"action_id":action_id, "url":url, "value":value, "confirm":confirm, "accessibility_label":accessibility_label}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT

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

def overflow(options:list, confirm:dict=None, action_id:str=None):
    ELEMENT = {
        "type":"overflow",
        "options": [option(OPTION) for OPTION in options]
    }
    optional_args = {"action_id":action_id, "confirm":confirm}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def plain_text_input(action_id:str=None, initial_value:str=None, multiline:bool=None, min_length:int=None, max_length:int=None, dispatch_action_config:dict=None, focus_on_load:bool=None, placeholder:str=None):
 
    ELEMENT = {
        "type":"plain_text_input"
    }

    optional_args = {"action_id":action_id,"initial_value":initial_value,"multiline":multiline,"min_length":min_length,"max_length":max_length,"dispatch_action_config":dispatch_action_config,"focus_on_load":focus_on_load,"placeholder":plain_text(placeholder)}
    
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def radio_button(options:list, action_id:str=None, initial_option:str=None, confirm:dict=None, focus_on_load:bool=None):
    ELEMENT = {
        "type":"radio_buttons",
        "options":[option(OPTION) for OPTION in options]
    }

    optional_args = {"action_id": action_id, "initial_option": initial_option, "confirm": confirm, "focus_on_load": focus_on_load}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def static_select(options:list=None, action_id:str=None, option_groups:list=None, initial_option:str=None, confirm:dict=None, focus_on_load:bool=None):
    ELEMENT = {
        "type":"static_select",
    }

    if options is not None:
        ELEMENT['options'] = [option(OPTION) for OPTION in options]
    elif option_groups is not None:
        ELEMENT['option_groups'] = option_groups 
    else:
        raise Exception("Either options or option_groups must be provided!")
    optional_args = {"action_id": action_id, "initial_option": option(initial_option), "confirm": confirm, "focus_on_load": focus_on_load}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def external_select(action_id:str=None, initial_option:str=None, min_query_length:int=None, confirm:dict=None, focus_on_load:bool=None, placeholder:str=None):
    ELEMENT = {
        "type":"static_select",
    }
    
    optional_args = {"action_id": action_id, "initial_option": option(initial_option), "min_query_length": min_query_length, "confirm": confirm, "focus_on_load": focus_on_load, "placeholder": plain_text(placeholder)}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT


def users_select(action_id:str=None, initial_user:str=None, confirm:dict=None, focus_on_load:bool=None, placeholder:str=None):
    ELEMENT = {
        "type":"users_select"
    }
    optional_args = {"action_id": action_id, "initial_user": initial_user, "confirm": confirm, "focus_on_load": focus_on_load, "placeholder": plain_text(placeholder)}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def conversations_select(action_id:str=None, initial_conversation:str=None, default_to_current_conversation:bool=None, confirm:dict=None,
                          response_url_enabled:bool=None, filter:object=None, focus_on_load:bool=None, placeholder:str=None):
    ELEMENT = {
        "type":"conversations_select"
    }
    optional_args = {"action_id": action_id, "initial_conversation": initial_conversation, "default_to_current_conversation": default_to_current_conversation,
                     "confirm": confirm, "response_url_enabled": response_url_enabled, "filter": filter, "focus_on_load": focus_on_load, "placeholder": plain_text(placeholder)}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def channels_select(action_id:str=None, initial_channel:str=None, confirm:dict=None, response_url_enabled:bool=None, focus_on_load:bool=None, placeholder:str=None):
    ELEMENT = {
        "type":"channels_select"
    }
    optional_args = {"action_id": action_id, "initial_channel": initial_channel, "confirm": confirm, "response_url_enabled": response_url_enabled,
                     "focus_on_load": focus_on_load, "placeholder": plain_text(placeholder)}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def timepicker(action_id:str=None, initial_time:str=None, confirm:dict=None, focus_on_load:bool=None, placeholder:str=None, timezone:str=None):
    ELEMENT = {
        "type":"timepicker"
    }

    optional_args = {"action_id": action_id, "initial_time": initial_time, "confirm": confirm, "focus_on_load": focus_on_load, 
                     "placeholder": plain_text(placeholder), "timezone": timezone}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT


def url_text_input(action_id:str=None, initial_value:str=None, dispatch_action_configuration:str=None, focus_on_load:bool=None, placeholder:str=None):
    ELEMENT = {
        "type":"url_text_input"
    }
    optional_args = {"action_id": action_id, "initial_value": initial_value, "dispatch_action_configuration": dispatch_action_configuration,
                     "focus_on_load": focus_on_load, "placeholder": plain_text(placeholder)}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]
    return ELEMENT

def workflow_button(text:str, workflow:dict, action_id:str, style:str=None, accessibility_label:str=None):
    ELEMENT = {
        "type":"workflow_button",
        "text":plain_text(text),
        "workflow": workflow,
        "action_id": action_id
    }

    if style in ["red","danger"]:
        ELEMENT['style'] = "danger"
    elif style in ['green', 'primary']:
        ELEMENT['style'] = "primary"

    optional_args = {"action_id": action_id, "accessibility_label":accessibility_label}
    for KEY in optional_args.keys():
        if optional_args[KEY] is not None:
            ELEMENT[KEY] = optional_args[KEY]

    return ELEMENT

