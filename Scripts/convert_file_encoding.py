import codecs
import os
import sys
import shutil
import re
import chardet

convert_dir = sys.argv[1]
convert_file_types = [".txt"]


# convertfiletypes = [".cpp", ".h", ".hpp"]

def convert_encoding(filename, target_encoding):
    # Backup the origin file.

    # convert file from the source encoding to target encoding
    content = codecs.open(filename, 'rb').read()
    source_encoding = chardet.detect(content)['encoding']
    print(source_encoding, filename)
    if source_encoding != 'utf-8':
        print(source_encoding, filename)
        content = content.decode(source_encoding, 'ignore')  # .encode(source_encoding)
        codecs.open(filename, 'w', encoding=target_encoding).write(content)


def main():
    for root, dirs, files in os.walk(convert_dir):
        for f in files:
            for fileType in convert_file_types:
                if f.lower().endswith(fileType):
                    filename = os.path.join(root, f)
                    try:
                        convert_encoding(filename, 'utf-8')
                    except Exception as e:
                        print(e)


if __name__ == '__main__':
    main()
