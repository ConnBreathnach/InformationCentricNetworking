
##### Data Packet
##### ------------
##### Name
##### MetaInfo
##### Content
##### Signature

class DataPacket:
    def __init__(self, name, metaInfo, content, signature):
        self.name = name
        self.metaInfo = metaInfo
        self.content = content
        self.signature = signature

    def __str__(self):
        return self.name

    