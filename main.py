import xspj
import xxtydc

def main():
    username = input("请输入学号：")
    password = input("请输入密码：")
    xspj.start(username, password)
    xxtydc.start(username, password)

if __name__ == '__main__':
    main()