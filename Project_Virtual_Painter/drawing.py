import cv2

THRESHOLD = 10
colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]
color_index = 0
drawing_color = colors[color_index]
reset_counter = 0  
prev_index_pos = None

def calc_coord(finger_coord, frame):
    h, w, _ = frame.shape
    return int(finger_coord.x * w), int(finger_coord.y * h)

def draw_on_canvas(hand_landmarks, frame, canvas):
    global drawing_color, reset_counter, prev_index_pos, color_index

    index_tip = hand_landmarks.landmark[8]
    index_base = hand_landmarks.landmark[5]
    middle_tip = hand_landmarks.landmark[12]
    middle_base = hand_landmarks.landmark[9]
    ring_tip = hand_landmarks.landmark[16]
    ring_base = hand_landmarks.landmark[13]
    thumb_tip = hand_landmarks.landmark[4]  
    thumb_base = hand_landmarks.landmark[2]  

    index_x, index_y = calc_coord(index_tip, frame)
    _, index_base_y = calc_coord(index_base, frame)
    _, middle_y = calc_coord(middle_tip, frame)
    _, middle_base_y = calc_coord(middle_base, frame)
    _, ring_y = calc_coord(ring_tip, frame)
    _, ring_base_y = calc_coord(ring_base, frame)
    _, thumb_y = calc_coord(thumb_tip, frame)
    _, thumb_base_y = calc_coord(thumb_base, frame)

    index_raised = index_y < index_base_y - THRESHOLD
    middle_raised = middle_y < middle_base_y - THRESHOLD
    ring_raised = ring_y < ring_base_y
    thumb_raised = thumb_y < thumb_base_y - THRESHOLD

    # Stop drawing if two fingers are raised
    if index_raised and middle_raised:
        color_index = (color_index + 1) % len(colors)  
        drawing_color = colors[color_index]

    # Draw when index is raised
    if index_raised and not middle_raised:
        if prev_index_pos is not None:
            cv2.line(canvas, prev_index_pos, (index_x, index_y), drawing_color, thickness=2)
        prev_index_pos = (index_x, index_y)
    else:
        prev_index_pos = None

    # Clear the canvas if thumb is held for 20 frames
    if thumb_raised and not index_raised and not middle_raised:
        reset_counter += 1
        if reset_counter > 20:  
            canvas[:] = 0  
            reset_counter = 0  
    else:
        reset_counter = 0  
