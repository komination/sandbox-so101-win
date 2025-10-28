from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.cameras.opencv.camera_opencv import OpenCVCamera
from lerobot.cameras.configs import ColorMode, Cv2Rotation

# Construct an `OpenCVCameraConfig` with your desired FPS, resolution, color mode, and rotation.
camera_0_config = OpenCVCameraConfig(
    index_or_path=0,
    fps=30.0,
    width=640,
    height=480,
    color_mode=ColorMode.RGB,
    rotation=Cv2Rotation.NO_ROTATION
)

camera_1_config = OpenCVCameraConfig(
    index_or_path=1,
    fps=30.0,
    width=640,
    height=480,
    color_mode=ColorMode.RGB,
    rotation=Cv2Rotation.NO_ROTATION
)

# Instantiate and connect an `OpenCVCamera`, performing a warm-up read (default).
camera_0 = OpenCVCamera(camera_0_config)
camera_0.connect()

camera_1 = OpenCVCamera(camera_1_config)
camera_1.connect()

# Read frames asynchronously in a loop via `async_read(timeout_ms)`
try:
    for i in range(10):
        frame0 = camera_0.async_read(timeout_ms=200)
        frame1 = camera_1.async_read(timeout_ms=200)
        print(f"Async frame {i} from camera 0 shape:", frame0.shape)
        print(f"Async frame {i} from camera 1 shape:", frame1.shape)
finally:
    camera_0.disconnect()
    camera_1.disconnect()