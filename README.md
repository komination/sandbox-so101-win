
```powershell
lerobot-find-port

lerbot-find-cameras opencv
```

```powershell
lerobot-calibrate `
  --robot.type=so101_follower `
  --robot.port=COM6 `
  --robot.id=my_awesome_follower_arm

lerobot-calibrate `
  --teleop.type=so101_leader `
  --teleop.port=COM7 `
  -teleop.id=my_awesome_leader_arm
```

```powershell
lerobot-teleoperate `
  --robot.type=so101_follower `
  --robot.port=COM6 `
  --robot.id=my_awesome_follower_arm `
  --teleop.type=so101_leader `
  --teleop.port=COM7 `
  --teleop.id=my_awesome_leader_arm  `
  --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}, top: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}" `
  --display_data=true
```

```powershell
lerobot-record `
  --robot.type=so101_follower `
  --robot.port=COM6 `
  --robot.id=my_awesome_follower_arm `
  --robot.cameras="{ front: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}, top: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" `
  --teleop.type=so101_leader `
  --teleop.port=COM7 `
  --teleop.id=my_awesome_leader_arm `
  --display_data=true `
  --dataset.repo_id=${HF_USER}/${MY_DATASET_NAME} `
  --dataset.root=${MY_DATASET_NAME} `
  --dataset.num_episodes=50 `
  --dataset.single_task="MY_TASK" `
  --dataset.episode_time_s=20 `
  --dataset.private=true `
  --dataset.reset_time_s=10 
  
  # 再開時付与
  # --resume=true

  # Upload
  # hf auth login
  # hf upload "$env:HF_USER/$env:MY_DATASET_NAME" "./$env:MY_DATASET_NAME" --repo-type dataset
```

```powershell
lerobot-replay `
  --robot.type=so101_follower `
  --robot.port=COM6 `
  --robot.id=my_awesome_follower_arm `
  --dataset.repo_id=$env:HF_USER/$env:MY_DATASET_NAME `
  --dataset.episode=0 `
  --dataset.root="./$env:MY_DATASET_NAME"
```

```powershell
# シェル変数設定
$env:HF_USER=""
$env:MY_DATASET_NAME=""

# act ver.
lerobot-train `
  --policy.type=act `
  --dataset.repo_id=$env:HF_USER/$env:MY_DATASET_NAME  `
  --dataset.root="./$env:MY_DATASET_NAME" `
  --output_dir=outputs/train/my_act `
  --job_name=my_act_training `
  --policy.device=cuda `
  --wandb.enable=false `
  --policy.repo_id=my-act-policy-v1 `
  --policy.private=true `
  --steps=20000 `
  --batch_size=64 

# smolvla ver
lerobot-train `
  --policy.path=lerobot/smolvla_base `
  --dataset.repo_id=$env:HF_USER/$env:MY_DATASET_NAME `
  --dataset.root="./$env:MY_DATASET_NAME" `
  --batch_size=64 `
  --steps=20000 `
  --output_dir=outputs/train/my_smolvla `
  --job_name=my_smolvla_training `
  --policy.device=cuda `
  --wandb.enable=false `
  --policy.private=true `
  --policy.repo_id=my-smolvla-policy-v1


lerobot-train `
  --policy.type=groot `
  --dataset.repo_id=$env:HF_USER/$env:MY_DATASET_NAME `
  --dataset.root="./$env:MY_DATASET_NAME" `
  --batch_size=64 `
  --steps=20000 `
  --output_dir=outputs/train/gr00t `
  --job_name=my_groot_training `
  --policy.device=cuda `
  --wandb.enable=false `
  --policy.private=true `
  --policy.repo_id=my-gr00t-policy-v1 `
  --save_freq=10 `
  --log_freq=2 
```

```powershell
lerobot-record `
  --robot.type=so101_follower `
  --robot.port=COM6 `
  --robot.id=my_awesome_follower_arm `
  --robot.cameras="{ front: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}, top: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" `
  --dataset.single_task="Grab the red pen and put it in the black box." `
  --dataset.episode_time_s=1600 `
  --dataset.num_episodes=3 `
  --dataset.reset_time_s=10 `
  --display_data=true `
  --policy.repo_id=$env:HF_USER/my-gr00t-policy-v1 `
  --policy.path=$env:HF_USER/my-gr00t-policy-v1 `
  --dataset.push_to_hub=false `
  --policy.device=cuda `
  --dataset.repo_id=$env:HF_USER/eval_$env:MY_DATASET_NAME
```