from canvas import detect_handmark
import numpy as np

def main():
    blank_canvas = np.zeros((500, 500, 3), dtype=np.uint8) # Blank canvas
    detect_handmark(blank_canvas)

if __name__ == "__main__":
    main()
