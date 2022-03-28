from base import *

# 调用deploy.py会获得contract_address
contract_address = '0x08B5dD71Db6299e3FD6E96fcB367Fa4D78b1D961'

nonce = w3.eth.get_transaction_count(my_address)

# 实例化合约对象
storage = w3.eth.contract(address=contract_address, abi=abi)
# 调用addPerson方法
transaction = storage.functions.addPerson('zhangsan', 28).buildTransaction({
    "chainId": chain_id,
    "gasPrice": w3.eth.gas_price,
    "from": my_address,
    "nonce": nonce
})
# 签名
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# 发送交易
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print('add new Person to contract...')
# 等待交易完成
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# 获得people数组中存储的值
result = storage.functions.people(0).call()
print(f'get person info: {result}')
