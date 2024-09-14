import os
import platform
import argparse

global GLOBAL_CONFIG_OUTPUT_FILE
GLOBAL_CONFIG_OUTPUT_FILE = None

# 获取操作系统类型
def get_os_type():
    os_type = platform.system()
    return os_type

# 获取hosts文件路径
def get_hosts_file_path():
    os_type = get_os_type()
    if os_type == 'Windows':
        return r'C:\Windows\System32\drivers\etc\hosts'
    elif os_type == 'Linux':
        return '/etc/hosts'
    else:
        raise Exception(f"Unsupported OS: {os_type}")

GLOBAL_CONFIG_OUTPUT_FILE = get_hosts_file_path()

# 添加或更新hosts文件条目
def update_hosts_file(domain, ip):
    hosts_file_path = GLOBAL_CONFIG_OUTPUT_FILE

    with open(hosts_file_path, 'r') as file:
        lines = file.readlines()

    entry_exists = False
    new_line = f"{ip} {domain}\n"

    # 检查是否已有对应的域名条目
    for i, line in enumerate(lines):
        if domain in line:
            lines[i] = new_line
            entry_exists = True
            break

    # 如果条目不存在，则追加
    if not entry_exists:
        lines.append(new_line)

    # 写入修改后的内容
    with open(hosts_file_path, 'w') as file:
        file.writelines(lines)

    print(f"Successfully updated hosts file with: {new_line.strip()}")

# 从文件读取内容并更新hosts
def update_hosts_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                ip, domain = line.strip().split()
                update_hosts_file(domain, ip)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update hosts file based on input or file")
    
    # 允许用户选择直接输入或者通过文件导入
    parser.add_argument('--domain', type=str, help="Domain name to add or update in hosts file")
    parser.add_argument('--ip', type=str, help="IP address for the domain")
    parser.add_argument('--file', type=str, help="File containing domain/IP pairs")
	parser.add_argument('--output', type=str, help="Output file")

    args = parser.parse_args()

    try:
    # 确保以管理员/超级用户权限运行
      if os.geteuid() != 0:
          print("This script needs to be run as an administrator (Linux: sudo).")
          exit()
    except:
        pass

    try:
		if args.output:
			GLOBAL_CONFIG_OUTPUT_FILE = args.o
        if args.file:
            update_hosts_from_file(args.file)
        elif args.domain and args.ip:
            update_hosts_file(args.domain, args.ip)
        else:
            print("You need to provide either --file or both --domain and --ip.")
    except Exception as e:
        print(f"An error occurred: {e}")

