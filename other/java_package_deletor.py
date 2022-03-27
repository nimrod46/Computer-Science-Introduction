import os
import zipfile


def main():
    srcfile = input("File name: ")
    if srcfile.split("\\")[-1].find(".zip") == -1:
        srcfile += ".zip"
    dstfile = "temp.zip"
    with zipfile.ZipFile(srcfile) as inzip, zipfile.ZipFile(dstfile, "w") as outzip:
        # Iterate the input files
        for inzipinfo in inzip.infolist():
            # Read input file
            with inzip.open(inzipinfo) as infile:
                content = infile.readlines()

                if content[0].find(b"package") != -1:
                    content = content[1:]
                if content[1].find(b"package") != -1:
                    content = content[1:]

                # Write content
                outzip.writestr(inzipinfo.filename, b''.join(content))
    os.remove(srcfile)
    os.rename(dstfile, srcfile)
    print("success, see: " + srcfile)


if __name__ == '__main__':
    main()
