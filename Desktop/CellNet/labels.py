import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.transform import resize
import json
import os

# === CONFIG ===
tif_path = 'C:/Users/Platypus/Documents/CellNet/Cell Knocked_Figure7.tif' # Path to your .tif file
resize_shape = (64, 64)
output_path = 'manual_click_labels.json'

# === Load all frames ===
print("Loading frames...")
stack = imread(tif_path)
stack_resized = [resize(f, resize_shape) for f in stack]
print(f"Loaded {len(stack_resized)} frames.")

# === Variables to track state ===
clicked_coords = {}
current_frame = [0]  # Mutable for callbacks

# === Event handlers ===
def show_frame(i):
    ax.clear()
    ax.imshow(stack_resized[i], cmap='gray')
    ax.set_title(f'Frame {i} — Click to label, ← / → to scroll')
    fig.canvas.draw_idle()

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        ix, iy = event.xdata, event.ydata
        f = current_frame[0]
        clicked_coords[f] = (ix, iy)
        print(f'✔ Clicked on Frame {f}: ({ix:.2f}, {iy:.2f})') #change to copy pastable format ie {'frame': 5, 'xy': (3.79, 3.66)}

def onkey(event):
    if event.key == 'left':
        current_frame[0] = max(0, current_frame[0] - 1)
        show_frame(current_frame[0])
    elif event.key == 'right':
        current_frame[0] = min(len(stack_resized) - 1, current_frame[0] + 1)
        show_frame(current_frame[0])
    elif event.key == 'escape':
        print("🚪 Exit requested. Saving labels...")
        plt.close()

# === Run the GUI ===
fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', onkey)
show_frame(current_frame[0])
plt.show()

# === After plot is closed ===
if clicked_coords:
    with open(output_path, 'w') as f:
        json.dump(clicked_coords, f)
    print(f"✅ Labels saved to: {os.path.abspath(output_path)}")
else:
    print("⚠️ No clicks recorded.")
