# Takeover-alert - Subdomain Takeover Finder / Alerter v0.3

Takeover-alert is forked from https://github.com/m4ll0k/takeover. Thanks to @m4ll0k[https://twitter.com/m4ll0k]

This project adds support for Telegram alerts for any targets found vulnerable to Sub-domain takeover.

Sub-domain takeover vulnerability occur when a sub-domain (**subdomain.example.com**) is pointing to a service (e.g: **GitHub**, **AWS/S3**,..) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that sub-domain. For example, if **subdomain.example.com** was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a **CNAME** file containing **subdomain.example.com**, and claim **subdomain.example.com**. For more information: [here](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)


## Supported Services

```
'Acquia'
'ActiveCampaign'
'Aftership'
'Aha'
'AWS/S3'
'Bigcartel'
'BitBucket'
'Brightcove'
'Campaignmonitor'
'Cargo'
'CloudFront'
'Desk'
'Fastly'
'FeedPress'
'GetResponse'
'Ghost'
'Github'
'Helpjuice'
'Helpscout'
'Heroku'
'Intercom'
'Jetbrains'
'Kajabi'
'Mashery'
'Pantheon'
'Pingdom'
'Proposify'
'S3Bucket'
'Shopify'
'Simplebooklet'
'Smartling'
'StatuPage'
'Surge'
'Surveygizmo'
'Tave'
'TeamWork'
'Thinkific'
'Tictail'
'Tilda'
'Tumbler'
'Unbounce'
'Uservoice'
'Vend'
'Webflow'
'Wishpond'
'Wordpress'
'ZenDesk'
'feedpress'
'readme'
'statuspage'
'zendesk'   
'worksites.net'                                    
'smugmug'
```
## Installation:

```shell
git clone git@github.com:VikzSharma/takeover-alert.git
cd takeover-alert
python3 setup.py install
```
## Usage

```
Add domains in targets.txt

$ python3 takeover.py -d www.domain.com -v 
$ python3 takeover.py -d www.domain.com -v -t 30
$ python3 takeover.py -d www.domain.com -p http://127.0.0.1:8080 -v 
$ python3 takeover.py -d www.domain.com -o <output.txt> or <output.json> -v 
$ python3 takeover.py -l targets.txt -o output.txt -p http://xxx.xxx.xxx.xxx:8080 -v 
$ python3 takeover.py -l targets.txt -o output.txt -T 3 -v 

```
## Configure Telegram Alerts
To configure Telegram notifications, you need to add your Telegram API key and chat_id to the code or in environment variables . You can read how to get these values [here](https://blog.r0b.re/automation/bash/2020/06/30/setup-telegram-notifications-for-your-shell.html).

$ export TAKEOVER_TELEGRAM_TOKEN = "TelegramToken" <br>
$ export TAKEOVER_TELEGRAM_CHAT_ID = "TelegramChatID"

To create a cron script to run Takeover-alert regularly:
```
crontab -e
```

create an entry like this:
```
@daily /path/to/alert-takeover.sh
```

This will run Takeover-alert once a day, at midnight.
You can change ``@daily`` to whatever schedule suits you. 


## Docker support

Build the image:

```
docker build -t takeover .
```

Run the container:

```
docker run -it --rm takeover -d www.domain.com -v
```

