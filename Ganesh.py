from discord import Webhook, RequestsWebhookAdapter, Embed
import __time__


def icon_url():
    return "https://images-ext-2.discordapp.net/external/XnfnaHmjhY6X2sMmA_z-5DoHnj5ZzpfudyBd2ABJ9h0/https/s3.eu-west-2.amazonaws.com/ganeshbotdl/ganesh_logo_square.png"

def send_webhook():
    url = "https://discordapp.com/api/webhooks/699401809206313061/5koJESNpTWnxS2Gu8ZokSGY0Hgd8C8uFDXvTXqsZJFQdfbqvXqDSZqmy1lbfoAB0aUSX"
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='Successful Checkout!', url='https://twitter.com/GaneshBot', color=3329330)
    embed.set_thumbnail(url='http://runnerspoint.scene7.com/is/image/rpe/316701312304')
    embed.add_field(name="\u200b", value='[Track Order](https://footlocker.narvar.com/footlocker/tracking/uk-mail?order_number=31900440404200595851)', inline=False)\
        .add_field(name='Date Time', value='||{}||'.format(__time__.timeStamp()), inline=True)\
        .add_field(name='Store', value='Foorlocker GB', inline=True)\
        .add_field(name='Product', value='Jordan 1 Retro High - Grade School Shoes', inline=False)\
        .add_field(name='Size', value='UK 5.5 / US 6', inline=True)\
        .add_field(name='Order Numver', value='||31900440404200595859||', inline=False)\
        .add_field(name='Proxy', value='||192.168.1.1:8080:user:password||')\
        .set_footer(text='@GaneshBot · {}'.format(__time__.timeStamp()), icon_url=icon_url())
    webhook.send(embed=embed, avatar_url=icon_url(), username='GaneshBot Checkout')

if __name__== '__main__':
    send_webhook()