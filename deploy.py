from base import *

# 构建智能合约对象
storage = w3.eth.contract(abi=abi, bytecode=bytecode)
# 当前区块链中最后一个交易的nonce
nonce = w3.eth.get_transaction_count(my_address)

# 部署智能合约 - 创建交易
transaction = storage.constructor().buildTransaction(
    {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": my_address, "nonce": nonce}
)
# 签名当前交易 - 证明是你发起的交易
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")

# 开始部署 - 发送交易
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print('Waiting for deploy transaction to finish...')
# 等待智能合约部署结果，部署完后，会获得合约的地址
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print('Deployed Done!')
print(f'contract address: {tx_receipt.contractAddress}')