import cv2
 
foreground = cv2.imread('logo.png')
cap = cv2.VideoCapture("sample.mp4")

# position of logo on video
top_left = [0,0] # the top-left corner of your logo goes here
tx = top_left[0] 
ty = top_left[1]

# crop of logo
left = 0
right = 170
top = 0 # y = 0 is the top of the image
bottom = 170

# calculate width and height of logo crop
width = right - left
height = bottom - top


alpha = 0.5
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

while True:
    ret, background = cap.read()

    # get crops of background and logo
    background_slice = background[ty:ty+height, tx:tx+width]; 
    logo_slice = foreground[top:bottom, left:right]; 

    # add slice of logo onto slice of background
    added_image = cv2.addWeighted(background_slice,alpha,logo_slice,1-alpha,0)
    background[ty:ty+height, tx:tx+width] = added_image

    # show image
    cv2.imshow('a',background)
    out.write(background)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()