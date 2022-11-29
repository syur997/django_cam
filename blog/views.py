from .models import Fileupload, getGPS, Filereceive
from django.shortcuts import render, redirect
from .forms import FileUploadForm
import requests
import random
import string
import json

from django.shortcuts import render

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import datetime
import threading


def fileUpload(request):
    if request.method == 'POST':
        title = request.user
        img = request.FILES["imgfile"]
        
        fileupload = Fileupload(
            title=title,
            imgfile=img
        )
        letters=string.ascii_letters
        rand_str = ''.join(random.choice(letters) for i in range(6))
        fileupload.imgfile.name=str(request.user)+'_'+str(request.user.id)+'_'+rand_str+'.jpg'
        fileupload.save()

        pk=fileupload.pk
        fileupload = Fileupload.objects.get(pk=pk)
        test=getGPS('_media/'+str(fileupload.imgfile))
        latitude = test['latitude']
        longitude = test['longitude']
        fileupload.latitude = latitude
        fileupload.longitude = longitude
        fileupload.save()
        print(str(fileupload.imgfile.path))
        requests.post('http://127.0.0.1:8000/post/imgupload', json={'test':str(fileupload.imgfile.path)})
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'blog/fileupload.html', context)

def fileReceive(request):
    if request.method == 'POST':
        tmp=json.loads(request.body.decode())
        print(tmp['test'])
        return render(request, 'blog/fileupload.html')
    return render(request, 'blog/fileupload.html')

#--------------------------------------
# home.html
def home(request):
    return render(request,"home.html") #home.html을 호출해서 띄워준다.

#카메라 관련 클래스
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()



def gen(camera):
    while True:
        frame = camera.get_frame()
        # frame단위로 이미지를 계속 반환한다. (yield)
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def Savepicture():
    video_capture = cv2.VideoCapture(1)

    while (True):

        grabbed, frame = video_capture.read()
        cv2.imshow('Original Video', frame)

        key = cv2.waitKey(1);
        if key == ord('q'):
            break
        elif key == ord('s'):
            file = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + '.jpg'
            cv2.imwrite(file, frame)
            print(file, ' saved')
    video_capture.release()
    cv2.destroyAllWindows()


# detectme를 띄우는 코드(여기서 웹캠을 킨다.)
@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera() #웹캠 호출
        # frame단위로 이미지를 계속 송출한다
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다.")
        pass



#--------------------------------------

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet
from .models import Room, Amenity
from .serializers import testSerial, AmenitySerializer, RoomSerializer, tmpserial

# def see_one_room(request, room_pk):
#     rooms = Room.objects.get(pk=room_pk)
#     return render(request, 'test/one_rooms.html', {'rooms':rooms,},)

# api_뷰 보기, serializers.py와 연계해서 보여줄 요소만 출력

# api보기는 패스 따로 설정 path('api/v1/room/', see_one_room) 과 같은 형태로

# 정보 보내기
# 좋은 방법이지만 한계가 명확. 아래꺼 사용하기
class CategoryViewSet(ModelViewSet):

    serializer_class = testSerial
    queryset = Room.objects.all()


#class Categories(APIView):

    def get(self, request):
        all_room = Room.objects.all()
        serializer = testSerial(all_room, many = True)
        return Response({'ok':'true', "test": serializer.data,})
    
    def post(self, request):
        serializer = tmpserial(data=request.data)
        if serializer.is_valid():
            # save할시에 serializers의 create함수로 넘어감
            new_room = serializer.save()
            
            return Response(tmpserial(new_room).data)
        else:
            return Response(serializer.errors)

#class Category(APIView):
    
    def get_object(slef, pk):
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
        return room

    def get(self, request, pk):
        serializer = testSerial(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        # 부분수정 가능적용 
        serializer = testSerial(self.get_object(pk), data=request.data, partial=True)
        if serializer.is_valid():
            room=serializer.save()
            return Response(testSerial(room).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)    
    
    def post(self, request):
        pass

class AmenityDetail(APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomSerializer(all_rooms.data)








# 보내는 폼은 아래와 같아야 함
# {
# "name":"test22",
# "owner":"admin"
# }