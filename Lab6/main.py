from CachedDL import CachedDownload
from SimpDL import SimpDownload

def main():
    DL = CachedDownload(SimpDownload())

    data1 = DL.download("https://smth.com/1")
    data2 = DL.download("https://smth.com/2")
    data3 = DL.download("https://smth.com/3")

if __name__ == "__main__":
    main()
