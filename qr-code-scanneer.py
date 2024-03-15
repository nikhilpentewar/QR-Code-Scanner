import cv2
from pyzbar.pyzbar import decode

def scan_barcode(image):
    # Perform barcode scanning
    barcodes = decode(image)

    # Process scanned barcodes
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type

        print(f'Barcode Type: {barcode_type}')
        print(f'Barcode Data: {barcode_data}\n')

    return image

# Ask the user whether they want to scan a barcode by image or by camera
while True:
    choice = input('Do you want to scan a barcode by image (i) or by camera (c)? ')

    if choice.lower() == 'i':
        # Read the image or video
        image = cv2.imread('qr.png')

        # Perform barcode scanning and processing
        scanned_image = scan_barcode(image)

        # Display the resulting image
        cv2.imshow('frame', scanned_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice.lower() == 'c':
        # For scanning barcodes in real-time using the camera
        cap = cv2.VideoCapture(0)  # use 0 for the default camera

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Perform barcode scanning and processing
            scanned_frame = scan_barcode(frame)

            # Display the resulting frame
            cv2.imshow('frame', scanned_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    else:
        print('Invalid choice. Please choose either Image "i" or Camera "c".')
        continue

    # Ask the user whether they want to continue or terminate the section
    while True:
        cont = input('Do you want to continue (yes/no)? ')
        if cont.lower() == 'y':
            break
        elif cont.lower() == 'n':
            print('Thank you for using the barcode scanner. bye!')
            exit()
        else:
            print('Invalid choice. Please choose either "y" or "n".')
            continue