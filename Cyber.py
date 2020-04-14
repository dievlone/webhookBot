from discord import Webhook, RequestsWebhookAdapter, Embed
import __time__

def icon_url():
    return "https://cdn.discordapp.com/avatars/620838537742385163/87268e7934f8da3add6bd5621ee610d5.webp?size=128"


def avatar_url():
    return "https://cdn.discordapp.com/avatars/620838537742385163/87268e7934f8da3add6bd5621ee610d5.webp?size=128"

def send_webhook():
    url = "https://discordapp.com/api/webhooks/699401809206313061/5koJESNpTWnxS2Gu8ZokSGY0Hgd8C8uFDXvTgXqsZJFQdfbqvXqDSZqmy1lbfoAB0aUSX"
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title="Successfully checked out!", description='Motion Logo Hooded Sweatshirt', color=3329330)
    embed.set_thumbnail(url="http://assets.supremenewyork.com/185573/ma/JfeTzLouyDg.jpg")\
         .add_field(name='Store', value='Supreme US', inline=True) \
         .add_field(name='Size', value='Medium', inline=True) \
         .add_field(name='Profile', value='||fake||', inline=True) \
         .add_field(name='Order', value='||94685829||', inline=True) \
         .add_field(name='Proxy LIst', value='||dc||', inline=True) \
         .add_field(name='color', value='black', inline=True) \
         .add_field(name='Quantity', value='1', inline=True) \
         .add_field(name='Captcha Bypass', value='Enabled', inline=True) \
         .add_field(name='Mode', value='Safe') \
         .set_footer(text='CyberAIO·{}'.format(__time__.timeStamp()),  icon_url=icon_url())
    webhook.send(embed=embed, username='CyberAIO', avatar_url=avatar_url())

if __name__== '__main__':
    send_webhook()





