from collections import OrderedDict
from time import time

from utility.printable import Printable


class DataEntry(Printable):
    """DataEntry which can be added to a block in the blockchain.

    Attributes:
        :entry_address: The entity adding data.
        :content: The information that should be saved on blockchain
        :external_ids: Metadata of the action being carried out ['delivery','raw extraction'].
        :signature: The signature of the transaction.
        :time: the time the information was reported by the entity. Different than when it was recorded on blockchain.
    """

    def __init__(self, entry_address, content, external_ids, signature):
        self.entry_address = entry_address
        self.content = content
        self.external_ids = external_ids
        self.signature = signature

    def to_ordered_dict(self):
        """Converts this data entry into a (hashable) OrderedDict."""
        return OrderedDict([('entry_address', self.entry_address),
                            ('content', self.content),
                            ('external_ids', self.external_ids),
                            ('signature', self.signature)])
