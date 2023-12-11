from django.shortcuts import render
from django.views import View
from pytube import YouTube


class YouTubeDownloader(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            link = request.POST['link']
            video = YouTube(link)

            stream = video.streams.get_lowest_resolution()

            stream.download()
            return render(request,'home.html')
        return render(request,'home.html')
