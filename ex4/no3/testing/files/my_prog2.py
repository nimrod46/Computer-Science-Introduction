# NEVER USE: ECB is not secure!
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
 
class my3Des:
    def __init__(self, key, mode, iv=b"\x00"*8):
        if mode.upper() == "ECB":
            self.__desCipher = Cipher(
                algorithms.TripleDES(key),
                modes.ECB(),
                backend=default_backend())
        elif mode.upper() == "CBC":
            self.__desCipher = Cipher(
                algorithms.TripleDES(key),
                modes.CBC(iv),
                backend=default_backend())
        elif mode.upper() == "CTR":
            self.__desCipher = Cipher(
                algorithms.TripleDES(key),
                modes.CTR(iv),
                backend=default_backend())
        else:
            raise ValueError("illegal mode")
        
    def encrypt(self, ptext):
        desEncryptor = self.__desCipher.encryptor() 
        padder = padding.PKCS7(64).padder()
        padded_data = padder.update(ptext) + padder.finalize()
        return desEncryptor.update(padded_data) + desEncryptor.finalize()
    
    def decrypt(self, ctext):
        desDecryptor = self.__desCipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        padded_ptext = desDecryptor.update(ctext) + desDecryptor.finalize()
        return unpadder.update(padded_ptext) + unpadder.finalize()
           
        
        


            
            
            
            
            
            
            
            
            
            
            