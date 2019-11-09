import slack


class SlackClient:
    def __init__(self, token, proxy):
        self.web_client = slack.WebClient(token=token, proxy=proxy)

    def list_up_channels(self):
        channels_call = self.web_client.api_call("channels.list")
        if channels_call.get('ok'):
            return channels_call['channels']
        return None

    def list_up_users(self):
        users_call = self.web_client.api_call("users.list")
        if users_call.get('ok'):
            return users_call['members']
        return None

    def send_message(self, arg_id, arg_message):
        response = self.web_client.chat_postMessage(
            channel=arg_id, text=arg_message)
        assert response['ok']

    def send_image(self, arg_id, arg_image):
        response = self.web_client.files_upload(
            channels=arg_id,
            file=arg_image)
        assert response['ok']
