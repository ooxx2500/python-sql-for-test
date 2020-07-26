# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:07:35 2020

@author: 莫再提
"""


   elif event.message.text == "Buttons Template":
        buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text='ButtonsTemplate可以傳送text,uri',
            thumbnail_image_url='顯示在開頭的大圖片網址',
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='VIDEO1',
                    uri='影片網址'
                ),
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='postback1'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)