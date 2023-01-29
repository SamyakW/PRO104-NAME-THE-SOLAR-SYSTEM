import cv2

img = cv2.imread("SolarSystem.jpg")

cv2.putText(img,
            "Sun",
            (40,350),
            cv2.FONT_HERSHEY_TRIPLEX,
            1.0,
            (0,0,225)
            )

cv2.putText(img,
            "Mercury",
            (190,270),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (280,270),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (350,270),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (450,270),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (545,465),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (660,465),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (765,465),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (880,465),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            )

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("Named_SolarSystem.jpg",img)