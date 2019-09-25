# -*- coding: UTF-8 -*-

import re
import json
import requests

IS_TEST = False


class BaseMsg(object):
    def __init__(self):
        self.msg_type = ""
        self.at_all = False
        self.at_users = []

    def set_at_all(self, at_all):
        self.at_all = at_all

    def add_at_user(self, telephone):
        if self.is_telephone_number(telephone):
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

    # 是否为电话号码
    @staticmethod
    def is_telephone_number(telephone):
        rex = "^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$"
        rp = re.compile(rex)
        return rp.match(telephone)


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

    def set_picUrl(self, pic_url):
        self.picUrl = pic_url

    def set_messageUrl(self, message_url):
        self.messageUrl = message_url

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

    def set_hideAvatar(self, hide_avatar):
        self.hideAvatar = hide_avatar

    def set_btnOrientation(self, btn_orientation):
        self.btnOrientation = btn_orientation

    def set_singleTitle(self, single_title):
        self.singleTitle = single_title

    def set_singleURL(self, single_url):
        self.singleURL = single_url

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

    def add_feed_link(self, title=None, message_url=None, pic_url=None):
        self.links.append({
            "title": title,
            "messageURL": message_url,
            "picURL": pic_url
        })

    def get_data(self):
        return {
            "msgtype": self.msg_type,
            "feedCard": {
                "links": self.links
            }
        }


class MsgClient(object):
    def __init__(self, access_token, test=IS_TEST):
        self.access_token = access_token
        self.test = test

    def __send_real_msg(self, data=None):
        if self.test:
            print json.dumps(data)
            return None
        else:
            if not self.access_token:
                raise Exception("You must set access_token before send message.")
            api = "https://oapi.dingtalk.com/robot/send?access_token=%s" % self.access_token
            return requests.post(url=api, data=json.dumps(data), headers={
                'Content-Type': 'application/json'
            })

    def send_message(self, base_msg):
        if isinstance(base_msg, BaseMsg):
            return self.__send_real_msg(base_msg.get_send_data())
        else:
            raise Exception("not support msg")
