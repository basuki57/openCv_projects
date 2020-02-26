import cv2

cap = cv2.VideoCapture(0)

def change_res(width, height):
	cap.set(3, width)
	cap.set(4, height)

def frame_rescale(frame, percent = 75):
	height = int(frame.shape[0]*percent/100)
	width = int(frame.shape[1]*percent/100)
	dim = (width, height)
	return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

while True:
		rect, frame = cap.read()
		frame150 = frame_rescale(frame, 150)
		cv2.imshow("frame150", frame150)	
		frame50 = frame_rescale(frame, 50)
		cv2.imshow("frame50", frame50)
		#change_res(50, 50)
		cv2.imshow("Resolution 25", frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break


cap.release()
cv2.destroyAllWindows()