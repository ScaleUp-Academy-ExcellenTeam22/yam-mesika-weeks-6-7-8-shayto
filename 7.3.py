class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

                Args:
                    sender (str): The message sender's username.
                    recipient (str): The message recipient's username.
                    message_body (str): The body of the message.
                    urgent (bool, optional): The urgency of the message.
                                            Urgent messages appear first.

                Returns:
                    int: The message ID, auto incremented number.

                Raises:
                    KeyError: If the recipient does not exist.

                Examples:
                    After creating a PO box and sending a letter,
                    the recipient should have 1 message in the
                    inbox.

                    >>> po_box = PostOffice(['a', 'b'])
                    >>> message_id = po_box.send_message('a', 'b', 'Hello!')
                    >>> len(po_box.boxes['b'])
                    1
                    >>> message_id
                    1
                """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=None):
        """
            The function receives username and n - number of messages he wishes to read.
            The function will return the first n messages in the user's inbox.
            If n not sent (specified)- returns all messages in the user's inbox.
            The messages will be marked as read and will not be returned to the user on the next call.
            :param str username: The username that wants to read message.
            :param int n: The number of messages the user wants to read.
            :return: List of - the first n messages in the user's inbox or all messages in the user's inbox.
            :rtype: list
            :raises KeyError: if the username does not exist and
            if the value of n is greater than the number of messages of username.
            """
        read_messages = []
        user_box = self.boxes[username]

        if n is not None:
            for message in user_box[0:n]:
                if not message["read"]:
                    message["read"] = True
                    read_messages.append(message["body"])
            return read_messages

        else:
            return [message["body"] for message in user_box]

    def search_inbox(self, username, string) -> list:
        """
        This function returns the user messages that contain the passed string
        :param str username: The message sender's username.
        :param string: string we want in the messages
        :return list: the messages that contain the passed string
        :rtype: list
        """
        return [msg for msg in self.boxes[username] if string in msg['body']]


class Message:
    """A Message class. Manages the user's message, can present the message.
        :ivar int message_id: Incremental id of the message.
        :ivar string message_body: The body of the message.
        :ivar string sender: The name of the sender.
        :ivar boolean read: Indicates whether the message was read or not.
        """
    def __init__(self, message_id, message_body, sender, read):
        self.message_id = message_id
        self.sender = sender
        self.message_body = message_body
        self.read = read

    def __str__(self):
        """
        The function styles the message and returns string.
        :return:
        """
        return f"""This message is from {self.sender}.\nThe message is as follows:\n{self.message_body}."""


if __name__ == "__main__":
    message = Message(0, "hello", "Shay", True)
    print(message)
