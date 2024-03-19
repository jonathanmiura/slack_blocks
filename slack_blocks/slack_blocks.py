from composition_objects import *
from elements import *

class slack_blocks:
    def __init__(self, surface:str="message"):
        self.message = []
        self.surface = surface

    @property
    def to_string(self):
        """Transform message object into string ready for Slack's block kit builder https://app.slack.com/block-kit-builder/"""
        BLOCKS = {
            "blocks": self.message
        }
        return str(BLOCKS).replace("True","true").replace("False","false")

    def actions(self, elements:list, block_id:str=None):
        BLOCK = {
            "type":"actions",
            "elements": elements
        }

        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self

    def context(self, elements:list, block_id:str=None):
        BLOCK = {
            "type":"context",
            "elements": elements
        }

        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self
    
    def divider(self, block_id:str=None):
        BLOCK = {"type":"divider"}

        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self

    def file(self, external_id:str, source:str="remote", block_id:str=None):
        BLOCK = {
            "type":"file",
            "external_id":external_id,
            "source":"remote"
        }

        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self 
    
    def header(self, text:str, block_id:str=None):
        BLOCK = {
            "type":"header",
            "text":plain_text(text)
        }

        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self
     
    def image(self, alt_text:str, image_url:str=None, slack_file:str=None, title:str=None, block_id:str=None):
        BLOCK = {
            "type":"image",
            "alt_text":plain_text(text),
        }

        if image_url is not None:
            BLOCK["image_url"]=image_url
        elif slack_file is not None:
            BLOCK["slack_file"]=slack_file
        else:
            raise Exception("Either image_url or slack_file must be provided!")
        
        if title is not None:
            BLOCK["title"] = plain_text(title)

        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self
    
    def input(self, label:str, element:list, dispatch_action:bool = False, hint:str=None, optional:bool = False, block_id:str=None):
        BLOCK = {
            "type":"input",
            "element":element,
            "label": plain_text(label),
            "dispatch_action":dispatch_action,
            "optional":optional
        }

        if hint is not None:
            BLOCK['hint'] = hint

        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self
    
    def section(self, text:str=None, fields:list=None, accessory:dict=None, text_type:str='mrkdwn' ,block_id:str=None):
        BLOCK = {
            "type":"section"
        }

        if text is not None:
            BLOCK['text'] = mrkdwn(text) if text_type=='mrkdwn' else plain_text(text)
        elif fields is not None:
            BLOCK['fields'] = fields
        else:
            raise ("Either text or fields must be provided!")

        if accessory is not None:
            BLOCK['accessory']=accessory


        if block_id is not None:
            BLOCK['block_id'] = block_id

        self.message.append(BLOCK)
        return self
    
    def video(self, alt_text:str, title:str, video_url:str, thumbnail_url:str, author_name:str=None, description:str=None, provider_icon_url:str=None, provider_name:str=None, title_url:str=None, block_id:str=None):
        BLOCK = {
            "type":"video",
            "title": plain_text(title),
            "alt_text":alt_text,
            "thumbnail_url": thumbnail_url,
            "video_url": video_url
        }

        if author_name is not None:
            BLOCK['author_name'] = author_name

        if description is not None:
            BLOCK['description'] = plain_text(description)

        if provider_icon_url is not None:
            BLOCK['provider_icon_url'] = provider_icon_url

        if provider_name is not None:
            BLOCK['provider_name'] = provider_name

        if title_url is not None:
            BLOCK['title_url'] = title_url

        if block_id is not None:
            BLOCK['block_id'] = block_id

        return self
    

button_input = button("Click Here!", url = "https://www.google.com", style="danger")

checkbox_input = checkboxes(['charmander','bulbasaur','squirtle'],'pokemon_pick', initial_options=['squirtle'])

date_input = datepicker(action_id="date_pick",placeholder=None)

email_input = email('email_gather')

file_input = file(action_id="file_input", filetypes=["jpeg","png"], max_files=4)

image_element = image(alt_text="example", image_url="https://api.slack.com/img/blocks/bkb_template_images/Streamline-Beach.png")

number_input = number(is_decimal_allowed=True, action_id="number_input")

OPTION_GROUPS = [
    option_group(label="Roupas",options=["calças","camisetas","meias","cuecas"]),
    option_group(label="Higiene",options=["escova","pasta","shampoo","sabonete","desodorante"]),
    option_group(label="Documentos",options=["RG","passaporte","CNH"]),
]

multi_static_select_input = multi_static_select(options=["calças","camisetas","meias","cuecas"])

multi_users_select_input = multi_users_select( action_id="users_select")

multi_conversations_select_input = multi_conversations_select( action_id="conversation_select", default_to_current_conversation=True)
multi_channels_select_input = multi_channels_select( action_id="channel_select")


S = (
    slack_blocks()
    .header("Hello, World!")
    .divider()
    # .section(text="Hello there, stranger", accessory=button_input)
    # .section(text="Select pokemon", accessory=checkbox_input)
    # .section(text="Date pick",accessory=date_input)
    # .input(label="Email",element=email_input)
    # .input(label="File",element=file_input, hint="Your selfie here")
    # .input(label="height",element=number_input)
    # .section(text="Travel Checklist",accessory=multi_static_select_input)
    .input(label='Pick users',element=multi_users_select_input)
    .input(label='Pick conversation',element=multi_conversations_select_input)
    .input(label='Pick channel',element=multi_channels_select_input)

    # .section(text="Hi", accessory=image_element)
    
)

print(S.to_string)