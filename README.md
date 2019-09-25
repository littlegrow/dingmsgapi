`python`封装钉钉机器人群消息的发送逻辑，目前仅支持`python2`:


安装：

```
pip install dingmsgapi
```


使用参考：

```
from ding_msg_api import MsgClient
from ding_msg_api import TextMsg, LinkMsg, MarkdownMsg, ActionCardMsg, FeedCardMsg

if __name__ == "__main__":
    # Webhook机器人access_token
    msgClient = MsgClient("****************")

    # @群里所有人发文本消息
    txtMsg = TextMsg()
    txtMsg.set_text(txt="text message")
    txtMsg.set_at_all(True)
    msgClient.send_message(txtMsg)

    # @某个人发文本消息
    txtMsg = TextMsg()
    txtMsg.set_text(txt="text message")
    txtMsg.add_at_user(telephone="***********")
    msgClient.send_message(txtMsg)

    # 发送链接消息
    linkMsg = LinkMsg()
    linkMsg.set_title(title="link message")
    linkMsg.set_text(txt="test")
    linkMsg.set_picUrl(pic_url="")
    linkMsg.set_messageUrl(message_url="")
    msgClient.send_message(linkMsg)

    # 发送markdown格式消息
    markDownMsg = MarkdownMsg()
    markDownMsg.set_title(title="markdown message")
    markDownMsg.set_text(txt="### test")
    msgClient.send_message(markDownMsg)

    # 发送actionCard格式消息
    actionCardMsg = ActionCardMsg()
    actionCardMsg.set_title(title="actioncard message")
    actionCardMsg.set_text(txt="test")
    actionCardMsg.set_singleTitle(single_title="test")
    actionCardMsg.set_singleURL(single_url="")
    msgClient.send_message(actionCardMsg)

    # 发送feedCard格式消息
    feedCardMsg = FeedCardMsg()
    for i in range(2):
        feedCardMsg.add_feed_link(title="test%d" % i, message_url="messageURL%d" % i, pic_url="picUrl%d" % i)
    msgClient.send_message(feedCardMsg)
```



参考文档：

[钉钉开放平台群机器人](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)



祝您工作愉快！！！