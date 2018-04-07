import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '0404b504'.decode('hex')
P2P_PORT = 5534
ADDRESS_VERSION = 36
RPC_PORT = 5535
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'fireflycoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 120*100000000 >> (height + 1)//2592000
POW_FUNC = data.hash256
BLOCK_PERIOD = 60 # s
SYMBOL = 'FFC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'FireFlyCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/FireFlyCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.FireFlyCoin'), 'FireFlyCoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://208.94.243.138/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://208.94.243.138/address/'
TX_EXPLORER_URL_PREFIX = 'http://208.94.243.138/tx/'
SANE_TARGET_RANGE = (2**256//100000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8