import cv2
import numpy as np

cap = cv2.VideoCapture(0)
qr_detector = cv2.QRCodeDetector()

chess_piece_map = {
    'white_pawn': 'White Pawn',
    'black_pawn': 'Black Pawn',
    'white_rook': 'White Rook',
    'black_rook': 'Black Rook',
    'white_knight': 'White Knight',
    'black_knight': 'Black Knight',
    'white_bishop': 'White Bishop',
    'black_bishop': 'Black Bishop',
    'white_queen': 'White Queen',
    'black_queen': 'Black Queen',
    'white_king': 'White King',
    'black_king': 'Black King'
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = qr_detector.detectAndDecode(frame)

    if bbox is not None:
        bbox = np.int32(bbox).reshape(-1, 2)

        for i in range(len(bbox)):
            cv2.line(frame, tuple(bbox[i]), tuple(bbox[(i + 1) % len(bbox)]), (0, 255, 0), 2)

        if data:
            chess_piece = chess_piece_map.get(data, 'Unknown Piece')
            print(f"Detected QR code: {data}, Classified as: {chess_piece}")

            cv2.putText(frame, chess_piece, (bbox[0][0], bbox[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("Chess Piece QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
