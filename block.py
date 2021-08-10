from time import time

from utility.printable import Printable


class Block(Printable):
    """Each block has these attributes

    Attributes:
        :index: the blocks index
        :previous_hash: previous block hash
        :timestamp: When the block has been successfully mined the time is stored. This is not the time of the original transactions. a timestamp for reach transaction or data entry could be done
        :transactions: This is usually saved as merkle tree, but here it is a list of tansactions saved in block.
	:data_entry: This is content stored to blocks that is not the sending of money.
        :proof: This is a number resulting from our nonce value and hashing of transactions.
    """

    def __init__(self, index, previous_hash, transactions, data_entry, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.data_entry = data_entry
        self.proof = proof
