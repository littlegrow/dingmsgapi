# -*- coding: UTF-8 -*-

import re
import json
import requests

ACCESS_TOKEN = None


# 是否为电话号码
def is_telephone_number(telephone):
    rex = "^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$"
    rp = re.compile(rex)
    return rp.match(telephone)


class BaseMsg(object):
    def __init__(self):
        self.msg_type = ""
        self.at_all = False
        self.at_users = []

    def set_at_all(self, at_all):
        self.at_all = at_all

    def add_at_user(self, telephone):
        if is_telephone_number(telephone):
            self.at_users.append(telephone)
        else:
            raise Exception("telephone number is wrong")

    def get_msg_type(self):
        return self.msg_type

    def get_data(self):
        raise NotImplementedError("error")

    def get_send_data(self):
        data = self.get_data()
        if self.at_all:
            data["at"] = {
                "isAtAll": True
            }
        elif len(self.at_users) > 0:
            data["at"] = {
                "isAtAll": False,
                "atMobiles": self.at_users
            }
        return data


# 文本类型消息
class TextMsg(BaseMsg):
    def __init__(self):
        super(TextMsg, self).__init__()
        self.msg_type = "text"
        self.text = ""

    def set_text(self, txt):
        self.text = txt

    def get_data(self):
        return {
            "msgtype": self.msg_type,
            "text": {
                "content": self.text
            }
        }


# 链接类型消息
class LinkMsg(TextMsg):
    def __init__(self):
        super(LinkMsg, self).__init__()
        self.msg_type = "link"
        self.title = ""
        self.picUrl = ""
        self.messageUrl = ""

    def set_title(self, title):
        self.title = title

    def set_picUrl(self, picUrl):
        self.picUrl = picUrl

    def set_messageUrl(self, messageUrl):
        self.messageUrl = messageUrl

    def get_data(self):
        return {
            "msgtype": self.msg_type,
            "link": {
                "title": self.title,
                "text": self.text,
                "picUrl": self.picUrl,
                "messageUrl": self.messageUrl
            }
        }


class MarkdownMsg(TextMsg):
    def __init__(self):
        super(MarkdownMsg, self).__init__()
        self.msg_type = "markdown"
        self.title = ""

    def set_title(self, title):
        self.title = title

    def get_data(self):
        return {
            "msgtype": self.msg_type,
            "markdown": {
                "title": self.title,
                "text": self.text
            },
        }


class ActionCardMsg(TextMsg):
    def __init__(self):
        super(ActionCardMsg, self).__init__()
        self.msg_type = "actionCard"
        self.title = ""
        self.hideAvatar = "0"
        self.btnOrientation = "0"
        self.singleTitle = ""
        self.singleURL = ""

    def set_title(self, title):
        self.title = title

    def set_hideAvatar(self, hideAvatar):
        self.hideAvatar = hideAvatar

    def set_btnOrientation(self, btnOrientation):
        self.btnOrientation = btnOrientation

    def set_singleTitle(self, singleTitle):
        self.singleTitle = singleTitle

    def set_singleURL(self, singleURL):
        self.singleURL = singleURL

    def get_data(self):
        return {
            "msgtype": self.msg_type,
            "actionCard": {
                "title": self.title,
                "text": self.text,
                "hideAvatar": self.hideAvatar,
                "btnOrientation": self.btnOrientation,
                "singleTitle": self.singleTitle,
                "singleURL": self.singleURL
            }
        }


class FeedCardMsg(BaseMsg):
    def __init__(self):
        super(FeedCardMsg, self).__init__()
        self.msg_type = "feedCard"
        self.links = []

    def add_feed_link(self, title=None, messageURL=None, picUrl=None):
        self.links.append({
            "title": title,
            "messageURL": messageURL,
            "picURL": picUrl
        })

    def get_data(self):
        return {
            "msgtype": self.msg_type,
            "feedCard": {
                "links": self.links
            }
        }


def __sendRealMsg(data=None, test=True):
    if test:
        # 仅打印数据
        print json.dumps(data)
        return None
    else:
        api = "https://oapi.dingtalk.com/robot/send?access_token=%s" % ACCESS_TOKEN
        return requests.post(url=api, data=json.dumps(data), headers={
            'Content-Type': 'application/json'
        })


# 发送消息
def sendMsg(baseMsg, test=True):
    if isinstance(baseMsg, BaseMsg):
        return __sendRealMsg(baseMsg.get_send_data(), test=test)
    else:
        raise Exception("not support msg")
