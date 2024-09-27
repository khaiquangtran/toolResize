import os
import argparse
import ast
import cv2

def scranFolder(folder_path):
    list_file_path = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            list_file_path.append(file_path)
    return list_file_path

def resize(file_path, size):
    image = cv2.imread(file_path)
    resized_image = cv2.resize(image, size)
    cv2.imwrite(file_path, resized_image)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input path.')
    parser.add_argument('--path', type=str, help='Input folder path (e.g., "C:/Users/YourName")', required=True)
    parser.add_argument('--size', type=str, help='Input size as a tuple (e.g., "(100, 200)")')

    args = parser.parse_args()

    if args.size:
        try:
            args.size = ast.literal_eval(args.size)  # Safely evaluate the tuple string
            if not isinstance(args.size, tuple):
                raise ValueError
        except (ValueError, SyntaxError):
            parser.error("Invalid size format. Use '(width, height)' format.")

    print(f'Path: {args.path}')
    print(f'Size: {args.size}')
    list_fodler_path = scranFolder(args.path)
    for file_path in list_fodler_path:
        resize(file_path, args.size)

