import pytube


class y2down():
    def downloadthis(self, link):
        link.streams.first().download()
        return True

    def view(self):
        print('|________________________________________________________|')
        print('|-------------Welcome to YouTube Video Downloader--------|')
        print('|--------------------------------------------------------|')
        y2down.getTheLink('Get the Link')

def main():
    y2down.view('get the link')


if __name__ == "__main__":
    main()
