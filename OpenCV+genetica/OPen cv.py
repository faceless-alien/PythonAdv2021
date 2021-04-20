import cv2,random,numpy,threading,time

images=[]
threads=[]
img=cv2.imread('bimba.jpg')
print(img.shape)
blank_img=cv2.imread('blank_bimba.jpg')

def Generate_new_img(example):
    for i in range(example.shape[0]):
        for j in range(example.shape[1]):
            example[i][j]=numpy.array([numpy.uint8(random.randint(0,255)),numpy.uint8(random.randint(0,255)),numpy.uint8(random.randint(0,255))])
    return example
def Thread_func():
    global images
    a=[]
    for i in range(1):
        a.append(Generate_new_img(blank_img))
    images+=a
def mutate(img):
    c=[1,-1]
    for i in range(img.shape[0]//10):
        for j in range(img.shape[1]//10):
            random_x=random.randint(0,img.shape[0]-1)
            random_y=random.randint(0,img.shape[1]-1)
            
            rand_int=random.randint(1,3)
            if rand_int==1:
                img[random_x][random_y][0]+=random.choice(c)
            elif rand_int==2:
                img[random_x][random_y][1]+=random.choice(c)
            else:
                img[random_x][random_y][2]+=random.choice(c)
    return img[random_x][random_y]
def Compare_with_example(image,example):
    perfect_pixels=1
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0]==example[i][j][0] or image[i][j][0]+1==example[i][j][0] or image[i][j][0]-1==example[i][j][0]:
                if image[i][j][1]==example[i][j][1] or image[i][j][1]+1==example[i][j][1] or image[i][j][1]-1==example[i][j][1]:
                    if image[i][j][2]==example[i][j][2] or image[i][j][2]+1==example[i][j][2] or image[i][j][2]-1==example[i][j][2]:
                        perfect_pixels+=1
    if perfect_pixels/(image.shape[0]*image.shape[1])>=0.8:
        return True
    print(str(perfect_pixels)+' идеальных пикселей' )
threads.append(threading.Thread(target=Thread_func))
threads[0].start()
while threading.active_count()>1:
    pass
print('Сгенерировано')
perfect_image=False
iterations=0
while not perfect_image:
    iterations+=1
    for i in images:
        i=mutate(i)
    for i in images:
        img=cv2.imread('bimba.jpg')
        if Compare_with_example(i, img):
            cv2.imshow('Кек',i)
            cv2.waitKey(0)
            perfect_image=True
            break
    print('Прошла '+str(iterations) +' итерация')