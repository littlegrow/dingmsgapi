
`python`封装钉钉`Webhook`机器人消息发送逻辑，目前仅支持`python2`。


### 安装

```
pip install dingmsgapi
```

<br>

### 初始化实例

<br>

```
from ding_msg_api import MsgClient
# Webhook机器人access_token
msgClient = MsgClient("****************")
```

<br>

### 发送Text消息

<br>

```
from ding_msg_api import TextMsg

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
```


<br>

### 发送Link消息

<br>

```
from ding_msg_api import LinkMsg

linkMsg = LinkMsg()
linkMsg.set_title(title="link message")
linkMsg.set_text(txt="test")
linkMsg.set_picUrl(pic_url="")
linkMsg.set_messageUrl(message_url="")
msgClient.send_message(linkMsg)
```


<br>

### 发送Markdown消息

<br>

```
from ding_msg_api import MarkdownMsg

markDownMsg = MarkdownMsg()
markDownMsg.set_title(title="markdown message")
markDownMsg.set_text(txt="### test")
msgClient.send_message(markDownMsg)
```

<br>

### 发送ActionCard消息

<br>

```
from ding_msg_api import ActionCardMsg

actionCardMsg = ActionCardMsg()
actionCardMsg.set_title(title="actioncard message")
actionCardMsg.set_text(txt="test")
actionCardMsg.set_singleTitle(single_title="test")
actionCardMsg.set_singleURL(single_url="")
msgClient.send_message(actionCardMsg)
```

<br>

### 发送FeedCard消息

<br>

```
from ding_msg_api import FeedCardMsg

feedCardMsg = FeedCardMsg()
for i in range(5):
    feedCardMsg.add_feed_link(title="test%d" % i, message_url="messageURL%d" % i, pic_url="picUrl%d" % i)
msgClient.send_message(feedCardMsg)
```

<br>

### 参考文档

<br>

[钉钉开放平台群机器人](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)

<br><br>



祝您工作愉快！！！