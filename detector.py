import cv2
from pyzbar.pyzbar import decode

def main():
    # Initialize the webcam (No forced HD resolution, so it runs FAST!)
    cap = cv2.VideoCapture(0)

    print("Starting webcam... Press 'q' to quit.")

    while True:
        success, frame = cap.read()
        
        if not success:
            break

        # --- STEP 1: Convert to Grayscale ---
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # --- STEP 2: Apply Gaussian Blur ---
        # This removes the "pixel grid" noise when scanning a phone screen!
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Decode the blurred, grayscale frame
        detected_objects = decode(blurred_frame)

        for obj in detected_objects:
            (x, y, w, h) = obj.rect
            
            # Draw a green rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

            barcode_data = obj.data.decode('utf-8')
            barcode_type = obj.type

            text = f"{barcode_data} ({barcode_type})"
            
            # Draw the text
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.8, (0, 0, 255), 2)
            
            print(f"Detected {barcode_type}: {barcode_data}")

        # --- STEP 3: Resize the final window to be larger ---
        # The camera captures fast, but we enlarge the window for easy viewing
        display_frame = cv2.resize(frame, (1000, 750))

        # Display the large output screen
        cv2.imshow("Barcode and QR Code Detector", display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()