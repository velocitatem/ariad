import time
import threading


class PomodoroTimer:
    def __init__(self):
        self.duration = 0  # Duration in seconds
        self.remaining_time = 0
        self.is_running = False
        self.is_paused = False
        self.timer_thread = None

    def start_timer(self, duration):
        self.duration = duration * 60  # Convert to seconds
        self.remaining_time = self.duration
        self.is_running = True
        self.is_paused = False
        self.timer_thread = threading.Thread(target=self.run_timer)
        self.timer_thread.start()
        return f"Timer started for {duration} minutes."

    def run_timer(self):
        while self.remaining_time > 0 and self.is_running:
            if not self.is_paused:
                time.sleep(1)
                self.remaining_time -= 1
        if self.remaining_time == 0:
            print("Timer finished.")
            self.is_running = False

    def pause_timer(self):
        if self.is_running and not self.is_paused:
            self.is_paused = True
            return "Timer paused."
        return "Timer is not running."

    def resume_timer(self):
        if self.is_running and self.is_paused:
            self.is_paused = False
            return "Timer resumed."
        return "Timer is not running or already resumed."

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.remaining_time = 0
            return "Timer stopped."
        return "Timer is not running."

    def reset_timer(self):
        self.is_running = False
        self.is_paused = False
        self.remaining_time = 0
        return "Timer reset."

    def display_time_remaining(self):
        if not self.is_running:
            return "Timer is not running."
        mins, secs = divmod(self.remaining_time, 60)
        return f"Time remaining: {mins:02d}:{secs:02d}."


timer = PomodoroTimer()


def cli_loop():
    while True:
        command = input("Enter command (start/pause/resume/stop/display/reset): ").split()
        action = command[0]
        message = ""
        if action == "start" and len(command) == 2:
            try:
                duration = int(command[1])
                message = timer.start_timer(duration)
            except ValueError:
                message = "Invalid duration. Please enter a number."
        elif action == "pause":
            message = timer.pause_timer()
        elif action == "resume":
            message = timer.resume_timer()
        elif action == "stop":
            message = timer.stop_timer()
        elif action == "display":
            message = timer.display_time_remaining()
        elif action == "reset":
            message = timer.reset_timer()
        else:
            message = "Unknown command. Please use: start, pause, resume, stop, display, reset."

        print(message)


# Entry point for the application
if __name__ == "__main__":
    cli_loop()
