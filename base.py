import os
import json
from web3 import Web3

# 编译 solidity
# https://github.com/iamdefinitelyahuman/py-solc-x
from solcx import compile_standard, install_solc
from dotenv import load_dotenv

load_dotenv()

with open('./Storage.sol', 'r', encoding='utf-8') as f:
    storage_file = f.read()

# 下载0.6.0版本的Solidity编译器
install_solc('0.6.0')

# 编译Solidity时的配置
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        # Solidity文件
        "sources": {"Storage.sol": {"content": storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    # 编译后产生的内容
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    # 版本，与编写智能合约时Solidity使用的版本对应
    solc_version="0.6.0",
)

# 编译后的结果写入文件
with open('compiled_code.json', 'w') as f:
    json.dump(compiled_sol, f)

# 智能合约编译后的字节码（上链的数据）
bytecode = compiled_sol["contracts"]["Storage.sol"]["Storage"]["evm"]["bytecode"]["object"]

# ABI (Application Binary Interface)，用于与智能合约中的方法进行交互的接口
abi = json.loads(compiled_sol["contracts"]["Storage.sol"]["Storage"]["metadata"])["output"]["abi"]

w3 = Web3(Web3.HTTPProvider(os.getenv("RINKEBY_RPC_URL")))
chain_id = int(os.getenv("CHAIN_ID"))

my_address = os.getenv("ACCOUNT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
print(f'my address: {my_address}')
print(f'private key: {private_key}')
