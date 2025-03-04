import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time
import signal
import socket

def resource_path(relative_path):
    """获取资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹，将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # 使用resource_path获取正确的目录路径
        base_dir = resource_path(".")
        super().__init__(*args, directory=base_dir, **kwargs)

def is_port_in_use(port):
    """检查端口是否被占用"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('', port))
            return False
        except socket.error:
            return True

def find_available_port(start_port):
    """查找可用端口"""
    port = start_port
    while is_port_in_use(port):
        port += 1
    return port

# 全局变量存储实际使用的端口
actual_port = None

def start_server():
    global actual_port
    # 查找可用端口
    actual_port = find_available_port(8000)
    Handler = CustomHandler
    
    try:
        with socketserver.TCPServer(("", actual_port), Handler) as httpd:
            print("DeepSeek本地部署中...")
            time.sleep(1)  # 添加短暂延迟使提示更自然
            print("DeepSeek部署完毕.")
            print("关闭窗口停止运行。")
            httpd.serve_forever()
    except Exception as e:
        print(f"服务器启动错误: {e}")
        sys.exit(1)

def signal_handler(signum, frame):
    sys.exit(0)

def main():
    # 注册信号处理器
    signal.signal(signal.SIGINT, signal_handler)
    
    # 启动服务器线程
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = False  # 改为非守护线程
    server_thread.start()
    
    # 等待服务器启动和端口分配
    time.sleep(1)
    
    # 使用实际分配的端口打开浏览器
    webbrowser.open(f'http://localhost:{actual_port}/chat.html')
    
    try:
        # 保持主线程运行
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main() 