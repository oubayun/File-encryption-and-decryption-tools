from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA


def Encrypt(filename):
    data = ''
    # 二进制只读打开文件，读取文件数据
    with open(filename, 'rb') as f:
        data = f.read()
    with open(filename, 'wb') as out_file:
        # 收件人秘钥 - 公钥
        recipient_key = RSA.import_key(
            open('rsa_public.key').read())
        #一个 16 字节的会话密钥
        session_key = get_random_bytes(16)
        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)

        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)
    return ("文件: %s 加密成功" % filename)


def Descrypt(filename):
    code = 'muzilee_www.oubayun.com'
    with open(filename, 'rb') as fobj:
        # 导入私钥
        private_key = RSA.import_key(
            open('rsa_private.key').read(),
            passphrase=code)
        # 会话密钥， 随机数，消息认证码，机密的数据
        enc_session_key, nonce, tag, ciphertext = [
            fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
        ]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        # 解密
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    with open(filename, 'wb') as wobj:
        wobj.write(data)
    return ("文件: %s 解密成功" % filename)
