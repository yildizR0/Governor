import cv2, csv

class Bytes2Disk():
    def __init__(self, framebuffer, csvbuffer):
        super().__init__()
        self.frame_buffer = framebuffer
        self.csv_buffer = csvbuffer

        self.csv = open("collected.csv", "w", newline="")
        self.csv_writer = csv.writer(self.csv)

    def save_frame(self):
        while True:
            while self.frame_buffer:
                filename, frame = self.frame_buffer.popleft()
                cv2.imwrite(filename, frame)

    def save_csv(self):
        while True:
            while self.csv_buffer:
                filename, y, x = self.csv_buffer.popleft()
                self.csv_writer.writerow([filename, y, x])