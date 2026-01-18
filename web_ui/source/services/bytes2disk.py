import cv2, csv, time

class Bytes2Disk():
    def __init__(self, framebuffer, csvbuffer):
        super().__init__()
        self.frame_buffer = framebuffer
        self.csv_buffer = csvbuffer

        self.csv = open("collected.csv", "w", newline="")
        self.csv_writer = csv.writer(self.csv)

    def save_frame(self):
        while True:
            if self.frame_buffer:
                filename, frame = self.frame_buffer.popleft()
                cv2.imwrite(filename, frame)
            else:
                print("a")
                time.sleep(0.01)

    def save_csv(self):
        while True:
            if self.csv_buffer:
                filename, y, x = self.csv_buffer.popleft()
                self.csv_writer.writerow([filename, y, x])
            else:
                print("a")
                time.sleep(0.01)