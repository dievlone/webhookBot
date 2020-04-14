from discord import Webhook, RequestsWebhookAdapter, Embed
import __time__

def icon_url():
    return "https://media.discordapp.net/attachments/284082692591583252/585559939746103308/emote.png"


def send_webhook():
    url = "https://discordapp.com/api/webhooks/699401809206313061/5koJESNpTWnxS2Gu8ZokSGY0Hgd8C8uFDXvTXqsZJFQdfbqvXqDSZqmy1lbfoAB0aUSX"
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title="H67799 Checkout Success|Splashforce", url="https://www.google.com/", color=8087790)
    embed.add_field(name="Pid", value='H67799', inline=True)\
        .add_field(name='size', value='6', inline=True)\
        .add_field(name='Price', value='169.95', inline=True)\
        .add_field(name='Order Track URL', value='https://www.adidas.co.uk/', inline=True)\
        .add_field(name='Order Number', value='||AUK22266777||')\
        .set_footer(text='Splashforce {}'.format(__time__.timeStamp()), icon_url=icon_url())
    webhook.send(embed=embed,username='SplashForce', avatar_url=icon_url())

if __name__== '__main__':
    send_webhook()