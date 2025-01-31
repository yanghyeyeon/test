import threading
import time
import random
from queue import Queue

# 공유 메모리 역할을 하는 메시지 큐
message_queue = Queue()

class Agent(threading.Thread):
    def __init__(self, name, message_queue):
        super().__init__()
        self.name = name
        self.message_queue = message_queue
        self.running = True

    def send_message(self, message):
        """메시지를 큐에 추가합니다."""
        self.message_queue.put((self.name, message))

    def receive_message(self):
        """큐에서 메시지를 읽습니다."""
        while not self.message_queue.empty():
            sender, message = self.message_queue.get()
            if sender != self.name:  # 자기 자신이 보낸 메시지는 무시
                print(f"[{self.name}] Received message from {sender}: {message}")

    def run(self):
        """에이전트의 메인 루프."""
        while self.running:
            # 랜덤하게 메시지 보내기
            if random.random() < 0.5:
                message = f"Hello from {self.name}!"
                self.send_message(message)

            # 메시지 수신
            self.receive_message()

            # 대기 시간
            time.sleep(random.uniform(0.5, 1.5))

    def stop(self):
        """에이전트 정지."""
        self.running = False

if __name__ == "__main__":
    # 에이전트 생성
    agents = [Agent(f"Agent-{i+1}", message_queue) for i in range(3)]

    # 에이전트 실행
    for agent in agents:
        agent.start()

    try:
        # 10초 동안 실행
        time.sleep(10)
    finally:
        # 에이전트 정지
        for agent in agents:
            agent.stop()

        # 모든 에이전트가 종료될 때까지 기다림
        for agent in agents:
            agent.join()

    print("All agents stopped.")
