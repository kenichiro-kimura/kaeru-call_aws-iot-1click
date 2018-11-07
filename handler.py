# coding: utf-8
import json
import ConfigParser
from linebot import LineBotApi
from linebot.models import (TextSendMessage, FlexSendMessage, BubbleContainer, CarouselContainer,ImageComponent,BoxComponent,TextComponent)
from linebot.exceptions import LineBotApiError

inifile = ConfigParser.SafeConfigParser()
inifile.read("./config.ini")

def hello(event, context):
    #LINE botのコールバック。取りあえずイベントを全部CloudWatch Logsに出すので
    #ここからgroupIdやroomIdを取得してconfigに反映する(手抜き)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    print json.dumps(body)
    return response

def sendmsg(event, context):
    #各種設定読み込み
    s3url = inifile.get('s3','url')
    groupId = inifile.get('line','targetId')
    line_token = inifile.get('line','token')
    
    #LINE APIオブジェクト作成
    line_bot_api = LineBotApi(line_token)

    #イベント取得してメッセージを作成
    deviceId = event['deviceInfo']['deviceId']
    clickType = event['deviceEvent']['buttonClicked']['clickType']
    
    alttext = u"帰るね"
    cgfile = inifile.get('s3','shortcg');
    if(clickType == "DOUBLE"):
        alttext = u"急いで帰るね"
        cgfile = inifile.get('s3','doublecg');
    if(clickType == "LONG"):
        alttext = u"ごめん、遅くなります"
        cgfile = inifile.get('s3','longcg');

    flex = BubbleContainer(
        hero=ImageComponent(
            size='full',
            url=s3url+cgfile,
        ),
        body=BoxComponent(
            layout='vertical',
            contents=[
                TextComponent(
                    text=babyname+alttext,
                    weight='bold',
                    size='lg'
                )
            ]
        ),
    )

    #|LINEにプッシュメッセージを送る
    line_bot_api.push_message(
        groupId,
        FlexSendMessage(
            alt_text=alttext,
            contents=flex
        )
    )
    return
