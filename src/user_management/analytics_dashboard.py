class AnalyticsDashboard:

    def __init__(self):
        # Sample communication data
        # Each record has: [channel, message_sent, message_received, message_read]
        self.data = [
            ['email', 100, 90, 80],
            ['sms', 150, 130, 120],
            ['chat', 50, 45, 42],
            ['social_media', 70, 65, 50]
        ]

    def display_statistics(self):
        print("\n-- Analytics Dashboard --")
        print("Channel       | Sent | Received | Read")
        print("---------------------------------------")
        for record in self.data:
            channel, sent, received, read = record
            print(f"{channel.ljust(13)}| {str(sent).ljust(5)} | {str(received).ljust(8)} | {read}")
        print("---------------------------------------")

    def total_sent(self):
        return sum([record[1] for record in self.data])

    def total_received(self):
        return sum([record[2] for record in self.data])

    def total_read(self):
        return sum([record[3] for record in self.data])


def main():
    dashboard = AnalyticsDashboard()
    dashboard.display_statistics()
    print(f"Total Messages Sent: {dashboard.total_sent()}")
    print(f"Total Messages Received: {dashboard.total_received()}")
    print(f"Total Messages Read: {dashboard.total_read()}")

if __name__ == "__main__":
    main()
