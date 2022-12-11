from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 生成密钥
key = RSA.generate(1024)

# 提取私钥
private_key = RSA.import_key(key.export_key())

# 提取公钥
public_key = RSA.import_key(key.publickey().export_key())

# 要加密的内容
data = b"123456"

# 实例化加密套件
cipher = PKCS1_OAEP.new(public_key)

# 加密
encrypted_data = cipher.encrypt(data)

# 实例化加密套件
cipher = PKCS1_OAEP.new(private_key)

# 解密
data = cipher.decrypt(encrypted_data)
print(data)
