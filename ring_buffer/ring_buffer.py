class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_index = 0
        self.buffer = []

    def append(self, item):
        # if buffer is not full
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        # Otherwise, set the value of buffer at its current index to item
        self.buffer[self.current_index] = item
        # then increment current index
        self.current_index += 1
        # then check to make sure you haven't reached the max of the buffer
        if self.current_index > (self.capacity - 1):
        # if you have exceeded the max, set the current index back to 0, you've reached the beginning of the ring
            self.current_index = 0

    def get(self):
        return self.buffer