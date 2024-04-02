import jwt

from datetime import datetime, timezone,timedelta
# 假设这是你的JWT密钥
JWT_SECRET_KEY = 'your-secret-key'


def creatToken(username):
    payload = {
                'user_id': username,
                'exp': datetime.now(timezone.utc) + timedelta(minutes=30)
            }

            # 使用秘钥生成 JWT Token
    print(payload)
    
    jwt_token = jwt.encode(payload=payload, key=JWT_SECRET_KEY, algorithm='HS256')
    return jwt_token

def decodeToken(token):
    # 解码 Token
    decoded_token = jwt.decode(token, JWT_SECRET_KEY,algorithms=['HS256'],verify=True, options={'verify_exp':False})
    print("0-----------------------------")

    # 获取 Payload 中的数据
    user_id = decoded_token['user_id']
    expiration_time = decoded_token['exp']
    b = datetime.fromtimestamp(expiration_time,tz=timezone.utc)
    print(user_id,b)
    a = datetime.now(timezone.utc) 
    print(a,b)

    # 验证 Token 是否过期
    if a > b :
        print('Token 已过期')
        return user_id+" Token 已过期"
    else:
        print('Token 未过期')
        return user_id+" Token 未过期"
    

ss = creatToken("rong")
print(ss)
    
decodeToken(ss)