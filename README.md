
```powershell
lerobot-find-port
```

```powershell
lerobot-calibrate \
  --robot.type=so101_follower \
  --robot.port=COM6 \
  --robot.id=my_awesome_follower_arm

lerobot-calibrate \
  --teleop.type=so101_leader \
  --teleop.port=COM7 \
  -teleop.id=my_awesome_leader_arm
```

```powershell
lerobot-teleoperate \
  --robot.type=so101_follower \ 
  --robot.port=COM6 \
  --robot.id=my_awesome_follower_arm \
  --teleop.type=so101_leader \
  --teleop.port=COM7 \
  --teleop.id=my_awesome_leader_arm  \
  --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" \
  --display_data=true
```

