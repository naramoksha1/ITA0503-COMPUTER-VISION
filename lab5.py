
import cv2

# Read input video
cap = cv2.VideoCapture("input.mp4")

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frames = []

# Read and store frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Create output video
out = cv2.VideoWriter(
    "reversed_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

# Write frames in reverse order
for frame in reversed(frames):
    out.write(frame)

out.release()

print("Video reversed successfully!")

# Display reversed video
cap = cv2.VideoCapture("reversed_video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Reversed Video", frame)

    if cv2.waitKey(max(1, int(1000/fps))) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
