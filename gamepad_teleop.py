import pygame
from lerobot.robots.so101_follower import SO101Follower, SO101FollowerConfig
import time

# --- ロボットのセットアップ ---
config = SO101FollowerConfig(
    port="COM6",
    id="my_awesome_follower_arm",
    use_degrees=True,
)
robot = SO101Follower(config)
robot.connect()

# 現在姿勢（仮に全部 0 からスタート）
joint_state = {
    "shoulder_pan.pos": 0.0,
    "shoulder_lift.pos": 0.0,
    "elbow_flex.pos": 0.0,
    "wrist_flex.pos": 0.0,
    "wrist_roll.pos": 0.0,
    "gripper.pos": 0.0,
}

# --- pygame / gamepad のセットアップ ---
pygame.init()
pygame.joystick.init()
js = pygame.joystick.Joystick(0)
js.init()

step_deg = 2.0      # 軸入力 1.0 あたり何度動かすか
fps = 60.0
dt = 1.0 / fps

try:
    while True:
        start = time.perf_counter()
        pygame.event.pump()

        # 例: 左スティック x,y を肩パン / 肩リフト に割り当て
        lx = js.get_axis(0)   # -1〜1
        ly = js.get_axis(1)

        joint_state["shoulder_pan.pos"] += lx * step_deg
        joint_state["shoulder_lift.pos"] += -ly * step_deg

        # 必要に応じて他の軸 → 他の関節も追加

        robot.send_action(joint_state)

        # 簡単に FPS を合わせる
        elapsed = time.perf_counter() - start
        if elapsed < dt:
            time.sleep(dt - elapsed)

except KeyboardInterrupt:
    pass
finally:
    robot.disconnect()
    pygame.quit()
